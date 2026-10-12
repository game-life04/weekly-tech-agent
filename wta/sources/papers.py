"""前沿论文：两条线。

1. 热门线：Hugging Face Daily Papers 最近几天里点赞最多的论文。这是目前唯一免费、
   稳定、当周就有反馈的论文热度信号（Papers with Code 已经关站）。
2. 关注方向线：按 config.yaml 里每个方向的标题短语去 arXiv 搜最近几天的论文，
   再用“有点赞或放出了代码”把关。arXiv 每周几千篇，只靠关键词会被淹没。

回看 7 天而不是只看当天：论文公布几天后点赞才上来，arXiv 的公布也常比提交晚几天。
已经登过的论文由流程统一去重，不会重复出现。

arXiv 的使用规定是每 3 秒最多一次请求、同一时间只能有一个连接，所以这里串行并且主动等待。
"""

from __future__ import annotations

import logging
import re
import time
import xml.etree.ElementTree as ET
from datetime import timedelta
from typing import Any

from ..dates import to_iso
from ..feeds import safe_xml
from ..models import Item
from ..textutil import clean_text, log_scale
from .base import Context

log = logging.getLogger(__name__)

NAME = "papers"
TITLE = "论文"
MAX_SECONDS = 240  # arXiv 经常很慢，这个来源的时间上限放宽一些

HF_DAILY = "https://huggingface.co/api/daily_papers"
ARXIV_API = "https://export.arxiv.org/api/query"
ARXIV_INTERVAL = 3.1
PAGE_SIZE, MAX_PAGES = 200, 3
_ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
_CODE_LINK = re.compile(
    r"github\.com/|gitlab\.com/|huggingface\.co/|code (?:is|are|will be) (?:publicly |made )?(?:available|released)",
    re.I,
)
_last_arxiv_call = 0.0


def hf_daily_papers(ctx: Context, days: int) -> dict[str, dict[str, Any]]:
    """最近 days 天的 Daily Papers，返回 {arXiv 编号: 论文}。周末和没有论文的日子接口返回空列表。"""
    papers: dict[str, dict[str, Any]] = {}
    today = ctx.now.date()
    for offset in range(days):
        day = (today - timedelta(days=offset)).isoformat()
        page = 0
        while True:
            rows = ctx.http.get_json(HF_DAILY, params={"date": day, "limit": 100, "p": page})
            if not isinstance(rows, list):
                raise RuntimeError(f"Daily Papers 返回的格式不对：{str(rows)[:120]}")
            for row in rows:
                paper = row.get("paper") or {}
                paper_id = paper.get("id") or ""
                if paper_id and paper_id not in papers:
                    papers[paper_id] = {
                        "id": paper_id,
                        "title": clean_text(paper.get("title") or row.get("title")),
                        "abstract": clean_text(paper.get("summary") or row.get("summary")),
                        "upvotes": int(paper.get("upvotes") or 0),
                        "published": paper.get("publishedAt"),
                        "code": paper.get("githubRepo") or "",
                    }
            if len(rows) < 100:  # 响应头里永远有“下一页”，只能靠这一页不满来判断结束
                break
            page += 1
            time.sleep(0.3)
        time.sleep(0.3)
    return papers


def arxiv_query(ctx: Context, params: dict[str, Any]) -> list[dict[str, Any]]:
    """调用一次 arXiv 接口，返回 [{id, title, abstract, published, categories, comment}]。"""
    global _last_arxiv_call
    wait = ARXIV_INTERVAL - (time.monotonic() - _last_arxiv_call)
    if wait > 0:
        time.sleep(wait)
    try:  # retries=1：失败后不让底层 2 秒就重试，那样会违反 3 秒的规定；一个方向查不到就算了
        response = ctx.http.get(ARXIV_API, params=params, timeout=(15, 60), retries=1, max_seconds=90)
    finally:
        _last_arxiv_call = time.monotonic()
    try:
        root = safe_xml(response.content)
    except ET.ParseError as exc:
        raise RuntimeError(f"arXiv 返回的不是合法的 XML：{exc}") from exc
    entries = []
    for entry in root.findall("a:entry", _ATOM):
        entry_id = entry.findtext("a:id", "", _ATOM)
        if "/abs/" not in entry_id:
            continue  # 出错时 arXiv 会返回一条标题为 Error 的条目
        comment = entry.findtext("arxiv:comment", "", _ATOM) or ""
        entries.append(
            {
                "id": re.sub(r"v\d+$", "", entry_id.rsplit("/abs/", 1)[-1]),
                "title": clean_text(entry.findtext("a:title", "", _ATOM)),
                "abstract": clean_text(entry.findtext("a:summary", "", _ATOM)),
                "published": entry.findtext("a:published", "", _ATOM),
                "categories": [c.get("term") for c in entry.findall("a:category", _ATOM)],
                "comment": comment,
            }
        )
    return entries


def _paper_item(paper: dict[str, Any], via: str, heat: float, weight: float, upvotes: int, code: str = "") -> Item:
    extra: dict[str, Any] = {"links": [["代码", code]]} if code.startswith("https://") else {}
    return Item(
        title=paper["title"],
        url=f"https://arxiv.org/abs/{paper['id']}",
        source=NAME,
        section="papers",
        via=via,
        published=to_iso(paper.get("published")),
        summary=paper["abstract"],
        heat=heat,
        weight=weight,
        metrics={"upvotes": upvotes},
        extra=extra,
    )


def _popular(config: dict[str, Any], ctx: Context, hf: dict[str, dict[str, Any]]) -> list[Item]:
    settings = config.get("popular") or {}
    ranked = sorted(hf.values(), key=lambda p: (-p["upvotes"], p["id"]))
    ranked = [p for p in ranked if p["upvotes"] >= int(settings.get("min_upvotes", 20))][: int(settings.get("top", 15))]
    categories = set(config.get("categories") or [])
    if ranked and categories:
        try:  # 只留属于我们关注分类的论文（交叉分类也算），把纯视觉、机器人的论文挡在外面
            listed = arxiv_query(ctx, {"id_list": ",".join(p["id"] for p in ranked), "max_results": len(ranked)})
            allowed = {e["id"] for e in listed if categories & set(e["categories"])}
            ranked = [p for p in ranked if p["id"] in allowed]
        except Exception as exc:  # arXiv 不通时宁可不筛，也不要丢掉整条热门线
            log.warning("查询论文分类失败，本次不按分类筛选：%s", exc)
    weight = float(settings.get("weight", 0.6))
    return [
        _paper_item(p, "Hugging Face 热门论文", log_scale(p["upvotes"], 300), weight, p["upvotes"], p["code"])
        for p in ranked
    ]


def _watch(config: dict[str, Any], ctx: Context, hf: dict[str, dict[str, Any]]) -> list[Item]:
    themes = config.get("themes") or {}
    categories = config.get("categories") or []
    if not themes or not categories:
        return []
    start = (ctx.now - timedelta(days=int(config.get("days", 7)))).strftime("%Y%m%d0000")
    window = f"submittedDate:[{start} TO {ctx.now.strftime('%Y%m%d2359')}]"  # 两端都必须是 12 位数字
    category_query = " OR ".join(f"cat:{c}" for c in categories)
    gate = int(config.get("gate_upvotes", 5))
    weight = float(config.get("watch_weight", 0.8))
    items: list[Item] = []
    for theme in themes.values():
        phrases = " OR ".join(f'ti:"{phrase}"' for phrase in theme.get("phrases") or [])
        if not phrases:
            continue
        entries: list[dict[str, Any]] = []
        try:
            for start in range(0, PAGE_SIZE * MAX_PAGES, PAGE_SIZE):  # 论文多的方向一页装不下一周的量
                page = arxiv_query(
                    ctx,
                    {
                        "search_query": f"({category_query}) AND ({phrases}) AND {window}",
                        "sortBy": "submittedDate",
                        "sortOrder": "descending",
                        "start": start,
                        "max_results": PAGE_SIZE,
                    },
                )
                entries.extend(page)
                if len(page) < PAGE_SIZE:
                    break
        except Exception as exc:  # 一个方向查不到不影响其他方向；已经取到的几页照常使用
            log.warning("arXiv 查询“%s”失败：%s", theme.get("title", ""), exc)
        if not entries:
            continue
        candidates = []
        for entry in entries:
            known = hf.get(entry["id"]) or {}
            upvotes = int(known.get("upvotes") or 0)
            has_code = bool(known.get("code")) or bool(_CODE_LINK.search(f"{entry['abstract']} {entry['comment']}"))
            if upvotes < gate and not has_code:
                continue  # 既没人点赞也没放代码，无从判断质量，宁可这个方向今天空着
            heat = max(log_scale(upvotes, 300), 0.3 if has_code else 0.0)
            candidates.append((heat, entry, upvotes))
        candidates.sort(key=lambda c: c[0], reverse=True)
        via = f"arXiv · {theme.get('title', '关注方向')}"
        for heat, entry, upvotes in candidates[: int(theme.get("max_items", 6))]:
            code = (hf.get(entry["id"]) or {}).get("code") or ""
            items.append(_paper_item(entry, via, heat, weight, upvotes, code))
    return items


def fetch(config: dict[str, Any], ctx: Context) -> list[Item]:
    hf: dict[str, dict[str, Any]] = {}
    hf_error = ""
    try:
        hf = hf_daily_papers(ctx, int(config.get("days", 7)))
    except Exception as exc:  # Hugging Face 不通时，关注方向线仍然可以靠“有代码”这一条出结果
        hf_error = str(exc)
        log.warning("读取 Hugging Face Daily Papers 失败：%s", exc)
    items = _popular(config, ctx, hf) + _watch(config, ctx, hf)
    if not items and hf_error:
        raise RuntimeError(f"Hugging Face Daily Papers 读取失败：{hf_error}")
    return items
