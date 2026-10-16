"""去重：把链接规范化成统一写法，合并重复内容。"""

from __future__ import annotations

import hashlib
import re
from difflib import SequenceMatcher
from urllib.parse import parse_qsl, urlencode, urlsplit

from .models import Item

# 只用于统计来路、不影响页面内容的查询参数
_TRACKING = re.compile(r"^(utm_\w+|mc_cid|mc_eid|fbclid|gclid|igshid|spm|ref|ref_src|share_token)$", re.IGNORECASE)
# 同一篇论文在不同网站上的地址，统一成 arxiv:编号
_ARXIV = re.compile(
    r"(?:arxiv\.org/(?:abs|pdf|html)/|huggingface\.co/papers/|alphaxiv\.org/(?:abs|overview)/)(\d{4}\.\d{4,5})",
    re.IGNORECASE,
)
_GITHUB_REPO = re.compile(r"^/([^/]+)/([^/]+?)(?:\.git)?/?$")
_MODELSCOPE_MODEL = re.compile(r"^/models/([^/]+)/([^/]+)/?$")
_NOT_WORD = re.compile(r"[^0-9a-z一-鿿]+")
_DIGITS = re.compile(r"\d+")
_HEAD = re.compile(r"\s*[:：]\s*|\s+[–—|-]\s+")  # 标题和副标题之间的分隔符


def canonical_url(url: str) -> str:
    """把链接变成去重用的统一写法（不是给人点的地址）。

    忽略 http/https、www、末尾斜杠、锚点和统计参数；GitHub 仓库不区分大小写；
    arXiv 论文不管是摘要页、PDF 还是 Hugging Face 论文页，都算同一篇。
    同一个模型在 Hugging Face 和魔搭上的页面也算同一条。
    """
    url = (url or "").strip()
    paper = _ARXIV.search(url)
    if paper:
        return f"arxiv:{paper.group(1)}"
    parts = urlsplit(url)
    host = parts.netloc.lower().removeprefix("www.")
    path = parts.path or "/"
    if host == "github.com":
        repo = _GITHUB_REPO.match(path)
        if repo:
            return f"github.com/{repo.group(1).lower()}/{repo.group(2).lower()}"
    if host == "modelscope.cn":  # 魔搭上的模型和 Hugging Face 上同名的那个算同一条
        model = _MODELSCOPE_MODEL.match(path)
        if model:
            host, path = "huggingface.co", f"/{model.group(1)}/{model.group(2)}"
    if host == "huggingface.co":
        path = path.lower()
    query = urlencode(
        sorted((k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if not _TRACKING.match(k))
    )
    path = path.rstrip("/") or "/"
    return f"{host}{path}" + (f"?{query}" if query else "")


def item_id(url: str) -> str:
    return hashlib.sha1(canonical_url(url).encode("utf-8")).hexdigest()[:12]


def _normalize_title(title: str) -> str:
    return _NOT_WORD.sub("", title.lower())


def _head(title: str) -> str | None:
    """标题里冒号、破折号、竖线前面的部分（规范化以后）；标题里没有这些分隔符时返回 None。"""
    parts = _HEAD.split(title, maxsplit=1)
    return _normalize_title(parts[0]) if len(parts) == 2 else None


def similar_titles(a: str, b: str, threshold: float) -> bool:
    """两个标题是否基本相同。

    太短的标题只认完全相同；标题里的数字必须一致，
    否则 "Llama 3.1 发布" 和 "Llama 3.2 发布" 会被当成同一条。
    """
    na, nb = _normalize_title(a), _normalize_title(b)
    if not na or not nb:
        return False
    # 一个标题正好是另一个冒号前的部分：“Gemini 4 Argon”和“Gemini 4 Argon: Built to solve…”（10-15 同一期出现了两次）
    if min(len(na), len(nb)) >= 12 and (na == _head(b) or nb == _head(a)):
        return True
    if min(len(na), len(nb)) < 12:
        return na == nb
    if _DIGITS.findall(na) != _DIGITS.findall(nb):
        return False
    return SequenceMatcher(None, na, nb).ratio() >= threshold


def _priority(item: Item) -> tuple[float, float]:
    return (item.weight, item.heat)


def merge_into(keep: Item, other: Item) -> None:
    """把 other 的信息并进 keep：指标取较大值，并记下它还出现在哪个来源。"""
    for name, value in other.metrics.items():
        keep.metrics[name] = max(keep.metrics.get(name, 0), value)
    keep.heat = max(keep.heat, other.heat)
    # “相关性存疑”的标记：只要有一份来自不需要复核的来源，这条内容就不算存疑
    both_doubtful = keep.extra.get("needs_review") and other.extra.get("needs_review")
    for name, value in other.extra.items():
        keep.extra.setdefault(name, value)
    if not both_doubtful:
        keep.extra.pop("needs_review", None)
    if not keep.summary and other.summary:
        keep.summary = other.summary
    if not keep.published and other.published:
        keep.published = other.published
    # 当天重跑时，之前大模型写好的中文标题和摘要要保留下来
    keep.title_zh = keep.title_zh or other.title_zh
    keep.summary_zh = keep.summary_zh or other.summary_zh
    keep.tags = keep.tags or other.tags
    for via in [other.via, *other.also_in]:
        if via and via != keep.via and via not in keep.also_in:
            keep.also_in.append(via)
    # 记住被并掉的那一份：之后几天它单独出现时，也算“已经登过”
    for merged in [other.id, *other.merged_ids]:
        if merged and merged != keep.id and merged not in keep.merged_ids:
            keep.merged_ids.append(merged)


def _title_merge_order(item: Item) -> tuple[bool, float, float]:
    """按标题合并时谁留下：发布方自己的订阅优先，谁都能发帖的 Hacker News 排最后。

    Hacker News 的标题和链接由发帖人随便填。如果让它凭分数留下，一条同名帖子
    就能用自己的链接顶替媒体原文，还带着“同时见于某媒体”的背书。
    """
    return (item.source != "hackernews", *_priority(item))


def dedupe(items: list[Item], title_similarity: float = 0.92) -> list[Item]:
    """同一链接只留一条；news 栏目里同一个网站上标题几乎相同的也合并。

    留下来源权重更高的那条（权重相同看热度），另一条的指标并进来。
    按标题合并时发布方的订阅优先于 Hacker News（原因见 _title_merge_order）。
    论文和仓库只按链接判断，因为它们的标题容易撞车（例如不同仓库同名）。
    """
    by_id: dict[str, Item] = {}
    for item in items:
        item.id = item.id or item_id(item.url)
        kept = by_id.get(item.id)
        if kept is None:
            by_id[item.id] = item
        elif _priority(item) > _priority(kept):
            merge_into(item, kept)
            by_id[item.id] = item
        else:
            merge_into(kept, item)

    result: list[Item] = []
    news: list[Item] = []
    for item in sorted(by_id.values(), key=_title_merge_order, reverse=True):
        if item.section == "news":
            # 只合并不同来源之间的：同一个订阅里两篇标题一样的文章，是两篇不同的文章
            # 只合并不同来源之间的：同一个订阅里两篇标题一样的文章，是两篇不同的文章
            twin = next(
                (n for n in news if n.via != item.via and similar_titles(n.title, item.title, title_similarity)), None
            )
            if twin is not None:
                merge_into(twin, item)
                continue
            news.append(item)
        result.append(item)
    return result
