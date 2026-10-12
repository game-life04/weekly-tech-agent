"""量子位：中文 AI 媒体。

它的 RSS 只有 10 条，而且新旧两个缓存版本会来回切换，所以改用网站自带的
WordPress 接口（wp-json），一次能拿到最近 30 篇。
"""

from __future__ import annotations

from datetime import timedelta
from typing import Any

from ..dates import parse_time, to_iso
from ..models import Item
from .base import Context

NAME = "qbitai"
TITLE = "量子位"

API = "https://www.qbitai.com/wp-json/wp/v2/posts"


def fetch(config: dict[str, Any], ctx: Context) -> list[Item]:
    posts = ctx.http.get_json(API, params={"per_page": 30, "_fields": "id,date_gmt,link,title,excerpt"})
    if not isinstance(posts, list) or not posts:
        raise RuntimeError("接口没有返回文章列表")
    oldest = ctx.now - timedelta(hours=float(config.get("max_age_hours", 48)))
    weight = float(config.get("weight", 0.55))
    items: list[Item] = []
    for post in posts:
        published = parse_time(post.get("date_gmt"))  # 不带时区的 UTC 时间
        if published is None or published < oldest:
            continue
        items.append(
            Item(
                title=(post.get("title") or {}).get("rendered", ""),
                url=post.get("link", ""),
                source=NAME,
                section="news",
                published=to_iso(published),
                summary=(post.get("excerpt") or {}).get("rendered", ""),
                heat=weight,
                weight=weight,
            )
        )
    return items[: int(config.get("max_items", 5))]
