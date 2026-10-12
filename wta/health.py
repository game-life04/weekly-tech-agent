"""运行情况：哪些来源连续出问题，以及写给 GitHub Actions 运行页面的小结。"""

from __future__ import annotations

from collections.abc import Mapping
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from . import store
from .render import md_escape


def failing_sources(root: Path, day: date, report: list[dict[str, Any]], days: int = 3) -> list[str]:
    """连续 days 天都抓取失败的来源（显示名）。偶尔失败一次很正常，连续失败才值得去看。"""
    failing = {entry["name"]: entry["title"] for entry in report if not entry["ok"]}
    for offset in range(1, days):
        earlier = store.load_day(root, day - timedelta(days=offset))
        if earlier is None:
            return []  # 历史不够长，没法判断
        failed_then = {entry["name"] for entry in earlier.get("sources", []) if not entry.get("ok")}
        failing = {name: title for name, title in failing.items() if name in failed_then}
    return sorted(failing.values())


def step_summary(env: Mapping[str, str], day: date, payload: dict[str, Any], warnings: list[str]) -> None:
    """在 GitHub Actions 的运行页面上留一份小结；不在 Actions 里运行时什么都不做。"""
    path = env.get("GITHUB_STEP_SUMMARY")
    if not path:
        return
    sources = payload.get("sources", [])
    failed = [entry for entry in sources if not entry["ok"]]
    llm = payload.get("llm") or {}
    lines = [
        f"## {day.isoformat()} 日报",
        "",
        f"- 入选 {len(payload.get('items', []))} 条，候选 {payload.get('candidates', 0)} 条",
        f"- 来源：{len(sources) - len(failed)} 个成功，{len(failed)} 个失败",
        f"- 大模型：{llm.get('provider', '')} {llm.get('model', '')}".rstrip() if llm else "- 大模型：未使用",
    ]
    lines += [f"- ⚠️ {md_escape(warning)}" for warning in warnings]
    if failed:
        lines += ["", "| 失败的来源 | 原因 |", "| --- | --- |"]
        for entry in failed:  # 报错原文放进行内代码，里面的网址和排版符号都不会被渲染
            error = entry["error"].replace("`", "'").replace("|", "/")
            lines.append(f"| {md_escape(entry['title'])} | `{error}` |")
    with open(path, "a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")
