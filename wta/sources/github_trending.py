"""GitHub Trending：今天涨星最快的仓库里和 AI 有关的那些。

GitHub 没有 Trending 的官方接口，第三方接口要么已经停了、要么数据不可用，
所以直接解析 https://github.com/trending 的网页。解析只认语义明确的标记
（<article>、仓库链接、/stargazers 链接、“N stars today”这句话），不依赖样式类名，
页面改版时不容易失效。

“全部语言”榜单现在只有十来个仓库，所以把几个语言的榜单合在一起看。
"""

from __future__ import annotations

import re
import time
from html.parser import HTMLParser
from typing import Any

from ..models import Item
from ..textutil import log_scale
from .base import Context

NAME = "github_trending"
TITLE = "GitHub Trending"
MAX_SECONDS = 120  # 这个来源最多用多久（秒）

URL = "https://github.com/trending"
_GAINED = re.compile(r"([\d,]+)\s+stars?\s+(?:today|this\s+week|this\s+month)", re.IGNORECASE)
_REPO_HREF = re.compile(r"^/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)/?$")
_NOT_OWNERS = {"login", "signup", "sponsors", "trending", "features", "topics", "collections", "apps", "orgs", "site"}


def _to_int(text: str) -> int:
    digits = re.sub(r"\D", "", text or "")
    return int(digits) if digits else 0


class _Parser(HTMLParser):
    """一个 <article> 对应一个仓库。"""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.repos: list[dict[str, Any]] = []
        self._repo: dict[str, Any] | None = None
        self._in_h2 = False
        self._field: str | None = None  # 正在收集文字的字段
        self._closing_tag: str | None = None  # 遇到这个结束标签就收尾
        self._buffer: list[str] = []
        self._all_text: list[str] = []

    def _start(self, field: str, closing_tag: str) -> None:
        self._field, self._closing_tag, self._buffer = field, closing_tag, []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "article":
            self._repo = {"name": "", "description": "", "language": "", "stars": 0, "gained": 0}
            self._all_text, self._in_h2 = [], False
            return
        if self._repo is None:
            return
        if tag == "h2":
            self._in_h2 = True
        elif tag == "a":
            href = (attributes.get("href") or "").split("?")[0].split("#")[0]
            match = _REPO_HREF.match(href)
            if self._in_h2 and not self._repo["name"] and match and match.group(1).lower() not in _NOT_OWNERS:
                self._repo["name"] = f"{match.group(1)}/{match.group(2)}"
            elif href.endswith("/stargazers") and not self._repo["stars"]:
                self._start("stars", "a")
        elif tag == "p" and not self._repo["description"] and self._field is None:
            self._start("description", "p")
        elif tag == "span" and attributes.get("itemprop") == "programmingLanguage":
            self._start("language", "span")

    def handle_endtag(self, tag: str) -> None:
        if self._repo is None:
            return
        if tag == "h2":
            self._in_h2 = False
        if self._field and tag == self._closing_tag:
            text = " ".join("".join(self._buffer).split())
            self._repo[self._field] = _to_int(text) if self._field == "stars" else text
            self._field = self._closing_tag = None
        if tag == "article":
            gained = _GAINED.search(" ".join(" ".join(self._all_text).split()))
            self._repo["gained"] = _to_int(gained.group(1)) if gained else 0
            if self._repo["name"]:
                self.repos.append(self._repo)
            self._repo = None

    def handle_data(self, data: str) -> None:
        if self._repo is None:
            return
        self._all_text.append(data)
        if self._field:
            self._buffer.append(data)


def parse_trending(page: str) -> list[dict[str, Any]]:
    """解析 Trending 网页，返回 [{name, description, language, stars, gained}]。页面认不出来时返回空列表。"""
    parser = _Parser()
    parser.feed(page)
    parser.close()
    return parser.repos


def fetch(config: dict[str, Any], ctx: Context) -> list[Item]:
    repos: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    languages = config.get("languages", ["", "python", "typescript", "jupyter-notebook", "rust"])
    for index, language in enumerate(languages):
        if index:
            time.sleep(1)
        try:
            page = ctx.http.get_text(
                f"{URL}/{language}" if language else URL,
                params={"since": "daily"},
                headers={"Accept": "text/html", "Accept-Language": "en-US,en;q=0.8"},  # 保证 "stars today" 是英文
            )
        except Exception as exc:  # 一个榜单失败不影响其他榜单
            errors.append(f"{language or '全部语言'}：{exc}")
            continue
        for repo in parse_trending(page):
            repos.setdefault(repo["name"].lower(), repo)
    if not repos:
        raise RuntimeError("一个仓库都没解析出来（页面改版或访问受限）" + "；".join(errors))

    weight = float(config.get("weight", 0.6))
    items: list[Item] = []
    for repo in repos.values():
        url = f"https://github.com/{repo['name']}"
        if not ctx.keywords.match(f"{repo['name']} {repo['description']}", url):
            continue
        items.append(
            Item(
                title=repo["name"],
                url=url,
                source=NAME,
                section="opensource",
                summary=repo["description"],
                heat=log_scale(repo["gained"], 3000),
                weight=weight,
                metrics={"stars_today": repo["gained"], "stars": repo["stars"]},
                extra={"language": repo["language"]},
            )
        )
    return items
