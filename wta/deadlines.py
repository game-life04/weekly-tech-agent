"""快讯的“活动预告”：接下来几周截稿的 CCF 推荐会议。

数据来自社区维护的 CCF 推荐会议截稿列表 ccfddl（github.com/ccfddl/ccf-deadlines），
它的网站提供一份汇总好的 YAML。截稿时间统一换算成北京时间；时区写法认不出来的会议跳过，
宁可少登一条，也不把时间写错。
"""

from __future__ import annotations

import logging
import re
from datetime import datetime, timedelta
from typing import Any

import yaml

from .http import Http
from .textutil import clean_text

log = logging.getLogger(__name__)

URL = "https://ccfddl.com/conference/allconf.yml"
VIA = "CCFDDL"
# CCF 推荐目录的十个领域
SUBJECTS = {
    "AI": "人工智能",
    "CG": "图形学与多媒体",
    "HI": "人机交互与普适计算",
    "MX": "交叉/综合/新兴",
    "DB": "数据库/数据挖掘/内容检索",
    "NW": "计算机网络",
    "SE": "软件工程/系统软件/程序设计语言",
    "DS": "体系结构/并行与分布计算/存储系统",
    "SC": "网络与信息安全",
    "CT": "计算机科学理论",
}
_UTC = re.compile(r"UTC\s*([+-]\d{1,2})?", re.IGNORECASE)


def _offset(zone: str, moment: datetime) -> float | None:
    """时区写法 → 相对 UTC 的小时数；认不出来返回 None。"""
    zone = zone.strip().upper()
    if zone == "AOE":  # Anywhere on Earth，即 UTC-12
        return -12.0
    if match := _UTC.fullmatch(zone):
        return float(match.group(1) or 0)
    if zone in ("PST", "PDT"):
        return -8.0 if zone == "PST" else -7.0
    if zone == "PT":  # 美国太平洋时间：3 到 10 月按夏令时算（换季那几天可能差一小时）
        return -7.0 if 3 <= moment.month <= 10 else -8.0
    return None


def to_beijing(text: object, zone: str) -> datetime | None:
    """把“2026-10-25 23:59:59”这样的截稿时间按会议给的时区换成北京时间（不带时区信息）。"""
    try:
        moment = datetime.strptime(str(text).strip(), "%Y-%m-%d %H:%M:%S")
    except ValueError:  # 还没公布的写作 TBD
        return None
    offset = _offset(zone, moment)
    return None if offset is None else moment + timedelta(hours=8 - offset)


def _day(moment: datetime) -> str:
    return f"{moment.month}月{moment.day}日"


def entries(data: Any, now: datetime, settings: dict[str, Any]) -> list[dict[str, Any]]:
    """从 ccfddl 的数据里挑出 now（北京时间）之后 days 天内截稿的会议，按截稿时间排列。"""
    subjects = set(settings.get("subjects") or [])
    ranks = set(settings.get("ranks") or [])
    end = now + timedelta(days=int(settings.get("days", 45)))
    found: list[tuple[datetime, dict[str, Any]]] = []
    for conference in data if isinstance(data, list) else []:
        if not isinstance(conference, dict):
            continue
        subject, rank = conference.get("sub"), (conference.get("rank") or {}).get("ccf")
        if subject not in subjects or rank not in ranks:
            continue
        title = clean_text(conference.get("title"), 30)
        description = clean_text(conference.get("description"), 120)
        for edition in conference.get("confs") or []:
            if not isinstance(edition, dict):
                continue
            zone = str(edition.get("timezone") or "")
            for line in edition.get("timeline") or []:
                deadline = to_beijing(line.get("deadline"), zone) if isinstance(line, dict) else None
                if deadline is None or not now < deadline <= end:
                    continue
                name = f"{title} {edition.get('year', '')}".strip()
                comment = clean_text(line.get("comment"), 40)
                body = f"{description}（{name}，CCF-{rank} 类，{SUBJECTS.get(subject, subject)}）"
                body += f"{comment}的" if comment else ""
                body += f"论文提交截止时间为北京时间{_day(deadline)} {deadline:%H:%M}"
                abstract = to_beijing(line.get("abstract_deadline"), zone)
                if abstract and abstract < deadline:
                    body += f"，摘要截止时间为{_day(abstract)} {abstract:%H:%M}"
                held, place = clean_text(edition.get("date"), 40), clean_text(edition.get("place"), 60)
                if held and place:
                    body += f"。会议将于 {held} 在 {place} 举行"
                entry = {
                    "cat": "events",
                    "headline": f"{name} 论文截稿",
                    "when": _day(deadline),
                    "date": deadline.date().isoformat(),
                    "body": body + "。",
                    "url": clean_text(edition.get("link")),
                    "via": "会议官网",
                }
                found.append((deadline, entry))
    return [entry for _, entry in sorted(found, key=lambda pair: pair[0])]


def fetch(http: Http, now: datetime, settings: dict[str, Any]) -> list[dict[str, Any]]:
    data = yaml.safe_load(http.get_text(URL))
    if not isinstance(data, list):
        raise RuntimeError("ccfddl 返回的不是会议列表")
    return entries(data, now, settings)
