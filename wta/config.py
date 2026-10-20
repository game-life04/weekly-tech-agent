"""读取 config.yaml，没写的项用默认值补齐。"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import yaml

DEFAULTS: dict[str, Any] = {
    "utc_offset_hours": 8,  # 日期按北京时间算
    "sections": {
        "news": {"title": "AI 动态", "emoji": "🗞️", "daily": 8, "weekly": 12},
        "opensource": {"title": "开源圈", "emoji": "🛠️", "daily": 8, "weekly": 12},
        "papers": {"title": "前沿论文", "emoji": "📄", "daily": 5, "weekly": 10},
    },
    "select": {"per_source_cap": 2, "caps": {}},
    "dedupe": {"remember_days": 120, "title_similarity": 0.92},
    "keywords": {"exact": [], "any_case": [], "exclude": [], "domains": []},
    "sources": {},
    "kuaixun": {
        "enabled": True,
        "candidates": {"news": 30, "opensource": 20, "papers": 8},
        "chinese_news": 12,
        "caps": {
            "club": 5,
            "policy": 3,
            "domestic": 6,
            "overseas": 6,
            "opensource": 4,
            "papers": 3,
            "industry": 3,
            "events": 5,
        },
        "club": {
            "name": "俱乐部",
            "org": "hust-open-atom-club",
            "dashboard": "https://osd.openatom.club",
            "exclude": [],
            "top_repos": 3,
            "release_repos": 8,
        },
        "policy": {"keywords": [], "exclude": []},
        "companies": {"domestic": [], "overseas": []},
        "sites": {"domestic": [], "overseas": []},
        "events": {"subjects": ["AI"], "ranks": ["A", "B"], "days": 45},
        "daily": {
            "enabled": True,
            "event_days": 14,
            "caps": {
                "club": 3,
                "policy": 2,
                "domestic": 5,
                "overseas": 5,
                "opensource": 4,
                "papers": 3,
                "industry": 2,
                "events": 3,
            },
        },
    },
    "llm": {
        "enabled": True,
        "max_requests": 30,
        "max_seconds": 480,
        "max_candidates": 150,
        "review_min_score": 7,
        "drop_filtered": True,
        "providers": [],
    },
}


def _merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """递归合并：override 里写了的覆盖 base，没写的保留默认值。"""
    for key, value in override.items():
        if value is None and isinstance(base.get(key), dict):
            continue  # 只写了键名、下面留空：当作没写，沿用默认值
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            _merge(base[key], value)
        else:
            base[key] = value
    return base


def load_config(path: Path) -> dict[str, Any]:
    config = copy.deepcopy(DEFAULTS)
    if path.is_file():
        loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(loaded, dict):
            raise ValueError(f"{path} 的最外层必须是键值对")
        _merge(config, loaded)
    return config
