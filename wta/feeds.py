"""RSS / Atom 解析器，只用标准库。

支持 RSS 2.0、RSS 1.0（RDF）和 Atom。真实世界的订阅源经常不规范，所以这里做了几件事：
- 返回的是 HTML 页面（拦截页、登录页）时直接报错，而不是当成“0 条”；
- XML 不合法时修一修再试（控制字符、裸的 &、&nbsp; 这类 HTML 实体）；
- 拒绝带 DOCTYPE 声明的文档，避免实体膨胀攻击；
- 日期解析不了、明显离谱（1995 年以前、未来两天以后）的一律当作没有日期。
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from datetime import UTC, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.entities import name2codepoint
from typing import Any
from urllib.parse import urljoin

from .textutil import clean_text

_ATOM = "http://www.w3.org/2005/Atom"
_CORE_NAMESPACES = {
    "",
    _ATOM,
    "http://purl.org/atom/ns#",
    "http://purl.org/rss/1.0/",
    "http://my.netscape.com/rdf/simple/0.9/",
    "http://backend.userland.com/rss2",
}
_PREFIXES = {
    "http://purl.org/rss/1.0/modules/content/": "content:",
    "http://purl.org/dc/elements/1.1/": "dc:",
    "http://purl.org/dc/terms/": "dc:",
}
_DATE_KEYS = ("pubdate", "published", "dc:date", "dc:created", "dc:issued", "issued", "created", "updated", "modified")

_ILLEGAL_XML = re.compile(rb"[\x00-\x08\x0b\x0c\x0e-\x1f]")
_BARE_AMP = re.compile(rb"&(?!(?:#\d+|#x[0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]*);)")
_NAMED_ENTITY = re.compile(rb"&([A-Za-z][A-Za-z0-9]*);")
_XML_ENTITIES = {b"amp", b"lt", b"gt", b"quot", b"apos"}

_ISO = re.compile(r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}")
_RFC_YEAR = re.compile(r"\d{1,2}\s+[A-Za-z]{3,9}\s+(\d{4})\b")
MAX_ENTRIES = 300  # 一个订阅里只细看最新的这么多条
_FALLBACK_FORMATS = ("%B %d, %Y", "%b %d, %Y", "%d %B %Y", "%d %b %Y", "%a, %d %b %Y", "%m/%d/%Y")


class FeedError(ValueError):
    """订阅源下载到了，但内容没法当作 RSS / Atom 解析。"""


def parse_date(value: str | None, now: datetime, naive_offset: float = 0, force_offset: float | None = None):
    """把订阅源里的各种日期写法解析成 UTC 时间；解析不了或明显离谱时返回 None。

    naive_offset：字符串没写时区时，按 UTC+几 小时理解（中文网站一般是 8）。
    force_offset：无视字符串里写的时区，直接按 UTC+几 小时理解
                  （有的网站把北京时间标成 GMT）。
    """
    text = " ".join((value or "").split())
    if not text:
        return None
    moment: datetime | None = None
    if _ISO.match(text):
        iso = text.replace("/", "-")
        iso = re.sub(r"^(\d{4})-(\d{1,2})-(\d{1,2})", lambda m: f"{m[1]}-{int(m[2]):02d}-{int(m[3]):02d}", iso)
        iso = iso.replace(" ", "T", 1) if "T" not in iso else iso
        iso = re.sub(r"(\.\d{6})\d+", r"\1", iso)  # 纳秒截成微秒
        iso = re.sub(r"\s*(UTC|GMT|Z)$", "+00:00", iso)
        iso = re.sub(r"\s+([+-]\d{2}:?\d{2})$", r"\1", iso)  # "10:00:00  +0800"
        try:
            moment = datetime.fromisoformat(iso)
        except ValueError:
            moment = None
    if moment is None:
        try:
            moment = parsedate_to_datetime(text)
        except (TypeError, ValueError, IndexError, OverflowError):
            moment = None
        # 标准库会把 "Mon, 01 Jan 0001" 这种零值日期变成 2001 年，这里识别出来丢掉
        year = _RFC_YEAR.search(text)
        if moment is not None and year and int(year.group(1)) != moment.year:
            return None
    if moment is None:
        for fmt in _FALLBACK_FORMATS:
            try:
                moment = datetime.strptime(text, fmt)
                break
            except ValueError:
                continue
    if moment is None:
        return None
    if force_offset is not None:
        moment = moment.replace(tzinfo=timezone(timedelta(hours=force_offset)))
    elif moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone(timedelta(hours=naive_offset)))
    try:
        moment = moment.astimezone(UTC)
    except (OverflowError, ValueError):
        return None
    if moment.year < 1995 or moment > now + timedelta(days=2):
        return None
    return moment


def _fix_entity(match: re.Match[bytes]) -> bytes:
    name = match.group(1)
    if name in _XML_ENTITIES:
        return match.group(0)
    code = name2codepoint.get(name.decode("ascii"))
    return b"&#%d;" % code if code else b""


def _parse_xml(raw: bytes) -> ET.Element:
    raw = raw.lstrip(b"\xef\xbb\xbf \t\r\n")
    if not raw:
        raise FeedError("返回内容为空")
    head = raw[:2048].lower()
    if head.startswith((b"<!doctype html", b"<html")):
        raise FeedError("返回的是网页而不是订阅源（可能是拦截页，或订阅地址已失效）")
    try:
        return safe_xml(raw)
    except ET.ParseError as first:
        fixed = _NAMED_ENTITY.sub(_fix_entity, _BARE_AMP.sub(b"&amp;", _ILLEGAL_XML.sub(b"", raw)))
        try:
            return safe_xml(fixed)
        except ET.ParseError:
            try:  # 最后一招：按声明的编码容错解码（有的源里夹着非法字节）
                text = fixed.decode(_declared_encoding(fixed), errors="replace")
                return safe_xml(re.sub(r"^\s*<\?xml[^>]*\?>", "", text))
            except (ET.ParseError, LookupError):
                raise FeedError(f"XML 格式错误：{first}") from None


class _NoDoctype(ET.TreeBuilder):
    """遇到 DOCTYPE 声明就拒绝。

    实体只能在 DOCTYPE 里声明，所以这一条就堵住了“一个小文件展开成几百兆”的实体膨胀。
    让解析器自己来报告比在原始字节里找 <!ENTITY 可靠：后者能用注释、大小写、UTF-16 绕过。
    代价是带 DOCTYPE 的老式 RSS 0.91 也会被拒，现在已经很少见了。
    """

    def doctype(self, name: str, pubid: str | None, system: str | None) -> None:
        raise FeedError("不接受带 DOCTYPE 声明的 XML")


def safe_xml(raw: bytes | str) -> ET.Element:
    """解析不可信的 XML。格式错误抛 ET.ParseError，带 DOCTYPE 抛 FeedError。"""
    return ET.fromstring(raw, parser=ET.XMLParser(target=_NoDoctype()))


def _declared_encoding(raw: bytes) -> str:
    match = re.search(rb'encoding=["\']([A-Za-z0-9_-]+)["\']', raw[:200])
    return match.group(1).decode("ascii") if match else "utf-8"


def _key(element: ET.Element) -> str | None:
    """把带命名空间的标签名变成 'title'、'dc:date'、'content:encoded' 这样的短名；不认识的返回 None。"""
    tag = element.tag
    if not isinstance(tag, str):
        return None
    namespace, _, local = tag[1:].partition("}") if tag.startswith("{") else ("", "", tag)
    if namespace in _CORE_NAMESPACES:
        return local.lower()
    prefix = _PREFIXES.get(namespace)
    return prefix + local.lower() if prefix else None


def _text(element: ET.Element | None) -> str:
    return "".join(element.itertext()).strip() if element is not None else ""


def _children(element: ET.Element) -> dict[str, list[ET.Element]]:
    grouped: dict[str, list[ET.Element]] = {}
    for child in element:
        key = _key(child)
        if key:
            grouped.setdefault(key, []).append(child)
    return grouped


def _first(children: dict[str, list[ET.Element]], *keys: str) -> ET.Element | None:
    for key in keys:
        for element in children.get(key, ()):
            if _text(element) or element.attrib:
                return element
    return None


def _pick_link(children: dict[str, list[ET.Element]], base: str) -> str:
    fallback = ""
    for link in children.get("link", []):
        href = link.get("href")
        if href:  # Atom 的写法：<link rel="alternate" href="...">
            rel = (link.get("rel") or "alternate").lower()
            kind = (link.get("type") or "").lower()
            if rel == "alternate" and (not kind or "html" in kind):
                return urljoin(base, href.strip())
            if rel == "alternate" and not fallback:
                fallback = href.strip()
        elif _text(link):  # RSS 的写法：<link>...</link>
            return urljoin(base, _text(link))
    if fallback:
        return urljoin(base, fallback)
    for key in ("guid", "id"):
        for element in children.get(key, []):
            value = _text(element)
            if value.startswith(("http://", "https://")) and element.get("isPermaLink", "true").lower() != "false":
                return value
    return ""


def parse_feed(
    raw: bytes,
    base_url: str = "",
    *,
    now: datetime,
    summary_chars: int = 500,
    naive_offset: float = 0,
    force_offset: float | None = None,
) -> list[dict[str, Any]]:
    """解析订阅源，返回 [{title, url, published, summary, tags}]，新的在前。

    published 是 UTC 时间或 None。个别条目有问题会跳过，整个文档不能用才抛 FeedError。
    """
    root = _parse_xml(raw)
    root_key = _key(root) or root.tag.rsplit("}", 1)[-1].lower()
    if root_key == "feed":
        container, entries = root, [e for e in root if _key(e) == "entry"]
    elif root_key in ("rss", "rdf"):
        channel = next((e for e in root if _key(e) == "channel"), None)
        container = channel if channel is not None else root
        entries = [e for e in container if _key(e) == "item"] or [e for e in root if _key(e) == "item"]
    else:
        raise FeedError(f"根元素 <{root_key}> 既不是 RSS 也不是 Atom")

    link_base = _pick_link(_children(container), base_url) or base_url
    # 先只解析日期（很便宜），按新旧排好，只细看最新的一批：
    # 有的官方订阅带着上千条历史文章，逐条清洗正文既没必要，也给了坏数据拖慢运行的机会
    dated = []
    for entry in entries:
        children = _children(entry)
        published = None
        for key in _DATE_KEYS:
            for element in children.get(key, ()):
                published = published or parse_date(_text(element), now, naive_offset, force_offset)
        dated.append((published, children))
    dated.sort(key=lambda pair: pair[0] or datetime.min.replace(tzinfo=UTC), reverse=True)

    items: list[dict[str, Any]] = []
    for published, children in dated[:MAX_ENTRIES]:
        try:
            url = _pick_link(children, link_base)
        except ValueError:  # 这一条的链接写坏了，跳过它，不影响其他条目
            continue
        body = clean_text(_text(_first(children, "description", "summary"))) or clean_text(
            _text(_first(children, "content:encoded", "content"))
        )
        title = clean_text(_text(_first(children, "title"))) or clean_text(body, 80)
        if not title or not url:
            continue
        tags: list[str] = []
        for category in children.get("category", []) + children.get("dc:subject", []):
            tag = clean_text(category.get("term") or _text(category))
            if tag and tag not in tags:
                tags.append(tag)
        items.append(
            {
                "title": title,
                "url": url,
                "published": published,
                "summary": clean_text(body, summary_chars),
                "tags": tags,
            }
        )
    return items
