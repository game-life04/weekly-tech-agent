"""把数据排成页面：日报、每周快讯（Markdown 和公众号排版用的 HTML）、README 里的“最新一期”和往期目录。

GitHub 会直接渲染仓库里的 Markdown，所以这些文件就是读者看到的页面。
这里的函数只生成文字、不读写文件，方便测试；写文件在 publish.py 里。
"""

from __future__ import annotations

import html
import posixpath
import re
from datetime import date, timedelta
from typing import Any
from urllib.parse import quote

from . import REPO_URL
from .dates import date_span, local_time, parse_time, weekday_name
from .models import KX_SECTIONS, SECTIONS, Item
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


def weekly_html_path(week: str) -> str:
    return f"weekly/{week}.html"


def group_text_path(kx: dict[str, Any]) -> str:
    """每日快讯的群消息文字版。"""
    day = date.fromisoformat(kx["day"])
    return f"daily/{day:%Y}/{day.isoformat()}-group.txt"


def kuaixun_paths(kx: dict[str, Any]) -> tuple[str, str]:
    """一期快讯的两个文件（相对仓库根目录）：Markdown 页面和公众号排版版。"""
    if kx.get("kind") == "daily":
        day = date.fromisoformat(kx["day"])
        base = f"daily/{day:%Y}/{day.isoformat()}-kuaixun"
        return base + ".md", base + ".html"
    return weekly_path(kx["week"]), weekly_html_path(kx["week"])


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
    nav = [f"[每周快讯]({_relative(here, 'weekly/README.md')})"]
    if isinstance(payload.get("kuaixun"), dict):
        nav.insert(0, f"[今日快讯]({_relative(here, kuaixun_paths(payload['kuaixun'])[0])})")
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


def render_latest_block(
    day: date | None, payload: dict[str, Any], config: dict[str, Any], kx: dict[str, Any] | None = None
) -> str:
    """README 里“最新一期”这一段（含首尾标记）：最新一期每日快讯（没有的话是日报），加上最新一期每周快讯的速览。"""
    blocks = [LATEST_START]
    daily = payload.get("kuaixun") if day is not None else None
    if isinstance(daily, dict):
        blocks += _kx_daily_readme(daily, config, kx)
    if kx:
        blocks += _kx_readme(kx)
    if day is not None and not isinstance(daily, dict):
        items = items_of(payload)
        nav = f"[往期日报](daily/README.md) · [每周快讯](weekly/README.md) · [单独打开这一期]({daily_path(day)})"
        blocks += [
            f"## 最新日报 · {day.isoformat()}（{weekday_name(day)}）",
            f"> 收录 **{len(items)}** 条：{_counts(items, config)}<br>\n> {nav}",
            render_sections(items, config, level=3),
            _footer(payload, config, _has_ai_text(items), _models([payload])),
        ]
    blocks.append(LATEST_END)
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


def render_daily_index(days: list[tuple]) -> str:
    """daily/README.md：按月份倒序列出所有日报。days 是（日期，条数），有每日快讯的再加一项 True。"""
    lines = ["# 往期日报", "", "[返回首页](../README.md) · [每周快讯](../weekly/README.md)"]
    month = None
    for day, count, *rest in sorted(days, reverse=True):
        if (day.year, day.month) != month:
            month = (day.year, day.month)
            lines += ["", f"## {day.year} 年 {day.month} 月", ""]
        line = f"- [{day:%m-%d}（{weekday_name(day)}）]({day:%Y}/{day.isoformat()}.md) · {count} 条"
        if rest and rest[0]:
            base = f"{day:%Y}/{day.isoformat()}-kuaixun"
            line += f" · [每日快讯]({base}.md) · [公众号排版版]({base}.html)"
        lines.append(line)
    return "\n".join(lines) + "\n"


def render_weekly_index(issues: list[dict[str, Any]]) -> str:
    """weekly/README.md：倒序列出所有快讯。issues 是每一期快讯的数据。"""
    lines = ["# 每周快讯", "", "[返回首页](../README.md) · [往期日报](../daily/README.md)", ""]
    for kx in sorted(issues, key=lambda kx: kx["start"], reverse=True):
        year, week, _ = date.fromisoformat(kx["start"]).isocalendar()
        lines.append(
            f"- [{year} 年第 {week} 周 · {kx_range(kx)}]({kx['week']}.md) · [公众号排版版]({kx['week']}.html)"
            f" · {len(_kx_entries(kx))} 条"
        )
    if not issues:
        lines.append("还没有快讯：每周一生成上一周的一期。")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# 每周快讯和每日快讯（kx["kind"] 是 weekly 或 daily）

_KX_SCOPE = "俱乐部动态、政策动向、国内外动态、开源项目、学术前沿和产业纵横，以及近期活动和会议截稿。"


def _daily(kx: dict[str, Any]) -> bool:
    return kx.get("kind") == "daily"


def kx_title(kx: dict[str, Any]) -> str:
    return ("每日科技快讯" if _daily(kx) else "每周科技快讯") + f" · {kx_range(kx)}"


def _kx_intro(kx: dict[str, Any]) -> str:
    return f"{'3' if _daily(kx) else '5'} 分钟速读 AI 与开源大事件：{_KX_SCOPE}"


def kx_range(kx: dict[str, Any]) -> str:
    """每周：10.12–10.18；每日：10.20。"""
    start, end = date.fromisoformat(kx["start"]), date.fromisoformat(kx["end"])
    return f"{end:%m.%d}" if start == end else f"{start:%m.%d}–{end:%m.%d}"


def _kx_entries(kx: dict[str, Any]) -> list[dict[str, Any]]:
    return [entry for entry in kx.get("entries") or [] if isinstance(entry, dict)]


def _kx_groups(kx: dict[str, Any]) -> list[tuple[str, str, list[dict[str, Any]]]]:
    """（栏目内部名，栏目名，条目）；没有内容的栏目不出现。"""
    entries = _kx_entries(kx)
    groups = [(name, title, [entry for entry in entries if entry.get("cat") == name]) for name, title in KX_SECTIONS]
    return [group for group in groups if group[2]]


def _kx_parts(kx: dict[str, Any]) -> list[tuple[str, list[tuple[str, str, list[dict[str, Any]]]]]]:
    """正文分两部分：上周快讯（每日快讯叫今日快讯，下面分栏目）和活动预告。"""
    groups = _kx_groups(kx)
    parts = [
        ("今日快讯" if _daily(kx) else "上周快讯", [g for g in groups if g[0] != "events"]),
        ("活动预告", [g for g in groups if g[0] == "events"]),
    ]
    return [part for part in parts if part[1]]


def _kx_brings(kx: dict[str, Any]) -> list[str]:
    """“本期为您带来”的几项。"""
    events = any(entry.get("cat") == "events" for entry in _kx_entries(kx))
    return [f"{kx_range(kx)} 快讯"] + (["近期活动预告"] if events else [])


def _kx_notes(kx: dict[str, Any], config: dict[str, Any]) -> list[tuple[str, str, str, str]]:
    """页脚的几句说明，每句是（链接前的文字，链接文字，链接，链接后的文字）；没有链接的中间两项为空。"""
    entries = _kx_entries(kx)
    notes: list[tuple[str, str, str, str]] = []
    if any(entry.get("ai") for entry in entries):
        models = "、".join(kx.get("models") or [])
        notes.append(
            (f"标题和正文由 AI 根据原文整理{f'（{models}）' if models else ''}，可能有误，请以原文为准。", "", "", "")
        )
    period = kx.get("club_period") or {}
    if any(entry.get("cat") == "club" for entry in entries) and period.get("start") and period.get("end"):
        when = date_span(date.fromisoformat(period["start"]), date.fromisoformat(period["end"]))
        dashboard = config["kuaixun"]["club"]["dashboard"].rstrip("/") + "/"
        notes.append((f"俱乐部动态的统计日期为{when}，数据来自", "俱乐部开源仪表盘", dashboard, "。"))
    if any(entry.get("cat") == "events" for entry in entries):
        notes.append(("会议截稿时间来自", "CCFDDL", "https://ccfddl.com/", "，已换算成北京时间，请以会议官网为准。"))
    failed = [str(source.get("title")) for source in kx.get("sources") or [] if not source.get("ok")]
    if failed:
        notes.append((f"本期未取到：{'、'.join(failed)}。", "", "", ""))
    notes.append(("有新闻线索欢迎", "提交 Issue", f"{REPO_URL}/issues", "。"))
    generated = parse_time(kx.get("generated_at"))
    when = ""
    if generated:
        when = f"于 {local_time(generated, config['utc_offset_hours']):%Y-%m-%d %H:%M}（{_zone_name(config)}）"
    notes.append(("本期由", "每周科技收集 Agent", REPO_URL, f"{when}自动生成。"))
    return notes


def _kx_entry_md(entry: dict[str, Any]) -> str:
    url, via = md_url(str(entry.get("url") or "")), md_escape(entry.get("via") or "原文", 30)
    source = f"[{via}]({url})" if url else via
    text = f"{md_escape(entry.get('when'), 30)}，{md_escape(entry.get('body'), 360)}"
    return f"**{md_escape(entry.get('headline'), 80)}**<br>{text}<br><sub>（来源：{source}）</sub>"


def _kx_digest(kx: dict[str, Any], linked: bool) -> list[str]:
    """“新闻速览”：每个栏目的标题列表；linked 时标题链接到原文。"""
    blocks = []
    for _, title, rows in _kx_groups(kx):
        lines = []
        for entry in rows:
            headline, url = md_escape(entry.get("headline"), 80), md_url(str(entry.get("url") or ""))
            lines.append(f"✨ [{headline}]({url})" if linked and url else f"✨ {headline}")
        blocks.append(f"**{title}**<br>\n" + "<br>\n".join(lines))
    return blocks


def _kx_body_md(kx: dict[str, Any], level: int) -> list[str]:
    """各栏目的正文；level 是栏目标题的级别（活动预告之外的部分标题再低一级）。"""
    blocks = []
    for heading, groups in _kx_parts(kx):
        blocks.append(f"{'#' * level} {heading}")
        for _, title, rows in groups:
            if heading != "活动预告":
                blocks.append(f"{'#' * (level + 1)} {title}")
            blocks.extend(_kx_entry_md(entry) for entry in rows)
    return blocks


def _kx_footer_md(kx: dict[str, Any], config: dict[str, Any]) -> str:
    notes = [
        md_escape(before) + (f"[{md_escape(label)}]({md_url(url)})" if url else "") + md_escape(after)
        for before, label, url, after in _kx_notes(kx, config)
    ]
    return "<sub>" + " ".join(notes) + "</sub>"


def weekly_for(day: date, weekly: dict[str, Any] | None) -> dict[str, Any] | None:
    """周一的群消息要附上刚出的每周快讯：weekly 正好是 day 前一周的那一期时返回它。"""
    if weekly and weekly.get("end") == (day - timedelta(days=1)).isoformat():
        return weekly
    return None


def _plain(text: object) -> str:
    """群消息里的文字：去掉标签和多余空白；反引号换掉，免得打断 README 里的代码块。"""
    return clean_text(text).replace("`", "'")


def render_group_text(kx: dict[str, Any], config: dict[str, Any], weekly: dict[str, Any] | None = None) -> str:
    """每日快讯的群消息文字版：每天固定时间整段复制发到群里。

    只用纯文字（不用 Markdown、不放图），每条一行标题、一行要点，俱乐部动态只写标题，活动预告写日期；
    原文链接都在完整版里，末尾只放完整版的链接。周一再附上刚出的每周快讯。
    """
    day = date.fromisoformat(kx["day"])
    entries = _kx_entries(kx)
    count = sum(entry.get("cat") != "events" for entry in entries)
    lines = [
        f"【每日科技快讯】{day.month}月{day.day}日 {weekday_name(day)}",
        f"今日 AI 与开源要闻 {count} 条，3 分钟速读",
    ]
    number = 0
    for name, title, rows in _kx_groups(kx):
        lines += ["", f"【{title}】"]
        for entry in rows:
            if name == "events":
                lines.append(f"· {_plain(entry.get('when'))} {_plain(entry.get('headline'))}")
                continue
            number += 1
            lines.append(f"{number}. {_plain(entry.get('headline'))}")
            if name != "club":  # 俱乐部的标题就是统计数字，正文太长
                lines.append(f"→ {_plain(entry.get('body'))}")
    if not entries:
        lines += ["", "今天没有收集到内容。"]
    lines.append("")
    if weekly:
        lines.append(f"上周快讯（{kx_range(weekly)}）已出：{REPO_URL}/blob/main/{kuaixun_paths(weekly)[0]}")
    lines.append(f"完整版（含原文链接）：{REPO_URL}/blob/main/{kuaixun_paths(kx)[0]}")
    if any(entry.get("ai") for entry in entries):
        lines.append("标题和要点由 AI 整理，可能有误，请以原文为准。")
    return "\n".join(lines) + "\n"


def _kx_daily_readme(kx: dict[str, Any], config: dict[str, Any], weekly: dict[str, Any] | None = None) -> list[str]:
    """README 里的每日快讯：先是可以整段复制的群消息文字版（折叠起来），再全文照登。"""
    page, sheet = kuaixun_paths(kx)
    day = date.fromisoformat(kx["day"])
    nav = " · ".join(
        [
            f"[单独打开]({page})",
            f"[公众号排版版]({sheet})",
            f"[完整日报（含热度和原题）]({daily_path(day)})",
            "[往期日报](daily/README.md)",
        ]
    )
    entries = len([e for e in _kx_entries(kx) if e.get("cat") != "events"])
    text = render_group_text(kx, config, weekly_for(day, weekly))
    blocks = [
        f"## 每日快讯 · {kx_range(kx)}（{weekday_name(day)}）",
        f"> 今日 AI 与开源要闻 **{entries}** 条，3 分钟速读。<br>\n> {nav}",
        f"<details>\n<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>\n\n```text\n{text}```\n\n</details>",
    ]
    return [*blocks, *_kx_body_md(kx, level=3), _kx_footer_md(kx, config)]


def _kx_readme(kx: dict[str, Any]) -> list[str]:
    week = kx["week"]
    sheet = weekly_html_path(week)
    nav = f"[阅读全文]({weekly_path(week)}) · [公众号排版版]({sheet}) · [往期快讯](weekly/README.md)"
    return [
        f"## 每周快讯 · {kx_range(kx)}",
        f"> 上周 AI 与开源要闻 **{len(_kx_entries(kx))}** 条，5 分钟速读。<br>\n> {nav}",
        *_kx_digest(kx, linked=True),
    ]


def render_kuaixun(kx: dict[str, Any], config: dict[str, Any]) -> str:
    """一期快讯的 Markdown 页面：每周的是 weekly/<周>.md，每日的是 daily/<年>/<日期>-kuaixun.md。"""
    page, sheet = kuaixun_paths(kx)
    here = posixpath.dirname(page)
    if _daily(kx):
        day = date.fromisoformat(kx["day"])
        nav = [
            f"[群消息文字版]({_relative(here, group_text_path(kx))})",
            f"[完整日报（含热度和原题）]({_relative(here, daily_path(day))})",
            f"[往期日报]({_relative(here, 'daily/README.md')})",
            f"[每周快讯]({_relative(here, 'weekly/README.md')})",
        ]
    else:
        nav = ["[往期快讯](README.md)", f"[每日日报]({_relative(here, 'daily/README.md')})"]
    nav.append(f"[公众号排版版]({_relative(here, sheet)})")
    blocks = [
        f"# {kx_title(kx)}",
        f"> {_kx_intro(kx)}<br>\n> 本期为您带来：{' · '.join(f'**{b}**' for b in _kx_brings(kx))}<br>\n"
        f"> {' · '.join(nav)}",
    ]
    if _kx_parts(kx):
        blocks += ["## 新闻速览", *_kx_digest(kx, linked=False)]
    else:
        blocks.append("这一期没有收集到内容。")
    blocks += _kx_body_md(kx, level=2)
    blocks += ["---", _kx_footer_md(kx, config)]
    return "\n\n".join(blocks) + "\n"


# 公众号编辑器只保留写在标签上的样式；链接在公众号里点不了，所以来源直接写网址（《CCF开源快讯》也是这样）
_WX = {
    "page": "max-width:677px;margin:0 auto;padding:16px;font-family:-apple-system,BlinkMacSystemFont,"
    "'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#333;font-size:15px;line-height:1.75;"
    "letter-spacing:0.5px;",
    "title": "margin:8px 0 16px;font-size:22px;font-weight:bold;line-height:1.4;color:#1a1a1a;",
    "intro": "margin:0 0 20px;padding:12px 14px;background:#f3f6fc;border-radius:6px;font-size:14px;color:#555;",
    "part": "margin:28px 0 12px;padding:6px 12px;background:#1e5eff;color:#fff;font-size:17px;font-weight:bold;"
    "border-radius:4px;",
    "group": "margin:22px 0 8px;padding-left:10px;border-left:4px solid #1e5eff;font-size:16px;font-weight:bold;"
    "color:#1e5eff;",
    "label": "margin:14px 0 4px;font-size:14px;font-weight:bold;color:#1e5eff;",
    "digest": "margin:4px 0;font-size:14px;color:#333;",
    "headline": "margin:16px 0 6px;font-size:15px;font-weight:bold;color:#1a1a1a;",
    "body": "margin:0 0 6px;font-size:15px;color:#333;text-align:justify;",
    "source": "margin:0 0 14px;font-size:12px;line-height:1.6;color:#888;word-break:break-all;",
    "footer": "margin:28px 0 0;padding-top:12px;border-top:1px solid #e5e5e5;font-size:12px;color:#999;",
}


def _wx(kind: str, text: str) -> str:
    return f'<p style="{_WX[kind]}">{text}</p>'


def render_kuaixun_html(kx: dict[str, Any], config: dict[str, Any]) -> str:
    """公众号排版版（和 Markdown 页面放在一起，扩展名 .html）。用浏览器打开，全选复制，粘贴到公众号编辑器。"""
    esc = html.escape
    title = kx_title(kx)
    body = [
        _wx("title", esc(title)),
        _wx("intro", esc(_kx_intro(kx)) + "<br>本期为您带来：" + esc("、".join(_kx_brings(kx)))),
    ]
    parts = _kx_parts(kx)
    if parts:
        body.append(_wx("part", "新闻速览"))
    for _, name, rows in _kx_groups(kx):
        body.append(_wx("label", esc(name)))
        body.extend(_wx("digest", "✨" + esc(str(entry.get("headline") or ""))) for entry in rows)
    for heading, groups in parts:
        body.append(_wx("part", heading))
        for _, name, rows in groups:
            if heading != "活动预告":
                body.append(_wx("group", esc(name)))
            for entry in rows:
                url = md_url(str(entry.get("url") or ""))
                body += [
                    _wx("headline", esc(str(entry.get("headline") or ""))),
                    _wx("body", esc(f"{entry.get('when', '')}，{entry.get('body', '')}")),
                    _wx("source", esc(f"（来源：{url or entry.get('via') or '原文'}）")),
                ]
    notes = [
        esc(before + (f"{label}（{url}）" if url else "") + after)
        for before, label, url, after in _kx_notes(kx, config)
    ]
    body.append(_wx("footer", "<br>".join(notes)))
    page = [
        "<!doctype html>",
        '<html lang="zh-CN">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{esc(title)}</title>",
        "</head>",
        '<body style="margin:0;background:#ffffff;">',
        "<!-- 公众号排版版：用浏览器打开这个文件，全选、复制，粘贴到公众号编辑器即可，样式会一起带过去。 -->",
        f'<section style="{_WX["page"]}">',
        *body,
        "</section>",
        "</body>",
        "</html>",
    ]
    return "\n".join(page) + "\n"
