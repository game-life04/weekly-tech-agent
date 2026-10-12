"""GitHub 新项目：最近 30 天内创建、涨星很快的 AI 仓库。

Trending 榜单看的是“今天涨了多少星”，容易被老牌大仓库占满；这里用官方搜索接口
专门找新仓库，按“平均每天涨多少星”排序，和 Trending 互补。

搜索接口的几条限制（实测）：话题之间不能用 OR，只能一个话题发一次请求；
带令牌每分钟 30 次、不带每分钟 10 次，所以请求之间要停两秒。
"""

from __future__ import annotations

import logging
import time
from datetime import timedelta
from typing import Any

from ..dates import parse_time
from ..models import Item
from ..textutil import log_scale
from ._github import RateLimited, api_get
from .base import Context

log = logging.getLogger(__name__)

NAME = "github_new"
TITLE = "GitHub 新项目"
MAX_SECONDS = 120  # 这个来源最多用多久（秒）

DEFAULT_TOPICS = ["llm", "ai-agents", "mcp", "claude-code", "agent-skills"]
KEYWORD_QUERY = 'llm OR agent OR rag OR mcp OR "language model" OR inference in:name,description'  # 最多 5 个 OR


def fetch(config: dict[str, Any], ctx: Context) -> list[Item]:
    days = int(config.get("days", 30))
    since = (ctx.now - timedelta(days=days)).date().isoformat()
    base = f"created:>={since} stars:>={int(config.get('min_stars', 100))} fork:false archived:false"
    queries = [f"topic:{topic} {base}" for topic in config.get("topics", DEFAULT_TOPICS)]
    queries.append(f"{KEYWORD_QUERY} {base}")

    repos: dict[str, dict[str, Any]] = {}
    failures = 0
    for index, query in enumerate(queries):
        if index:
            time.sleep(2.1)
        try:
            data = api_get(ctx, "/search/repositories", {"q": query, "sort": "stars", "order": "desc", "per_page": 100})
        except RateLimited:
            raise
        except Exception as exc:  # 一次搜索失败不影响其他搜索
            failures += 1
            log.warning("GitHub 搜索失败（%s）：%s", query.split(" ", 1)[0], exc)
            continue
        for repo in (data or {}).get("items", []):
            repos.setdefault(repo["full_name"].lower(), repo)
    if failures == len(queries):
        raise RuntimeError("所有搜索请求都失败了")

    weight = float(config.get("weight", 0.5))
    items: list[Item] = []
    for repo in repos.values():
        description = repo.get("description") or ""
        # 话题标签谁都能随便加，所以还要求名字或简介里确实出现 AI 相关的词
        if not ctx.keywords.match(f"{repo['full_name']} {description}"):
            continue
        created = parse_time(repo.get("created_at"))
        age_days = max((ctx.now - created).days, 1) if created else days
        stars = int(repo.get("stargazers_count") or 0)
        items.append(
            Item(
                title=repo["full_name"],
                url=repo["html_url"],
                source=NAME,
                section="opensource",
                summary=description,
                heat=log_scale(stars / age_days, 1500),
                weight=weight,
                metrics={"stars": stars},
                extra={"language": repo.get("language") or "", "age_days": age_days},
            )
        )
    return items
