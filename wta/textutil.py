"""文本小工具：清洗、截断、关键词匹配、热度换算。"""

from __future__ import annotations

import html
import math
import re
import unicodedata
from typing import Any
from urllib.parse import urlsplit

MAX_INPUT = 100_000  # 再长的输入也只看前这么多字符：最终只取几百字，没必要处理几兆的正文

# 只删“确实是 HTML 标签”的东西。标题里的 <think>、Vec<T>、x < y 是正文，要留着，
# 进页面之前 render.md_escape 会统一转义尖括号。
_HTML_TAGS = (
    "a|abbr|article|b|blockquote|br|code|div|em|figcaption|figure|h[1-6]|hr|i|iframe|img|li|ol|p|picture|pre|"
    "s|section|small|source|span|strong|sub|sup|table|tbody|td|th|thead|tr|u|ul|video"
)
_TAG = re.compile(rf"</?(?:{_HTML_TAGS})(?![A-Za-z0-9-])[^<>]*>", re.IGNORECASE)

# 看不见的字符，按 Unicode 码位的范围列出（起、止）。它们能在标题里藏人眼看不到、
# 大模型却读得到的文字；其中孤立的代理字符还会让写文件时报错。
# 用码位而不是把字符直接写在源码里：字面的不可见字符会被编辑器悄悄改坏，GitHub 也会报警。
_INVISIBLE_RANGES = (
    (0x00, 0x08),  # 控制字符（制表符、换行、回车除外，它们按空白处理）
    (0x0B, 0x0C),
    (0x0E, 0x1F),
    (0x7F, 0x84),
    (0x86, 0x9F),
    (0xAD, 0xAD),  # 软连字符
    (0x061C, 0x061C),
    (0x180E, 0x180E),
    (0x200B, 0x200F),  # 零宽字符和方向标记
    (0x2028, 0x202E),  # 行、段分隔符和方向控制符
    (0x2060, 0x2064),
    (0x2066, 0x206F),
    (0xD800, 0xDFFF),  # 孤立的代理字符
    (0xE000, 0xF8FF),  # 私用区
    (0xFEFF, 0xFEFF),
    (0xFFF9, 0xFFFB),
    (0xE0000, 0xE0FFF),  # 标签字符
)
_INVISIBLE = re.compile("[" + "".join(f"{chr(first)}-{chr(last)}" for first, last in _INVISIBLE_RANGES) + "]")
_SPACE = re.compile(r"\s+")
# 各种连字符统一成 "-"：真实标题里的 GPT-6 常用不换行连字符（U+2011）来写
DASHES = {code: "-" for code in (0x2010, 0x2011, 0x2012, 0x2013, 0x2014, 0x2015, 0x2212)}
_EDGE_LEFT, _EDGE_RIGHT = r"(?<![A-Za-z0-9])", r"(?![A-Za-z0-9])"


def _drop_blocks(text: str, opening: str, closing: str) -> str:
    """删掉 opening…closing 之间的内容（注释、<script>、<style>），不区分大小写。

    用 str.find 一段一段往后找，耗时和长度成正比。用正则的 .*? 来做的话，
    遇到几万个只有开头没有结尾的标记会慢到平方级，一个恶意的订阅源就能拖垮整次运行。
    """
    lowered = text.lower()
    parts: list[str] = []
    position = 0
    while True:
        start = lowered.find(opening, position)
        if start == -1:
            break
        end = lowered.find(closing, start + len(opening))
        if end == -1:
            break  # 没有结尾：剩下的当普通文字，之后尖括号会被转义
        parts.append(text[position:start])
        close_end = lowered.find(">", end)
        position = len(text) if close_end == -1 else close_end + 1
        parts.append(" ")
    parts.append(text[position:])
    return "".join(parts)


def clean_text(text: object, limit: int = 0) -> str:
    """去掉 HTML 标签、看不见的字符和多余空白；limit > 0 时截断并加省略号。"""
    if not text:
        return ""
    out = str(text)[:MAX_INPUT]
    if "<" in out:
        for opening, closing in (("<!--", "--"), ("<script", "</script"), ("<style", "</style")):
            out = _drop_blocks(out, opening, closing)
        out = _TAG.sub(" ", out)
    for _ in range(2):  # RSS 里常见二次转义：&amp;amp; &amp;#8217;
        if "&" not in out:
            break
        out = html.unescape(out)
    out = _SPACE.sub(" ", _INVISIBLE.sub("", out)).strip()
    if limit and len(out) > limit:
        out = out[: limit - 1].rstrip() + "…"
    return out


def log_scale(value: float, full: float) -> float:
    """把一个计数换算成 0~1 的热度：value 达到 full 时为 1，用对数压缩大数。"""
    if not value or value <= 0 or full <= 1:
        return 0.0
    return min(1.0, math.log1p(min(float(value), 1e15)) / math.log1p(full))


def _compile(terms: list[str], flags: int, what: str) -> re.Pattern[str] | None:
    terms = [t for t in (terms or []) if t]
    if not terms:
        return None
    for term in terms:  # 逐个试编译，写错的时候能指出是哪一条
        try:
            re.compile(term)
        except re.error as exc:
            raise ValueError(f"config.yaml 的 keywords.{what} 里有写错的正则：{term!r}（{exc}）") from exc
    return re.compile(_EDGE_LEFT + "(?:" + "|".join(terms) + ")" + _EDGE_RIGHT, flags)


class KeywordMatcher:
    """判断一段文字是否和关注的主题（AI / 大模型）有关。

    词表来自 config.yaml 的 keywords，每一条都是正则片段：
    - exact：区分大小写的缩写，如 AI、RAG、LoRA（这样不会命中 said、LoRa）；
    - any_case：不区分大小写的词和短语，中英文都可以写；
    - exclude：同形异义的短语，如 "Claude Shannon"，命中后只屏蔽它自己那几个字；
    - domains：这些网站的内容即使标题里没有关键词也算相关。
    所有词都要求两侧不是英文字母或数字。
    """

    def __init__(self, keywords: dict[str, Any] | None):
        keywords = keywords or {}
        self._exact = _compile(keywords.get("exact"), 0, "exact")
        self._any_case = _compile(keywords.get("any_case"), re.IGNORECASE, "any_case")
        self._exclude = _compile(keywords.get("exclude"), re.IGNORECASE, "exclude")
        self._domains = tuple(d.lower().removeprefix("www.") for d in keywords.get("domains") or [])

    def hits(self, text: str, url: str = "") -> list[str]:
        """返回命中的关键词（去重、保持出现顺序）；空列表表示无关。"""
        text = unicodedata.normalize("NFKC", (text or "")[:MAX_INPUT]).translate(DASHES)
        if self._exclude:
            text = self._exclude.sub(" ", text)
        found = [m.group(0) for pattern in (self._exact, self._any_case) if pattern for m in pattern.finditer(text)]
        if not found and url and self._domains:
            try:
                host = (urlsplit(url).hostname or "").lower().removeprefix("www.")
            except ValueError:  # 写坏的链接（例如 https://[x]/）当作没有域名
                host = ""
            if any(host == domain or host.endswith("." + domain) for domain in self._domains):
                found = [host]
        return list(dict.fromkeys(term.lower() for term in found))

    def match(self, text: str, url: str = "") -> bool:
        return bool(self.hits(text, url))
