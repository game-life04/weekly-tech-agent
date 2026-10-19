"""每周快讯：参照《CCF开源快讯》的体例，把上一周的内容整理成一期“5 分钟速读”。

每周一生成上周一到周日的一期，栏目和顺序见 models.KX_SECTIONS：
- 俱乐部动态：俱乐部 GitHub 组织的周统计、最活跃的仓库、新仓库和新版本，由程序根据接口数据写成（club.py）；
- 政策动向：中国政府网上和人工智能、开源、软件有关的条目（policy.py）；
- 国内动态、海外动态、开源项目、学术前沿、产业纵横：从这一周每天的日报里挑。大模型负责分栏，
  按“主体+动作+对象”写标题，写一两句正文，并指出讲同一件事的重复条目；
- 活动预告：接下来几周截稿的 CCF 推荐会议（deadlines.py）。

和日报一样，大模型只写栏目、标题和正文，日期、链接、来源和统计数字都由程序填写；
写出了资料里没有的英文名称或数字、或者没写成中文的，就不用，退回日报里已经核对过的中文标题和摘要。
结果存进 data/weekly/<周>.json，页面只凭这份数据生成，重新排版不需要网络和大模型。
"""

from __future__ import annotations

import logging
import re
from collections.abc import Mapping
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

from . import club, deadlines, excerpt, policy, store
from .dates import local_date, local_time, parse_time, to_iso, week_id, week_range
from .editor import CJK, DATA_NOTE, BatchRun, batches, evidence_of, plain, ungrounded
from .http import Http
from .llm import LLMClient
from .models import KX_SECTIONS, Item
from .publish import load_week_note, week_payloads
from .sources.base import Context
from .textutil import KeywordMatcher, clean_text

log = logging.getLogger(__name__)

BATCH = 12
HEADLINE_LIMIT, BODY_LIMIT = 36, 130  # 提示词里要的是 28 字和 90 字，留一点余地；超出的不用
EVIDENCE_CHARS = 600
MAX_TRIES = 3  # 大模型没写完的那几条，最多再补几次
WRITABLE = ("domestic", "overseas", "opensource", "papers", "industry")  # 大模型可以把日报内容放进这些栏目
_DATE_PREFIX = re.compile(r"^(?:\d{4}年)?\d{1,2}月\d{1,2}日(?:[至到—–-]\d{1,2}日)?(?:消息)?[，,、。.\s]*")

PROMPT = f"""你是《每周科技快讯》的编辑，参照《CCF开源快讯》的体例，为关注人工智能和开源的中国大学生整理上周要闻。
{DATA_NOTE}

每一条有 title（原标题）、title_zh（中文标题，可能没有）、text（资料）、source（来源）和 section（日报里的栏目）。
对每一条：
1. cat：放进哪个栏目，只能是下面之一：
   domestic 国内动态：中国的公司、高校和机构的发布与动作，包括它们开源的模型和项目；
   overseas 海外动态：海外的公司、高校和机构的发布与动作，包括它们开源的模型和项目；
   opensource 开源项目：社区的开源项目、工具和版本更新，不是某家公司或机构的新闻；
   papers 学术前沿：论文和研究成果；
   industry 产业纵横：行业会议、标准、投融资、市场和产业数据；
   policy 政策动向：只用于 source 是“中国政府网”的条目；
   skip：和人工智能、开源关系不大，或者资料太少、说不清是什么。
2. headline：中文标题，不超过 28 个字，写成“主体+动作+对象”，
   例如“腾讯混元开源记忆框架Hy Memory 2.0”“英伟达发布Nemotron 3.5 Super VL模型”。
   主体必须是资料里写明的公司、机构或团队；谁发布、谁使用要和资料一致：“A 用了 B 的模型”不能写成“A 发布 B”。
   资料没写清是谁做的，就用项目或产品的名字开头。
3. body：一到两句中文，不超过 90 个字，接着标题说清楚做了什么、有什么特点。不要写日期，程序会在前面加上日期。
   只能依据 title、title_zh 和 text；资料里没有的数字、结论、评价、公司名和模型名一律不要写；
   名称、数字和单位照抄原文的写法。
4. same：如果这一条和前面某一条（i 更小）讲的是同一件事，填那一条的 i；不是就不写这个字段。

只输出一个 JSON 对象，格式为
{{"items": [{{"i": 0, "cat": "domestic", "headline": "...", "body": "..."}}]}}。
每条输入都要有对应的输出，i 与输入一致。不要输出其他任何文字。"""


def last_week(today: date) -> date:
    """today 所在这一周的上一周的周一。"""
    return week_range(today)[0] - timedelta(days=7)


def due(root: Path, today: date, llm_ready: bool) -> date | None:
    """上一周的快讯需不需要生成（或重新生成），需要就返回那一周的周一。

    - 还没有：这一周有日报就生成；
    - 大模型有几条没写成（服务过载、额度用完）：有大模型可用时再补，最多补 MAX_TRIES 次；
    - 周一当天，俱乐部的统计还没覆盖到周日（仪表盘每天更新一次，凌晨时还停在前一天）：重新取一次。
    重新生成时，大模型已经写好的条目直接沿用，不会重写。
    """
    monday = last_week(today)
    note = load_week_note(root, week_id(monday)).get("kuaixun")
    if not isinstance(note, dict):
        return monday if week_payloads(root, monday) else None
    if llm_ready and note.get("pending") and note.get("tries", 0) < MAX_TRIES:
        return monday
    sunday = monday + timedelta(days=6)
    covered = str((note.get("club_period") or {}).get("end", ""))
    if today == sunday + timedelta(days=1) and covered < sunday.isoformat():
        return monday
    return None


def pool_of(payloads: dict[date, dict[str, Any]]) -> list[Item]:
    """这一周每天入选的内容。同一条只留第一次出现的那天（记在 extra["kx_day"]）。"""
    seen: set[str] = set()
    pool: list[Item] = []
    for day in sorted(payloads):
        for item in store.items_of(payloads[day]):
            if item.id in seen:
                continue
            seen.add(item.id)
            item.extra["kx_day"] = day.isoformat()
            pool.append(item)
    return pool


def shortlist(pool: list[Item], limits: Mapping[str, int]) -> list[Item]:
    """每个日报栏目按综合分取前几条，交给大模型分栏和改写。"""
    picked: list[Item] = []
    for section, count in limits.items():
        rows = sorted((item for item in pool if item.section == section), key=lambda item: item.score, reverse=True)
        picked += rows[: int(count)]
    return picked


def guess(item: Item) -> str:
    """没有大模型时的分栏：政策、论文、开源项目照来源分；其余看原标题是不是中文。"""
    if item.source == policy.NAME:
        return "policy"
    if item.section in ("papers", "opensource"):
        return item.section
    return "domestic" if CJK.search(item.title) else "overseas"


def _facts(item: Item) -> str:
    return f"{item.title} {item.title_zh} {item.summary_zh} {item.via} {evidence_of(item)}"


def _checked(name: str, value: object, limit: int, item: Item) -> str:
    text = plain(value, 0)
    if name == "正文":
        text = _DATE_PREFIX.sub("", text).strip()
    if not text:
        return ""
    problem = ""
    if len(text) > limit:
        problem = "太长"
    elif not CJK.search(text):
        problem = "没有写成中文"
    elif invented := ungrounded(text, _facts(item)):
        problem = "出现了资料里没有的 " + "、".join(invented)
    if problem:
        log.info("快讯不采用模型写的%s（%s）：%s", name, problem, item.title[:60])
        return ""
    return text


class _Writer:
    """交给 BatchRun 的两个函数：生成每一批的输入，核对并记下模型的输出。

    一批里的条目按顺序编号；same 指向同一批里更靠前的那一条，所以要记住当前这一批。
    """

    def __init__(self) -> None:
        self.batch: list[Item] = []

    def row(self, index: int, item: Item) -> dict[str, Any]:
        if index == 0:
            self.batch = []
        self.batch.append(item)
        row: dict[str, Any] = {"i": index, "section": item.section, "source": item.via, "title": item.title[:200]}
        if item.title_zh:
            row["title_zh"] = item.title_zh
        text = clean_text(f"{item.summary_zh} {evidence_of(item)}", EVIDENCE_CHARS)
        if text:
            row["text"] = text
        return row

    def apply(self, item: Item, row: dict[str, Any]) -> bool:
        cat = row.get("cat")
        allowed = ("policy", "skip") if item.source == policy.NAME else (*WRITABLE, "skip")
        written = {
            "cat": cat if cat in allowed else "",
            "headline": _checked("标题", row.get("headline"), HEADLINE_LIMIT, item),
            "body": _checked("正文", row.get("body"), BODY_LIMIT, item),
        }
        position = next((i for i, other in enumerate(self.batch) if other is item), -1)
        same = row.get("same")
        if isinstance(same, int) and not isinstance(same, bool) and 0 <= same < position:
            written["same"] = self.batch[same].id
        item.extra["kx"] = written
        return bool(written["headline"] or written["body"])


def write(items: list[Item], client: LLMClient) -> int:
    """让大模型给这些条目分栏、写标题和正文，结果记在 extra["kx"]；返回写成的条数。"""
    todo = [item for item in items if "kx" not in item.extra and not item.extra.get("filtered")]
    if not todo:
        return 0
    writer = _Writer()
    run = BatchRun(client, PROMPT, writer.row, writer.apply, 260, reserve=0, depth=8)
    run.process(batches(todo, BATCH))
    log.info("大模型写快讯：%d/%d 条", run.done, len(todo))
    return run.done


def _when(item: Item, monday: date, sunday: date, offset: float) -> tuple[str, str]:
    """（日期，正文开头的日期写法）。发布日期在这一周里就写发布日期，否则写日报登出那天的“某日消息”。"""
    moment = parse_time(item.published)
    day = local_date(moment, offset) if moment else None
    if day and monday <= day <= sunday:
        return day.isoformat(), f"{day.month}月{day.day}日"
    seen = date.fromisoformat(item.extra.get("kx_day") or monday.isoformat())
    return seen.isoformat(), f"{seen.month}月{seen.day}日消息"


def entry_of(item: Item, cat: str, monday: date, sunday: date, offset: float) -> dict[str, Any] | None:
    """一条快讯。大模型没写成的部分用日报里的中文标题和摘要；连正文都没有的不登。"""
    written = item.extra.get("kx") or {}
    headline = written.get("headline") or item.title_zh or clean_text(item.title, 80)
    body = written.get("body") or item.summary_zh or clean_text(item.summary, 120)
    if not body and item.source == policy.NAME:
        body = f"据{policy.VIA}消息：{clean_text(item.title, 100)}"
    if not body:
        return None
    if body[-1] not in "。！？.!?…”）)":
        body += "。"
    day, when = _when(item, monday, sunday, offset)
    return {
        "cat": cat,
        "headline": headline,
        "when": when,
        "date": day,
        "body": body,
        "url": item.url,
        "via": item.via or item.source,
        "id": item.id,
        "ai": bool(written.get("headline") or written.get("body") or item.title_zh or item.summary_zh),
    }


def assemble(
    candidates: list[Item], caps: Mapping[str, int], monday: date, sunday: date, offset: float
) -> dict[str, list[dict[str, Any]]]:
    """按栏目挑出要登的条目：栏目内按综合分取前几条，再按日期排。重复的（same）不登。"""
    chosen: dict[str, list[dict[str, Any]]] = {name: [] for name, _ in KX_SECTIONS}
    for item in sorted(candidates, key=lambda item: item.score, reverse=True):
        written = item.extra.get("kx") or {}
        cat = written.get("cat") or guess(item)
        if cat not in chosen or cat in ("club", "events") or written.get("same"):
            continue  # skip、重复的，以及大模型不该填的栏目
        if len(chosen[cat]) >= int(caps.get(cat, 0)):
            continue
        entry = entry_of(item, cat, monday, sunday, offset)
        if entry:
            chosen[cat].append(entry)
    for rows in chosen.values():
        rows.sort(key=lambda entry: entry["date"])
    return chosen


def _attempt(report: list[dict[str, Any]], name: str, title: str, job) -> Any:
    """跑一个外部数据源，成败记进报告；失败返回 None。"""
    try:
        result = job()
    except Exception as exc:  # 任何一个数据源出问题都不能让快讯出不来
        log.warning("快讯的%s取不到：%s", title, exc)
        report.append({"name": name, "title": title, "ok": False, "error": clean_text(str(exc), 200)})
        return None
    report.append({"name": name, "title": title, "ok": True, "error": ""})
    return result


def build(
    root: Path,
    config: dict[str, Any],
    monday: date,
    *,
    client: LLMClient | None,
    http: Http,
    env: Mapping[str, str],
    now: datetime,
    reuse: bool = True,
) -> dict[str, Any]:
    """生成 monday 这一周的快讯（返回要存进周记录的数据，不写文件）。

    reuse 为真时，上一次大模型已经写好的条目直接沿用，只补没写成的。
    """
    settings, offset = config["kuaixun"], config["utc_offset_hours"]
    sunday = monday + timedelta(days=6)
    week = week_id(monday)
    previous = load_week_note(root, week).get("kuaixun") or {}
    kept = [entry for entry in previous.get("entries") or [] if isinstance(entry, dict)]
    report: list[dict[str, Any]] = []
    ctx = Context(http=http, now=now, keywords=KeywordMatcher(config["keywords"]), env=env)

    fetched = _attempt(report, "club", club.VIA, lambda: club.fetch(ctx, settings["club"], monday, sunday, offset))
    club_entries, club_period = fetched or ([e for e in kept if e.get("cat") == "club"], previous.get("club_period"))
    policies = _attempt(report, "policy", policy.VIA, lambda: policy.fetch(http, monday, sunday, settings["policy"]))
    beijing = local_time(now, offset).replace(tzinfo=None)
    events = _attempt(report, "events", deadlines.VIA, lambda: deadlines.fetch(http, beijing, settings["events"]))
    if events is None:
        events = [entry for entry in kept if entry.get("cat") == "events"]

    payloads = week_payloads(root, monday)
    candidates = shortlist(pool_of(payloads), settings["candidates"]) + (policies or [])
    cache = (previous.get("written") or {}) if reuse else {}
    for item in candidates:  # 上次已经写好的直接沿用
        if isinstance(cache.get(item.id), dict):
            item.extra["kx"] = cache[item.id]
    waiting = [item for item in candidates if "kx" not in item.extra]
    attempted = client is not None and not client.exhausted and bool(waiting)  # 真的要请求时才算补了一次
    if client is not None and attempted:
        try:
            excerpt.enrich([item for item in candidates if item.source == policy.NAME], http)
            write(candidates, client)
        except Exception:
            log.exception("大模型写快讯出错，用日报里的中文标题和摘要")

    caps = settings["caps"]
    chosen = assemble(candidates, caps, monday, sunday, offset)
    if policies is None:  # 政策列表这次取不到：沿用上次的
        chosen["policy"] = [entry for entry in kept if entry.get("cat") == "policy"]
    chosen["club"] = club_entries[: int(caps.get("club", 0))]
    chosen["events"] = events[: int(caps.get("events", 0))]
    entries = [entry for name, _ in KX_SECTIONS for entry in chosen[name]]

    models = [*previous.get("models", [])]
    models += [str((payload.get("llm") or {}).get("model") or "") for payload in payloads.values()]
    models += [provider.model for provider in client.answered] if client else []
    return {
        "week": week,
        "start": monday.isoformat(),
        "end": sunday.isoformat(),
        "generated_at": to_iso(now),
        "models": list(dict.fromkeys(name for name in models if name)),
        "tries": int(previous.get("tries", 0)) + attempted,
        "pending": sum("kx" not in item.extra and not item.extra.get("filtered") for item in candidates),
        "club_period": club_period,
        "sources": report,
        "entries": entries,
        "written": {item.id: item.extra["kx"] for item in candidates if "kx" in item.extra},
    }
