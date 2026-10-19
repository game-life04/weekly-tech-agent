"""命令行入口。

python -m wta run       抓取 → 去重 → 打分 →（大模型选稿、写中文摘要）→ 生成页面；上周的快讯还没有就顺带生成
python -m wta kuaixun   单独生成（或重新生成）某一周的快讯
python -m wta render    不抓取，只用 data/ 里已有的数据重新生成所有页面
python -m wta check     逐个测试来源，打印条数和样例（加来源、排查问题时用）
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import sys
from collections import Counter
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Any

from . import editor, excerpt, kuaixun, store
from .collect import collect
from .config import load_config
from .dates import local_date, local_time, parse_time, to_iso, week_id
from .dedupe import dedupe
from .health import failing_sources, step_summary
from .http import Http
from .llm import LLMClient, build_client
from .models import SECTIONS, Item
from .publish import publish, publish_all, publish_indexes, publish_kuaixun, save_week_note, week_payloads
from .rank import apply_scores, select
from .sources import SOURCES
from .sources.base import Context
from .textutil import KeywordMatcher

log = logging.getLogger("wta")


def _context(config: dict[str, Any], now: datetime) -> Context:
    return Context(http=Http(), now=now, keywords=KeywordMatcher(config["keywords"]), env=os.environ)


def _keep(item: Item, config: dict[str, Any]) -> bool:
    """大模型打完分以后，决定一条候选要不要留下。"""
    settings = config["llm"]
    if item.extra.get("filtered") and settings["drop_filtered"]:
        return False  # 被内容审核拦下的不登
    if item.extra.get("needs_review"):  # 相关性存疑的：大模型明确给了高分才留
        return item.extra.get("llm_score", -1) >= settings["review_min_score"]
    return True


def _shortlist(pool: list[Item], config: dict[str, Any]) -> list[Item]:
    """挑出送去给大模型打分的候选：每个来源只留规则分最高的几条，再取总分最高的一批。

    不先按来源裁剪的话，条数多的来源（Hacker News、GitHub 新项目）会占满名额，
    权重低的订阅永远轮不到被大模型看一眼。相关性存疑的条目全部保留，等大模型判断。
    """
    select_config = config["select"]
    taken: Counter[tuple[str, str]] = Counter()
    kept: list[Item] = []
    for item in sorted(pool, key=lambda item: item.score, reverse=True):
        origin = (item.section, item.via or item.source)
        limit = select_config["caps"].get(origin[1], select_config["per_source_cap"]) * 3
        if item.extra.get("needs_review") or taken[origin] < limit:
            taken[origin] += 1
            kept.append(item)
    return kept[: config["llm"]["max_candidates"]]


def _edit(
    pool: list[Item], config: dict[str, Any], client: LLMClient | None, now: datetime, http: Http | None = None
) -> list[Item]:
    """打分 → 按名额选稿 → 给入选的写中文。任何一步出错都退回到“只按规则选稿”。"""
    quotas = {s: config["sections"][s]["daily"] for s in SECTIONS}
    cap, caps = config["select"]["per_source_cap"], config["select"]["caps"]
    apply_scores(pool, now)
    if client:
        try:
            editor.score(_shortlist(pool, config), client)
        except Exception:  # 大模型这一步的任何意外都不能让日报出不来
            log.exception("大模型打分出错，本次按规则选稿")
    pool = [item for item in pool if _keep(item, config)]
    apply_scores(pool, now)
    selected = select(pool, quotas, cap, caps)
    if client:
        for _ in range(2):  # 写摘要时才被审核拦下的条目要去掉；去掉后用后面的候选补一次位
            try:
                excerpt.enrich(selected, http)  # 缺简介的 AI 动态到原文网页里取一段，好写摘要
                editor.summarize(selected, client)  # 已经写过的会跳过，第二轮只请求补进来的
            except Exception:
                log.exception("大模型写摘要出错，标题保持原文")
                break
            if all(_keep(item, config) for item in selected):
                break
            pool = [item for item in pool if _keep(item, config)]
            selected = select(pool, quotas, cap, caps)
        selected = [item for item in selected if _keep(item, config)]
    return selected


def _llm_label(items: list[Item], client: LLMClient | None, existing: dict[str, Any] | None) -> dict[str, str] | None:
    """页面上的“由 AI 生成”以实际发生的事为准：有哪家服务真的回复过、入选内容里真的有中文。"""
    if not any(item.title_zh or item.summary_zh for item in items):
        return None
    answered = client.answered if client else []
    if not answered:
        return (existing or {}).get("llm")  # 这次没用上，但入选内容里有之前写好的中文
    names = "、".join(dict.fromkeys(p.name for p in answered))
    return {"provider": names, "model": "、".join(dict.fromkeys(p.model for p in answered))}


def _kuaixun(
    root: Path, config: dict[str, Any], monday: date, client: LLMClient | None, ctx: Context, reuse: bool = True
) -> None:
    """生成（或补全）monday 这一周的快讯并写出页面。出任何意外都只记日志，不影响日报。"""
    try:
        issue = kuaixun.build(root, config, monday, client=client, http=ctx.http, env=ctx.env, now=ctx.now, reuse=reuse)
    except Exception:
        log.exception("生成每周快讯出错，本次跳过")
        return
    save_week_note(root, issue["week"], {"kuaixun": issue})
    publish_kuaixun(root, config, issue)
    log.info("%s 的快讯：%d 条，大模型还有 %d 条没写成", issue["week"], len(issue["entries"]), issue["pending"])


def _kuaixun_due(root: Path, config: dict[str, Any], today: date, client: LLMClient | None) -> date | None:
    return kuaixun.due(root, today, client is not None) if config["kuaixun"]["enabled"] else None


def _fill_in(root: Path, config: dict[str, Any], day: date, today: date, existing: dict[str, Any], no_llm: bool) -> int:
    """这一天的日报已经有了：不重新抓取，只把之前没写成的中文补上；上周的快讯该生成或补全的话也在这里做。

    大模型在白天常常过载，一次运行里总有几条写不成。定时任务一天触发几次，
    第一次负责出刊，后面几次走到这里：没什么可补的时候什么都不做。
    """
    items = store.items_of(existing)
    withdrawn = editor.recheck(items)  # 检查规则改进以后，已经登出的中文也按新规则复查，不合格的撤下
    client = build_client(config, os.environ) if config["llm"]["enabled"] and not no_llm else None
    tried = 0
    if client:
        try:
            tried = excerpt.enrich(items)  # 缺简介的 AI 动态到原文网页里取一段；每条只试一次
        except Exception:
            log.exception("取原文摘录出错，跳过")
    todo = [item for item in items if not item.extra.get("llm_done") and not item.extra.get("filtered")]
    week = _kuaixun_due(root, config, today, client)
    if not (withdrawn or tried or week) and (client is None or not todo):
        log.info("%s 的日报已经有了，跳过（去掉 --if-missing 可以强制刷新）", day)
        return 0
    waiting = f"，{week_id(week)} 的快讯待生成" if week else ""
    log.info("%s 的日报已经有了，不重新抓取：还有 %d 条没写中文%s", day, len(todo), waiting)
    if client and todo:
        try:
            editor.summarize(items, client)
        except Exception:
            log.exception("大模型写摘要出错，保持原样")
        items = [item for item in items if _keep(item, config)]  # 这次才被内容审核拦下的，撤掉
    # 没有大模型也要保存：复查撤下的中文不能再登出去；试过的摘录也要记下，免得下次再请求同一个网页
    if (client and todo) or withdrawn or tried:
        payload = {**existing, "llm": _llm_label(items, client, existing), "items": [item.to_dict() for item in items]}
        store.save_day(root, day, payload)
    if week:
        _kuaixun(root, config, week, client, _context(config, datetime.now(UTC)))
    for warning in publish(root, config, day) if day == today else publish_all(root, config):
        log.warning(warning)
    return 0


def cmd_run(root: Path, config: dict[str, Any], args: argparse.Namespace) -> int:
    now = datetime.now(UTC)
    today = local_date(now, config["utc_offset_hours"])
    day: date = args.date or today
    if day > today:
        log.error("--date 不能晚于今天（%s）：抓到的永远是现在的内容，记到未来的日期会让首页卡住", today)
        return 2
    existing = store.load_day(root, day)
    if args.if_missing and existing is not None and existing.get("items"):
        return _fill_in(root, config, day, today, existing, args.no_llm)
    ctx = _context(config, now)

    candidates, report = collect(config, ctx)
    if not any(entry["ok"] for entry in report):
        log.error("没有任何来源抓取成功，本次不生成内容。")
        return 2

    # 当天重跑时，把已经登出的内容并回来，保留之前写好的中文摘要（先按现在的规则复查一遍）
    previous = store.items_of(existing)
    editor.recheck(previous)
    pool = dedupe(candidates + previous, config["dedupe"]["title_similarity"])
    seen = store.published_ids(root, day, config["dedupe"]["remember_days"])
    pool = [item for item in pool if seen.isdisjoint([item.id, *item.merged_ids])]

    client = build_client(config, ctx.env) if config["llm"]["enabled"] and not args.no_llm else None
    if client is None:
        log.info("没有可用的大模型（未配置密钥或已关闭），只按规则选稿，标题保持原文")
    selected = _edit(pool, config, client, now, ctx.http)

    llm = _llm_label(selected, client, existing)
    payload = {
        "date": day.isoformat(),
        "generated_at": to_iso(now),
        "llm": llm,
        "candidates": len(pool),
        "sources": report,
        "items": [item.to_dict() for item in selected],
    }
    store.save_day(root, day, payload)
    log.info("%s：候选 %d 条，入选 %d 条", day, len(pool), len(selected))

    week = _kuaixun_due(root, config, today, client)
    if week:
        _kuaixun(root, config, week, client, ctx)

    # 补的是过去某一天时，后面几天的“上一期”链接也要跟着变，干脆全部重排
    warnings = publish(root, config, day) if day == today else publish_all(root, config)
    warnings += [f"{title} 已经连续 3 天抓取失败，请检查这个来源" for title in failing_sources(root, day, report)]
    if not selected:
        warnings.append("今天没有任何内容入选")
    if client and selected and llm is None:
        warnings.append("配置了大模型密钥，但这次一条中文标题和摘要都没写出来，请查看日志")
    for warning in warnings:
        log.warning(warning)
        if ctx.env.get("GITHUB_ACTIONS"):
            print(f"::warning::{warning}")
    step_summary(ctx.env, day, payload, warnings)
    return 0


def cmd_kuaixun(root: Path, config: dict[str, Any], args: argparse.Namespace) -> int:
    now = datetime.now(UTC)
    today = local_date(now, config["utc_offset_hours"])
    monday: date = args.week or kuaixun.last_week(today)
    if monday + timedelta(days=6) >= today:
        log.error("%s 还没过完，快讯要等这一周结束以后再生成", week_id(monday))
        return 2
    if not week_payloads(root, monday):
        log.error("%s 没有任何一天的日报数据，生成不了快讯", week_id(monday))
        return 2
    client = build_client(config, os.environ) if config["llm"]["enabled"] and not args.no_llm else None
    if client is None:
        log.info("没有可用的大模型（未配置密钥或已关闭），标题和正文用日报里已有的")
    _kuaixun(root, config, monday, client, _context(config, now), reuse=not args.rewrite)
    for warning in publish_indexes(root, config, store.list_days(root)):
        log.warning(warning)
    return 0


def cmd_render(root: Path, config: dict[str, Any], args: argparse.Namespace) -> int:
    for warning in publish_all(root, config):
        log.warning(warning)
    return 0


def _week(text: str) -> date:
    """2026-W42 → 那一周的周一。"""
    match = re.fullmatch(r"(\d{4})-W(\d{2})", text.strip())
    if not match:
        raise argparse.ArgumentTypeError("格式是 2026-W42")
    try:
        return date.fromisocalendar(int(match.group(1)), int(match.group(2)), 1)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"没有这一周：{text}") from exc


def cmd_check(root: Path, config: dict[str, Any], args: argparse.Namespace) -> int:
    unknown = [name for name in args.names if name.split(":")[0] not in SOURCES]
    if unknown:
        log.error("没有这些来源：%s。可用的有：%s", "、".join(unknown), "、".join(SOURCES))
        return 2
    now = datetime.now(UTC)
    items, report = collect(config, _context(config, now), only=args.names or list(SOURCES))
    apply_scores(items, now)
    for entry in report:
        state = f"{entry['count']} 条" if entry["ok"] else f"失败：{entry['error']}"
        print(f"\n== {entry['title']}（{entry['name']}）{state}，用时 {entry['seconds']} 秒")
        source = entry["name"].split(":")[0]
        mine = [i for i in items if i.source == source and (entry["name"] == source or i.via == entry["title"])]
        for item in sorted(mine, key=lambda i: i.score, reverse=True)[: args.top]:
            flag = "（相关性待大模型判断）" if item.extra.get("needs_review") else ""
            published = parse_time(item.published)
            when = f"{local_time(published, config['utc_offset_hours']):%m-%d %H:%M}" if published else "无发布时间"
            print(f"   {item.score:5.2f}  {when}  [{item.section}] {item.title[:70]}{flag}\n          {item.url}")
    return 0 if all(entry["ok"] for entry in report) else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m wta", description="每周科技收集 Agent")
    parser.add_argument("--root", type=Path, default=Path("."), help="数据和页面写到哪个目录（默认是当前目录）")
    parser.add_argument("--config", type=Path, help="配置文件（默认是 --root 目录下的 config.yaml）")
    parser.add_argument("-v", "--verbose", action="store_true", help="显示调试信息")
    commands = parser.add_subparsers(dest="command", required=True)

    run = commands.add_parser("run", help="抓取并生成当天日报和 README；上周的快讯还没有就顺带生成")
    run.add_argument(
        "--date",
        type=date.fromisoformat,
        help="把这次抓到的内容记到这个日期，格式 2026-10-11（调试用；抓到的是现在的内容，不能补抓历史）",
    )
    run.add_argument("--no-llm", action="store_true", help="不调用大模型，只按规则选稿")
    run.add_argument(
        "--if-missing",
        action="store_true",
        help="这一天已经有内容就不重新抓取，只补上还没写成的中文和上周的快讯（定时任务用）",
    )
    run.set_defaults(handler=cmd_run)

    issue = commands.add_parser("kuaixun", help="生成（或重新生成）某一周的快讯")
    issue.add_argument("--week", type=_week, help="哪一周，格式 2026-W42；不写就是上一周")
    issue.add_argument("--no-llm", action="store_true", help="不调用大模型，标题和正文用日报里已有的")
    issue.add_argument("--rewrite", action="store_true", help="大模型已经写好的也重新写（改了提示词以后用）")
    issue.set_defaults(handler=cmd_kuaixun)

    render = commands.add_parser("render", help="不抓取，用已有数据重新生成所有页面")
    render.set_defaults(handler=cmd_render)

    check = commands.add_parser("check", help="测试来源，打印条数、发布时间和样例")
    check.add_argument("names", nargs="*", help="来源名（如 hackernews）或单个订阅（如 rss:量子位）；不写就测试全部")
    check.add_argument("--top", type=int, default=5, help="每个来源显示几条样例")
    check.set_defaults(handler=cmd_check)

    args = parser.parse_args(argv)
    for stream in (sys.stdout, sys.stderr):  # Windows 终端默认不是 UTF-8，中文会乱码
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        stream=sys.stderr,
    )
    root = args.root.resolve()
    config = load_config(args.config or root / "config.yaml")
    return args.handler(root, config, args)
