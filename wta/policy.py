"""快讯的“政策动向”：中国政府网的“最新政策”和“要闻”两个列表里，和人工智能、开源、软件有关的条目。

两个列表都是网站自己前端在用的 JSON（标题、链接、发布日期），不用解析网页。
“最新政策”只收国务院层面的文件，一周常常一条都没有；“要闻”里有国务院常务会议和部委的消息，
所以两个都看。领导人的会见、考察这类时政新闻不收（见 config.yaml 里 kuaixun.policy.exclude）。
"""

from __future__ import annotations

import logging
import re
from datetime import date
from typing import Any

from .dates import to_iso
from .dedupe import item_id
from .http import Http
from .models import Item
from .textutil import clean_text

log = logging.getLogger(__name__)

NAME = "policy"
VIA = "中国政府网"
FEEDS = (
    "https://www.gov.cn/zhengce/zuixin/ZUIXINZHENGCE.json",
    "https://www.gov.cn/yaowen/liebiao/YAOWENLIEBIAO.json",
)
_SITE = re.compile(r"https://www\.gov\.cn/")


def _pattern(words: list[str]) -> re.Pattern[str] | None:
    words = [re.escape(word) for word in words if word]
    return re.compile("|".join(words)) if words else None


def fetch(http: Http, monday: date, sunday: date, settings: dict[str, Any]) -> list[Item]:
    """这一周里发布的相关条目，按日期排列。两个列表都取不到时抛异常。"""
    wanted, unwanted = _pattern(settings.get("keywords") or []), _pattern(settings.get("exclude") or [])
    items: dict[str, Item] = {}
    errors = []
    for feed in FEEDS:
        try:
            rows = http.get_json(feed)
        except Exception as exc:  # 一个列表取不到，另一个照用
            errors.append(f"{feed}：{exc}")
            continue
        for row in rows if isinstance(rows, list) else []:
            if not isinstance(row, dict):
                continue
            title = clean_text(row.get("TITLE"), 200)
            subtitle = clean_text(row.get("SUB_TITLE"), 200)
            url = clean_text(row.get("URL"))
            try:
                day = date.fromisoformat(str(row.get("DOCRELPUBTIME", ""))[:10])
            except ValueError:
                continue
            text = f"{title} {subtitle}"
            if not (title and _SITE.match(url) and monday <= day <= sunday):
                continue
            if wanted is None or not wanted.search(text) or (unwanted and unwanted.search(text)):
                continue
            items.setdefault(
                url,
                Item(
                    title=title,
                    url=url,
                    source=NAME,
                    section="news",
                    via=VIA,
                    published=to_iso(f"{day.isoformat()}T00:00:00+08:00"),
                    summary=subtitle,
                    extra={"kx_day": day.isoformat()},
                    id=item_id(url),
                ),
            )
    if len(errors) == len(FEEDS):
        raise RuntimeError("；".join(errors))
    for error in errors:
        log.warning("政策列表取不到：%s", error)
    return sorted(items.values(), key=lambda item: item.published)
