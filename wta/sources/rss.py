"""RSS / Atom 订阅：官方博客、作者博客、中英文科技媒体。

订阅列表写在 config.yaml 的 sources.rss.feeds 里，每个订阅可以设置：

    name           显示的名字（必填）
    url            订阅地址（必填）
    section        放进哪个栏目：news（默认）/ opensource / papers
    weight         重要程度 0~1（默认 0.5）。订阅源没有点赞数这类指标，排序主要靠它
    max_items      每次最多取几条（默认 3）
    max_age_hours  只要多少小时内发布的（默认用 sources.rss.max_age_hours）
    only_related   true 表示只要和 AI 相关的条目（综合类媒体用）
    title_match    标题必须匹配的正则（例如只要“科技爱好者周刊”）
    naive_offset   日期没写时区时按 UTC+几 理解（中文网站写 8）
    force_offset   无视日期里写的时区，按 UTC+几 理解（个别网站把北京时间标成了 GMT）
    no_summary     true 表示不采用它的简介（有的源简介只是一个分类名）

很多官方订阅源会带上全部历史文章（OpenAI 有一千多条），所以一定按发布时间筛选；
没有日期的条目不算新内容，直接跳过。
"""

from __future__ import annotations

import re
from datetime import timedelta
from typing import Any

from ..dates import to_iso
from ..feeds import parse_feed
from ..models import Item
from .base import Context

NAME = "rss"
TITLE = "RSS 订阅"

ACCEPT = "application/atom+xml, application/rss+xml, application/xml;q=0.9, text/xml;q=0.8, */*;q=0.5"


def expand(config: dict[str, Any]) -> list[tuple[str, str, dict[str, Any]]]:
    """每个订阅单独抓取、单独记录结果，这样一个订阅出错不影响其他订阅，也能看出是哪个坏了。"""
    shared = {"max_age_hours": config.get("max_age_hours", 48)}
    units = []
    for number, feed in enumerate(config.get("feeds") or [], 1):
        if not isinstance(feed, dict) or not feed.get("name"):  # 写错的这一条单独失败，不连累其他订阅
            feed = {"name": f"第 {number} 个订阅（配置缺少 name）"}
        units.append((f"{NAME}:{feed['name']}", str(feed["name"]), {**shared, **feed}))
    return units


def _related(ctx: Context, title: str, summary: str, url: str) -> bool:
    """综合类媒体的相关性判断：标题命中关键词，或者标题加简介里出现至少两个不同的关键词。

    正文里顺带提一句 AI 的文章很多，只凭简介里的一个词不算数。
    """
    return ctx.keywords.match(title, url) or len(ctx.keywords.hits(f"{title} {summary}")) >= 2


def fetch(config: dict[str, Any], ctx: Context) -> list[Item]:
    response = ctx.http.get(config["url"], headers={"Accept": ACCEPT})
    entries = parse_feed(
        response.content,
        response.url or config["url"],
        now=ctx.now,
        naive_offset=float(config.get("naive_offset", 0)),
        force_offset=config.get("force_offset"),
    )
    if not entries:
        raise RuntimeError("订阅源里一条内容都没有")
    if not any(entry["published"] for entry in entries):
        raise RuntimeError("所有条目的日期都解析不了（检查 naive_offset / force_offset，或者这个源的日期写法）")
    oldest = ctx.now - timedelta(hours=float(config["max_age_hours"]))
    title_match = re.compile(config["title_match"]) if config.get("title_match") else None
    weight = float(config.get("weight", 0.5))
    items: list[Item] = []
    for entry in entries:  # 已按发布时间从新到旧排好
        if len(items) >= int(config.get("max_items", 3)):
            break
        published = entry["published"]
        if published is None or published < oldest:
            continue
        if title_match and not title_match.search(entry["title"]):
            continue
        summary = "" if config.get("no_summary") else entry["summary"]
        if config.get("only_related") and not _related(ctx, entry["title"], summary, entry["url"]):
            continue
        items.append(
            Item(
                title=entry["title"],
                url=entry["url"],
                source=NAME,
                section=config.get("section", "news"),
                via=config["name"],
                published=to_iso(min(published, ctx.now)),  # 有的博客会把日期写到未来
                summary=summary,
                heat=weight,
                weight=weight,
            )
        )
    return items
