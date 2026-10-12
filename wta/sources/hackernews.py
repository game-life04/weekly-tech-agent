"""Hacker News：最近两天里和 AI 有关的热帖。

用 Algolia 提供的 HN 搜索接口（免密钥，每 IP 每小时 1 万次）：一次请求取回时间窗口内
达到分数线的全部帖子，再在本地用关键词筛选。不用服务端关键词搜索，因为它按前缀匹配，
搜 "AI" 会带出 airport。

标题里没有关键词、但分数很高的帖子会带上 needs_review 标记：有大模型时交给它判断
是否相关，没有大模型时不展示。
"""

from __future__ import annotations

import re
from typing import Any

from ..dates import to_iso
from ..models import Item
from ..textutil import log_scale
from .base import Context

NAME = "hackernews"
TITLE = "Hacker News"

API = "https://hn.algolia.com/api/v1"
ITEM_URL = "https://news.ycombinator.com/item?id={}"
STALE_AFTER = 3 * 3600  # 最新一条帖子比这还旧，说明索引停更了（2022、2025 年各发生过一次）
_NOT_WORD = re.compile(r"[^a-z0-9]+")


def _check_fresh(ctx: Context, now: int) -> None:
    data = ctx.http.get_json(
        f"{API}/search_by_date",
        params={
            "tags": "story",
            "hitsPerPage": 1,
            "attributesToRetrieve": "created_at_i",
            "attributesToHighlight": "[]",
        },
    )
    hits = data.get("hits") or []
    if not hits or now - int(hits[0].get("created_at_i") or 0) > STALE_AFTER:
        raise RuntimeError("Algolia 的 Hacker News 索引已经几个小时没有更新")


def fetch(config: dict[str, Any], ctx: Context) -> list[Item]:
    now = int(ctx.now.timestamp())
    start = now - int(config.get("hours", 48) * 3600)
    min_points = int(config.get("min_points", 20))
    review_points = int(config.get("review_points", 250))
    _check_fresh(ctx, now)
    data = ctx.http.get_json(
        f"{API}/search",  # 不带搜索词时按分数排序；最多返回 1000 条，被截掉的只会是分数最低的
        params={
            "tags": "story",
            "numericFilters": f"created_at_i>{start},created_at_i<={now},points>={min_points}",
            "hitsPerPage": 1000,
            "attributesToRetrieve": "title,url,points,num_comments,created_at_i",
            "attributesToHighlight": "[]",  # 去掉高亮字段，响应小一大半
        },
    )
    hits = data.get("hits")
    if not isinstance(hits, list):
        raise RuntimeError(f"接口返回的格式不对：{str(data)[:120]}")

    items: list[Item] = []
    seen_titles: set[str] = set()
    for hit in hits:  # 已按分数从高到低排好
        title = (hit.get("title") or "").strip()
        story_id = hit.get("objectID")
        if not title or not story_id or not hit.get("created_at_i"):
            continue
        title_key = _NOT_WORD.sub("", title.lower())
        if len(title_key) >= 8 and title_key in seen_titles:
            continue  # 同一个标题被提交了好几次，只留分数最高的
        seen_titles.add(title_key)
        discussion = ITEM_URL.format(story_id)
        url = (hit.get("url") or "").strip() or discussion  # Ask HN 这类帖子没有外链
        points = int(hit.get("points") or 0)
        related = ctx.keywords.match(title, url)
        if not related and points < review_points:
            continue
        items.append(
            Item(
                title=title,
                url=url,
                source=NAME,
                section="news",
                published=to_iso(hit["created_at_i"]),
                heat=log_scale(points, 500),
                weight=float(config.get("weight", 0.6)),
                metrics={"points": points, "comments": int(hit.get("num_comments") or 0)},
                extra={"discussion": discussion} | ({} if related else {"needs_review": True}),
            )
        )
    return items
