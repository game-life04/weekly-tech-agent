"""读写 data/ 目录。

每天一个 JSON 文件（data/年/日期.json），日报、周报和 README 都只从这些文件生成，
所以随时可以用 `python -m wta render` 重新排版，不需要重新抓取。
"""

from __future__ import annotations

import json
import re
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from .models import Item

_DAY_FILE = re.compile(r"\d{4}-\d{2}-\d{2}")


def write_file(path: Path, text: str) -> bool:
    """写文件，返回内容是否有变化（没变就不写）。

    先写到临时文件再改名，中途出错不会留下半个文件；遇到存不了的字符
    （例如孤立的代理字符）用问号代替，而不是让整次运行崩掉。
    """
    data = text.encode("utf-8", errors="replace")
    if path.is_file() and path.read_bytes() == data:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(data)
    temporary.replace(path)
    return True


def day_path(root: Path, day: date) -> Path:
    return root / "data" / f"{day:%Y}" / f"{day.isoformat()}.json"


def load_day(root: Path, day: date) -> dict[str, Any] | None:
    path = day_path(root, day)
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def save_day(root: Path, day: date, payload: dict[str, Any]) -> Path:
    path = day_path(root, day)
    write_file(path, json.dumps(payload, ensure_ascii=False, indent=1) + "\n")
    return path


def list_days(root: Path) -> list[date]:
    """已有数据的所有日期，从早到晚。文件名不是日期的会被忽略。"""
    days: list[date] = []
    for path in (root / "data").glob("[0-9][0-9][0-9][0-9]/*.json"):
        # 先用正则卡格式：date.fromisoformat 也接受 2026-W41 这种周写法，不能直接交给它判断
        if _DAY_FILE.fullmatch(path.stem):
            try:
                days.append(date.fromisoformat(path.stem))
            except ValueError:
                continue
    return sorted(days)


def items_of(payload: dict[str, Any] | None) -> list[Item]:
    return [Item.from_dict(d) for d in (payload or {}).get("items", [])]


def published_ids(root: Path, before: date, days: int) -> set[str]:
    """before 之前 days 天内已经登过的内容 id（含被合并掉的那几份），用来避免内容重复出现。"""
    seen: set[str] = set()
    for offset in range(1, days + 1):
        for item in items_of(load_day(root, before - timedelta(days=offset))):
            seen.update([item.id, *item.merged_ids])
    return seen
