"""原文摘录：入选的 AI 动态里，来源没给简介的那几条（主要是 Hacker News 的帖子，只有标题和链接），
到原文网页里取一小段文字，给大模型写中文摘要当依据。

- 只在写摘要之前、只对入选条目里缺简介的那几条做，一天十来个网页，有总时间上限；
- 只取网页自己写的描述（meta description、og:description）和正文开头几段，最多存 800 字，
  只给大模型当资料，不显示在页面上，也不保存全文；
- 需要登录才能看的网站（X、领英等）直接跳过；取不到、不是网页、太慢都算了，这一条照旧只有标题；
- 每条只试一次（记在 extra["excerpt_tried"]），之后补写的运行不会反复去请求同一个网页。

网页里的文字和其他抓来的文字一样不可信：进大模型时当资料，模型的输出照常经过 editor 的核对。
"""

from __future__ import annotations

import logging
import time
from html.parser import HTMLParser
from urllib.parse import urlsplit

from .editor import EVIDENCE_MIN, evidence_of
from .http import Http, HttpError
from .models import Item
from .textutil import clean_text

log = logging.getLogger(__name__)

SECTIONS = ("news",)  # 论文有摘要，开源项目有仓库简介；只有 AI 动态常常什么都没有
LIMIT = 800  # 存下来的摘录最多多少字
TOTAL_SECONDS = 90  # 所有网页加起来最多用多久
PAGE_SECONDS = 15  # 单个网页最多用多久
# 需要登录才能看、或者正文不在网页里的网站：取回来的只会是登录页或空壳
SKIP_HOSTS = (
    "twitter.com",
    "x.com",
    "linkedin.com",
    "facebook.com",
    "instagram.com",
    "threads.net",
    "youtube.com",
    "youtu.be",
    "reddit.com",
    "news.ycombinator.com",
)
_SKIP_TAGS = {"script", "style", "noscript", "nav", "header", "footer", "aside", "form", "svg", "template", "button"}
_DESCRIPTIONS = {"description", "og:description", "twitter:description"}
_MIN_PARAGRAPH = 40  # 比这短的段落多半是按钮、署名、日期


class _Page(HTMLParser):
    """收集网页描述和 <p> 段落里的文字，跳过导航、页眉页脚、脚本等。"""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.descriptions: list[str] = []
        self.paragraphs: list[str] = []
        self._skip = 0  # 现在处在几层“不要的标签”里面
        self._paragraph: list[str] | None = None
        self._collected = 0

    def _close_paragraph(self) -> None:
        if self._paragraph is not None:
            text = clean_text(" ".join(self._paragraph))
            if len(text) >= _MIN_PARAGRAPH:
                self.paragraphs.append(text)
                self._collected += len(text)
            self._paragraph = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in _SKIP_TAGS:
            self._skip += 1
        elif tag == "meta":
            values = {name.lower(): value or "" for name, value in attrs}
            key = (values.get("name") or values.get("property") or "").lower()
            if key in _DESCRIPTIONS and values.get("content"):
                self.descriptions.append(clean_text(values["content"]))
        elif tag == "p":
            self._close_paragraph()  # 上一段没写 </p> 也算结束
            if not self._skip and self._collected < 4 * LIMIT:
                self._paragraph = []

    def handle_endtag(self, tag: str) -> None:
        if tag in _SKIP_TAGS and self._skip:
            self._skip -= 1
        elif tag == "p":
            self._close_paragraph()

    def handle_data(self, data: str) -> None:
        if self._paragraph is not None and not self._skip:
            self._paragraph.append(data)


def page_text(html: str) -> str:
    """从网页里取描述和正文开头几段，合起来最多 LIMIT 字。"""
    page = _Page()
    page.feed(html[:2_000_000])
    page.close()
    description = max(page.descriptions, key=len, default="")
    parts = [description] if description else []
    for paragraph in page.paragraphs:
        if paragraph[:60] in description:  # 很多网站的描述就是第一段
            continue
        parts.append(paragraph)
        if sum(len(part) for part in parts) >= LIMIT:
            break
    return clean_text(" ".join(parts), LIMIT)


def fetchable(url: str) -> bool:
    parts = urlsplit(url)
    host = (parts.hostname or "").lower()
    if parts.scheme not in ("http", "https") or not host:
        return False
    return not any(host == skip or host.endswith("." + skip) for skip in SKIP_HOSTS)


def fetch(http: Http, url: str) -> str:
    """取一个网页的摘录；不是网页返回空字符串，请求失败抛 HttpError。"""
    response = http.get(url, timeout=(5, 10), retries=1, max_seconds=PAGE_SECONDS)
    headers = getattr(response, "headers", None) or {}
    kind = next((value for name, value in headers.items() if name.lower() == "content-type"), "")
    if kind and "html" not in kind.lower():
        return ""
    return page_text(response.text)


def _wanted(item: Item) -> bool:
    return (
        item.section in SECTIONS
        and not item.summary_zh
        and len(evidence_of(item)) < EVIDENCE_MIN
        and not item.extra.get("excerpt_tried")
        and fetchable(item.url)
    )


def enrich(items: list[Item], http: Http | None = None, seconds: float = TOTAL_SECONDS) -> int:
    """给缺简介的条目加上原文摘录（写进 item.extra["evidence"]），返回试过几条。

    取到摘录的条目会去掉“已处理”的标记，下一次写摘要时补上中文摘要（已有的中文标题不动）。
    """
    todo = [item for item in items if _wanted(item)]
    if not todo:
        return 0
    http = http or Http()
    previous, http.deadline = http.deadline, time.monotonic() + seconds
    tried = added = 0
    try:
        for item in todo:
            if time.monotonic() >= http.deadline:
                break  # 总时间用完了：剩下的留给下一次运行
            item.extra["excerpt_tried"] = True
            tried += 1
            try:
                text = fetch(http, item.url)
            except HttpError as exc:
                log.info("取不到原文摘录（%s）：%s", clean_text(str(exc), 120), item.title[:60])
                continue
            except Exception:  # 网页写得再怪也不能影响出刊
                log.exception("解析原文网页出错：%s", item.url)
                continue
            if len(text) >= EVIDENCE_MIN:
                item.extra["evidence"] = text
                item.extra.pop("llm_done", None)
                added += 1
    finally:
        http.deadline = previous
    log.info("原文摘录：%d 条缺简介，试了 %d 条，取到 %d 条", len(todo), tried, added)
    return tried
