"""把 data/ 里的数据写成仓库里的 Markdown 文件。"""

from __future__ import annotations

import json
import logging
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from . import render, store
from .dates import week_id, week_range

log = logging.getLogger(__name__)

README_SKELETON = "# 每周科技收集 Agent\n\n" + render.LATEST_START + "\n" + render.LATEST_END + "\n"


def _write(path: Path, text: str) -> None:
    if store.write_file(path, text):
        log.info("写入 %s", path.as_posix())


def week_note_path(root: Path, week: str) -> Path:
    return root / "data" / "weekly" / f"{week}.json"


def load_week_note(root: Path, week: str) -> dict[str, Any]:
    """周报的附加信息（目前只有大模型写的“本周看点”）。"""
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


def publish_week(root: Path, config: dict[str, Any], monday: date, today: date) -> None:
    payloads = week_payloads(root, monday)
    if not payloads:
        return
    overview = load_week_note(root, week_id(monday)).get("overview", "")
    text = render.render_weekly(monday, payloads, config, today, overview)
    _write(root / render.weekly_path(week_id(monday)), text)


def publish_indexes(root: Path, config: dict[str, Any], days: list[date]) -> list[str]:
    """写两个目录页和 README 里的“最新一期”。返回需要提醒维护者的问题（没有就是空列表）。"""
    counts = [(day, len((store.load_day(root, day) or {}).get("items", []))) for day in days]
    _write(root / "daily" / "README.md", render.render_daily_index(counts))
    weeks: dict[date, int] = {}
    for day, count in counts:
        monday = week_range(day)[0]
        weeks[monday] = weeks.get(monday, 0) + count
    _write(root / "weekly" / "README.md", render.render_weekly_index(list(weeks.items())))

    if not days:
        return []
    latest = days[-1]  # README 顶部永远显示最新一期
    readme = root / "README.md"
    current = readme.read_text(encoding="utf-8") if readme.is_file() else README_SKELETON
    block = render.render_latest_block(latest, store.load_day(root, latest) or {}, config)
    try:
        _write(readme, render.replace_latest_block(current, block))
    except ValueError as exc:  # 标记被改坏了：宁可不更新首页，也不要乱删乱加
        return [f"README.md 没有更新：{exc}"]
    return []


def publish(root: Path, config: dict[str, Any], day: date, today: date) -> list[str]:
    """生成 day 这一天受影响的页面：当天日报、周报、目录和 README。返回需要提醒的问题。"""
    days = store.list_days(root)
    publish_day(root, config, day, days)
    monday = week_range(day)[0]
    # 上一周也重排一次：周日那天没跑成的话，它会一直停在“本周还没结束”
    for week in (monday - timedelta(days=7), monday):
        publish_week(root, config, week, today)
    return publish_indexes(root, config, days)


def publish_all(root: Path, config: dict[str, Any], today: date) -> list[str]:
    """用已有数据重新生成所有页面（改了排版以后用）。"""
    days = store.list_days(root)
    for day in days:
        publish_day(root, config, day, days)
    for monday in sorted({week_range(day)[0] for day in days}):
        publish_week(root, config, monday, today)
    return publish_indexes(root, config, days)
