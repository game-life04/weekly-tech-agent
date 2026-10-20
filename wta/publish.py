"""把 data/ 里的数据写成仓库里的页面：日报、每周快讯（Markdown 和公众号排版版 HTML）、目录和 README。"""

from __future__ import annotations

import json
import logging
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from . import render, store

log = logging.getLogger(__name__)

README_SKELETON = "# 每周科技收集 Agent\n\n" + render.LATEST_START + "\n" + render.LATEST_END + "\n"


def _write(path: Path, text: str) -> None:
    if store.write_file(path, text):
        log.info("写入 %s", path.as_posix())


def week_note_path(root: Path, week: str) -> Path:
    return root / "data" / "weekly" / f"{week}.json"


def load_week_note(root: Path, week: str) -> dict[str, Any]:
    """一周的记录（目前只有这一周的快讯，键名 kuaixun）。"""
    path = week_note_path(root, week)
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}


def save_week_note(root: Path, week: str, note: dict[str, Any]) -> None:
    _write(week_note_path(root, week), json.dumps(note, ensure_ascii=False, indent=1) + "\n")


def week_payloads(root: Path, monday: date) -> dict[date, dict[str, Any]]:
    """这一周里已有数据的各天。"""
    found = {}
    for offset in range(7):
        day = monday + timedelta(days=offset)
        payload = store.load_day(root, day)
        if payload is not None:
            found[day] = payload
    return found


def publish_day(root: Path, config: dict[str, Any], day: date, days: list[date]) -> None:
    payload = store.load_day(root, day)
    if payload is None:
        return
    earlier = [d for d in days if d < day]
    text = render.render_daily(day, payload, config, earlier[-1] if earlier else None)
    _write(root / render.daily_path(day), text)
    if isinstance(payload.get("kuaixun"), dict):
        publish_kuaixun(root, config, payload["kuaixun"])


def kuaixun_issues(root: Path) -> list[dict[str, Any]]:
    """已经生成的所有每周快讯，从早到晚。"""
    issues = []
    for path in sorted((root / "data" / "weekly").glob("*.json")):
        issue = json.loads(path.read_text(encoding="utf-8")).get("kuaixun")
        if isinstance(issue, dict) and issue.get("week") == path.stem:
            issues.append(issue)
    return sorted(issues, key=lambda issue: issue["start"])


def publish_kuaixun(root: Path, config: dict[str, Any], issue: dict[str, Any]) -> None:
    """写一期快讯（每周或每日）的两个文件：Markdown 页面和公众号排版版。"""
    page, sheet = render.kuaixun_paths(issue)
    _write(root / page, render.render_kuaixun(issue, config))
    _write(root / sheet, render.render_kuaixun_html(issue, config))


def publish_indexes(root: Path, config: dict[str, Any], days: list[date]) -> list[str]:
    """写两个目录页和 README 里的“最新一期”。返回需要提醒维护者的问题（没有就是空列表）。"""
    payloads = {day: store.load_day(root, day) or {} for day in days}
    counts = [(day, len(p.get("items", [])), isinstance(p.get("kuaixun"), dict)) for day, p in payloads.items()]
    _write(root / "daily" / "README.md", render.render_daily_index(counts))
    issues = kuaixun_issues(root)
    _write(root / "weekly" / "README.md", render.render_weekly_index(issues))

    if not days and not issues:
        return []
    latest = days[-1] if days else None  # README 顶部永远显示最新一期快讯和最新一期日报
    readme = root / "README.md"
    current = readme.read_text(encoding="utf-8") if readme.is_file() else README_SKELETON
    payload = payloads.get(latest, {}) if latest else {}
    block = render.render_latest_block(latest, payload, config, issues[-1] if issues else None)
    try:
        _write(readme, render.replace_latest_block(current, block))
    except ValueError as exc:  # 标记被改坏了：宁可不更新首页，也不要乱删乱加
        return [f"README.md 没有更新：{exc}"]
    return []


def publish(root: Path, config: dict[str, Any], day: date) -> list[str]:
    """生成 day 这一天受影响的页面：当天日报、目录和 README。返回需要提醒的问题。"""
    days = store.list_days(root)
    publish_day(root, config, day, days)
    return publish_indexes(root, config, days)


def publish_all(root: Path, config: dict[str, Any]) -> list[str]:
    """用已有数据重新生成所有页面（改了排版以后用）。"""
    days = store.list_days(root)
    for day in days:
        publish_day(root, config, day, days)
    for issue in kuaixun_issues(root):
        publish_kuaixun(root, config, issue)
    return publish_indexes(root, config, days)
