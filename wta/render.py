"""把数据排成 Markdown：日报、周报、README 里的“最新一期”和往期目录。

GitHub 会直接渲染仓库里的 Markdown，所以这些文件就是读者看到的页面。
这里的函数只生成文字、不读写文件，方便测试；写文件在 publish.py 里。
"""

from __future__ import annotations

import posixpath
import re
from datetime import date, timedelta
from typing import Any
from urllib.parse import quote

from . import REPO_URL
from .dates import local_time, parse_time, week_id, weekday_name
from .models import SECTIONS, Item
from .rank import select
from .store import items_of
from .textutil import clean_text

LATEST_START = "<!-- wta:latest:start -->"
LATEST_END = "<!-- wta:latest:end -->"

_MD_SPECIAL = re.compile(r"([\\`*_\[\]|~])")
_URL_UNSAFE = re.compile(r"[\s()<>\"\\|`\[\]]")

# 指标的内部名 → 显示写法；按这里的顺序展示
_METRIC_LABELS = (
    ("stars_today", "今日 +{} ★"),
    ("stars_week", "本周 +{} ★"),
    ("stars", "{} ★"),
    ("points", "{} 分"),
    ("comments", "{} 评论"),
    ("upvotes", "{} 赞"),
    ("likes", "{} 喜欢"),
    ("downloads", "{} 下载"),
)


def daily_path(day: date) -> str:
    return f"daily/{day:%Y}/{day.isoformat()}.md"


def weekly_path(week: str) -> str:
    return f"weekly/{week}.md"


def _relative(from_dir: str, target: str) -> str:
    return posixpath.relpath(target, start=from_dir or ".")


def md_escape(text: object, limit: int = 0) -> str:
    """把外部来的文字变成安全的纯文本：去掉标签，转义会被当成排版符号的字符。"""
    out = clean_text(text, limit)
    out = out.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    out = _MD_SPECIAL.sub(r"\\\1", out)
    # GitHub 还会主动渲染两样东西：$…$ 数学公式，以及裸网址和邮箱的自动链接。
    # 反斜杠挡不住公式，官方给的办法是把 $ 包进 <span>；把 "://"、"www."、"@" 拆开就不会变成链接。
    out = out.replace("$", "<span>$</span>")
    return out.replace("://", ":\\//").replace("www.", "www\\.").replace("@", "\\@")


def md_url(url: str) -> str:
    """只接受 http/https 链接，并把会打断 Markdown 链接写法的字符做百分号编码。"""
    url = (url or "").strip()
    if not re.match(r"https?://", url, re.IGNORECASE):
        return ""
    return _URL_UNSAFE.sub(lambda m: quote(m.group(), safe=""), url)


def fmt_num(value: float) -> str:
    """532 → 532，12345 → 12.3k，1234567 → 1.2M。"""
    number = int(min(max(value, 0), 1e12))  # 限个范围：来源给出离谱的大数时不至于算溢出
    for size, suffix in ((1_000_000, "M"), (1_000, "k")):
        if number >= size:
            return f"{number / size:.1f}".removesuffix(".0") + suffix
    return str(number)


def _meta(item: Item) -> list[str]:
    """标题下面那一行小字：来源、指标、其他出处、标签、原标题、相关链接。"""
    parts = [md_escape(item.via or item.source)]
    for name, label in _METRIC_LABELS:
        value = item.metrics.get(name, 0)
        if value and value > 0:
            parts.append(label.format(fmt_num(value)))
    if item.also_in:
        parts.append("同时见于 " + "、".join(md_escape(v) for v in item.also_in))
    if item.tags:
        parts.append(" ".join(f"#{md_escape(tag, 12)}" for tag in item.tags[:3]))
    if item.title_zh and clean_text(item.title_zh) != clean_text(item.title):
        parts.append("原题：" + md_escape(item.title, 120))
    links = [["讨论", item.extra.get("discussion", "")], *(item.extra.get("links") or [])]
    for link in links:
        if isinstance(link, (list, tuple)) and len(link) == 2 and md_url(str(link[1])):
            parts.append(f"[{md_escape(link[0], 20)}]({md_url(str(link[1]))})")
    return parts


def render_item(number: int, item: Item) -> str:
    """一条内容占一行（用 <br> 换行），这样外部文字不会出现在行首被当成标题或列表。"""
    title = md_escape(item.title_zh or item.title, 120)
    url = md_url(item.url)
    parts = [f"**{number}. [{title}]({url})**" if url else f"**{number}. {title}**"]
    summary = md_escape(item.summary_zh or item.summary, 200)
    if summary:
        parts.append(summary)
    parts.append(f"<sub>{' · '.join(_meta(item))}</sub>")
    return "<br>".join(parts)


def render_sections(items: list[Item], config: dict[str, Any], level: int = 2) -> str:
    blocks: list[str] = []
    for section in SECTIONS:
        info = config["sections"][section]
        blocks.append(f"{'#' * level} {info['emoji']} {info['title']}")
        rows = [item for item in items if item.section == section]
        if rows:
            blocks.extend(render_item(number, item) for number, item in enumerate(rows, 1))
        else:
            blocks.append("这个栏目暂时没有新内容。")
    return "\n\n".join(blocks)


def _counts(items: list[Item], config: dict[str, Any]) -> str:
    return " · ".join(
        f"{config['sections'][s]['emoji']} {config['sections'][s]['title']} {sum(i.section == s for i in items)}"
        for s in SECTIONS
    )


def _zone_name(config: dict[str, Any]) -> str:
    offset = config["utc_offset_hours"]
    return "北京时间" if offset == 8 else f"UTC{offset:+g}"


def _has_ai_text(items: list[Item]) -> bool:
    return any(item.title_zh or item.summary_zh for item in items)


def _models(payloads: list[dict[str, Any]]) -> list[str]:
    """这些天里用过的大模型名字，去重、保持先后顺序。"""
    names = [str((payload.get("llm") or {}).get("model") or "") for payload in payloads]
    return list(dict.fromkeys(name for name in names if name))


def _footer(payload: dict[str, Any], config: dict[str, Any], ai_text: bool, models: list[str]) -> str:
    """页脚。ai_text 表示这一页里确实有大模型写的文字：有就一定标注，不看数据里记没记模型名。"""
    notes: list[str] = []
    if ai_text:
        named = f"（{md_escape('、'.join(models))}）" if models else ""
        notes.append(f"中文标题和摘要由 AI 生成{named}，可能有误，请以原文为准。")
    sources = payload.get("sources", [])
    groups: dict[str, list[dict[str, Any]]] = {}
    for source in sources:
        if source.get("ok"):
            groups.setdefault(source.get("group") or source["title"], []).append(source)
    if groups:  # 同一类来源（例如几十个 RSS 订阅）合成一项，避免页脚太长
        described = []
        for group, members in groups.items():
            total = sum(m["count"] for m in members)
            described.append(f"{md_escape(group)} {total}" + (f"（{len(members)} 个源）" if len(members) > 1 else ""))
        notes.append("本期候选来自：" + "、".join(described) + "。")
    failed = [s for s in sources if not s.get("ok")]
    if failed:
        notes.append("本次未取到：" + "、".join(md_escape(s["title"]) for s in failed) + "。")
    generated = parse_time(payload.get("generated_at"))
    when = ""
    if generated:
        when = f"于 {local_time(generated, config['utc_offset_hours']):%Y-%m-%d %H:%M}（{_zone_name(config)}）"
    notes.append(f"由[每周科技收集 Agent]({REPO_URL}){when}自动生成。")
    return "<sub>" + " ".join(notes) + "</sub>"


def render_daily(day: date, payload: dict[str, Any], config: dict[str, Any], previous: date | None) -> str:
    items = items_of(payload)
    here = posixpath.dirname(daily_path(day))
    nav = [f"[本周周报]({_relative(here, weekly_path(week_id(day)))})"]
    if previous:
        nav.append(f"[上一期]({_relative(here, daily_path(previous))})")
    nav.append(f"[往期目录]({_relative(here, 'daily/README.md')})")
    blocks = [
        f"# AI 日报 · {day.isoformat()}（{weekday_name(day)}）",
        f"> 今日收录 **{len(items)}** 条：{_counts(items, config)}<br>\n> " + " · ".join(nav),
        render_sections(items, config),
        "---",
        _footer(payload, config, _has_ai_text(items), _models([payload])),
    ]
    return "\n\n".join(blocks) + "\n"


def weekly_pick(payloads: dict[date, dict[str, Any]], config: dict[str, Any]) -> tuple[list[Item], int]:
    """从一周的日报里按综合分挑出周报内容。返回（入选内容，本周收录总数）。"""
    pool = [item for day in sorted(payloads) for item in items_of(payloads[day])]
    quotas = {s: config["sections"][s]["weekly"] for s in SECTIONS}
    caps = {name: cap * 2 for name, cap in config["select"]["caps"].items()}  # 一周的量，上限放宽一倍
    return select(pool, quotas, config["select"]["per_source_cap"] * 2, caps), len(pool)


def render_weekly(
    monday: date, payloads: dict[date, dict[str, Any]], config: dict[str, Any], today: date, overview: str = ""
) -> str:
    sunday = monday + timedelta(days=6)
    year, week, _ = monday.isocalendar()
    picked, total = weekly_pick(payloads, config)
    days = " · ".join(f"[{weekday_name(d)} {d:%m-%d}]({_relative('weekly', daily_path(d))})" for d in sorted(payloads))
    state = "本周内容已收齐。" if today >= sunday else "本周还没结束，内容每天更新。"
    blocks = [
        f"# AI 周报 · {year} 年第 {week} 周（{monday:%m-%d} ~ {sunday:%m-%d}）",
        f"> 本周日报共收录 **{total}** 条，这里按综合分精选 **{len(picked)}** 条。{state}<br>\n"
        f"> 每日日报：{days}<br>\n> [往期周报](README.md)",
    ]
    if overview.strip():
        blocks += ["## 本周看点", md_escape(overview, 1200)]
    blocks.append(render_sections(picked, config))
    ordered = [payloads[day] for day in sorted(payloads)]
    generated = {"generated_at": ordered[-1].get("generated_at")} if ordered else {}
    # 周报的内容来自一周里的每一天，AI 标注也按整周算，不能只看最后一天
    ai_text = bool(overview.strip()) or _has_ai_text(picked)
    blocks += ["---", _footer(generated, config, ai_text, _models(ordered))]
    return "\n\n".join(blocks) + "\n"


def render_latest_block(day: date, payload: dict[str, Any], config: dict[str, Any]) -> str:
    """README 里“最新一期”这一段（含首尾标记）。"""
    items = items_of(payload)
    nav = (
        f"[本周周报]({weekly_path(week_id(day))}) · [往期日报](daily/README.md) · [往期周报](weekly/README.md)"
        f" · [单独打开这一期]({daily_path(day)})"
    )
    blocks = [
        LATEST_START,
        f"## 最新一期 · {day.isoformat()}（{weekday_name(day)}）",
        f"> 收录 **{len(items)}** 条：{_counts(items, config)}<br>\n> {nav}",
        render_sections(items, config, level=3),
        _footer(payload, config, _has_ai_text(items), _models([payload])),
        LATEST_END,
    ]
    return "\n\n".join(blocks)


def replace_latest_block(readme: str, block: str) -> str:
    """把 README 里两个标记之间的内容换成新的；两个标记都没有时加在文末。

    标记缺一个、重复或顺序颠倒时抛 ValueError：这时候猜着改只会越改越乱
    （把后面的说明删掉，或者每天多追加一份）。
    """
    starts, ends = readme.count(LATEST_START), readme.count(LATEST_END)
    if starts == 0 and ends == 0:
        return readme.rstrip("\n") + "\n\n" + block + "\n"
    start, end = readme.find(LATEST_START), readme.find(LATEST_END)
    if starts != 1 or ends != 1 or end < start:
        raise ValueError(f"wta:latest 标记损坏（开始标记 {starts} 个、结束标记 {ends} 个），请手动修好")
    return readme[:start] + block + readme[end + len(LATEST_END) :]


def render_daily_index(days: list[tuple[date, int]]) -> str:
    """daily/README.md：按月份倒序列出所有日报。days 是（日期，条数）。"""
    lines = ["# 往期日报", "", "[返回首页](../README.md) · [往期周报](../weekly/README.md)"]
    month = None
    for day, count in sorted(days, reverse=True):
        if (day.year, day.month) != month:
            month = (day.year, day.month)
            lines += ["", f"## {day.year} 年 {day.month} 月", ""]
        lines.append(f"- [{day:%m-%d}（{weekday_name(day)}）]({day:%Y}/{day.isoformat()}.md) · {count} 条")
    return "\n".join(lines) + "\n"


def render_weekly_index(weeks: list[tuple[date, int]]) -> str:
    """weekly/README.md：倒序列出所有周报。weeks 是（周一日期，本周收录条数）。"""
    lines = ["# 往期周报", "", "[返回首页](../README.md) · [往期日报](../daily/README.md)", ""]
    for monday, count in sorted(weeks, reverse=True):
        year, week, _ = monday.isocalendar()
        sunday = monday + timedelta(days=6)
        lines.append(
            f"- [{year} 年第 {week} 周（{monday:%m-%d} ~ {sunday:%m-%d}）]({week_id(monday)}.md) · 收录 {count} 条"
        )
    return "\n".join(lines) + "\n"
