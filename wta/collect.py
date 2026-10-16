"""依次运行所有启用的来源。一个来源出错或太慢都不影响其他来源，结果记进报告里。"""

from __future__ import annotations

import json
import logging
import math
import time
from typing import Any

from .dates import to_iso
from .dedupe import item_id
from .models import SECTIONS, Item
from .render import md_url
from .sources import SOURCES
from .sources.base import Context
from .textutil import clean_text

log = logging.getLogger(__name__)

UNIT_SECONDS = 90.0  # 一个抓取单元（一个来源，或 RSS 的一个订阅）默认最多用这么久
TOTAL_SECONDS = 12 * 60.0  # 全部来源合计的上限；超过后剩下的单元直接记为失败


def _tidy(item: Item, name: str, title: str) -> Item | None:
    """统一清洗来源返回的内容，把各字段规范成后面流程要求的类型；不合格的丢掉并说明原因。"""
    item.title = clean_text(item.title, 300)
    item.summary = clean_text(item.summary, 1500 if item.section == "papers" else 600)  # 论文要写问题、方法、结果
    item.url = clean_text(item.url)
    problem = ""
    if not item.title:
        problem = "标题为空"
    elif not md_url(item.url):
        problem = "链接不是 http(s) 地址"
    elif item.section not in SECTIONS:
        problem = f"栏目 {item.section!r} 不是 {'/'.join(SECTIONS)} 之一"
    if problem:
        log.info("%s 丢弃一条内容（%s）：%s", title, problem, (item.title or item.url)[:60])
        return None
    item.source = name
    item.via = clean_text(item.via, 40) or title
    item.heat = round(min(max(float(item.heat), 0.0), 1.0), 3)
    item.weight = round(min(max(float(item.weight), 0.0), 1.0), 3)
    item.published = to_iso(item.published)
    item.metrics = {
        str(key): float(value)
        for key, value in (item.metrics or {}).items()
        if isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
    }
    item.extra = item.extra if isinstance(item.extra, dict) else {}
    item.tags = [clean_text(tag, 12) for tag in item.tags if tag] if isinstance(item.tags, list) else []
    item.also_in = []
    item.id = item_id(item.url)
    json.dumps(item.to_dict())  # extra 里放了存不成 JSON 的东西：让这个来源报错，而不是到保存时才崩
    return item


def _units(name: str, module: Any, source_config: dict[str, Any]) -> list[tuple[str, str, dict[str, Any]]]:
    """一个来源可以拆成几个“单元”分别抓取（例如 RSS 的每个订阅），各自记录成败。

    返回 [(单元名, 显示名, 这个单元的配置)]；不拆的来源只有一个单元。
    """
    if hasattr(module, "expand"):
        return module.expand(source_config)
    return [(name, module.TITLE, source_config)]


def collect(
    config: dict[str, Any], ctx: Context, only: list[str] | None = None
) -> tuple[list[Item], list[dict[str, Any]]]:
    """返回（所有来源抓到的内容，每个单元的运行报告）。

    only 不为空时只跑指定的来源；可以写来源名（rss），也可以写单元名（rss:量子位）。
    """
    items: list[Item] = []
    report: list[dict[str, Any]] = []
    stop_at = time.monotonic() + TOTAL_SECONDS
    for name, module in SOURCES.items():
        source_config = config["sources"].get(name) or {}
        wanted = [o for o in only or [] if o.split(":")[0] == name]
        if (only and not wanted) or (not only and not source_config.get("enabled", False)):
            continue
        try:
            units = _units(name, module, source_config)
        except Exception as exc:  # 配置写错（例如订阅漏了 name）只影响这一个来源
            units = []
            report.append(_entry(name, module.TITLE, module.TITLE, error=f"配置有误：{type(exc).__name__}: {exc}"))
            log.warning("%s 的配置有误，跳过：%s", module.TITLE, exc)
        for unit, title, unit_config in units:
            if only and unit not in wanted and name not in wanted:
                continue
            entry = _entry(unit, title, module.TITLE)
            started = time.monotonic()
            try:
                budget = float(unit_config.get("max_seconds", getattr(module, "MAX_SECONDS", UNIT_SECONDS)))
                ctx.http.deadline = min(started + budget, stop_at)
                found = []
                for raw in module.fetch(unit_config, ctx):
                    try:
                        tidy = _tidy(raw, name, title)
                    except Exception as exc:  # 一条内容有问题（例如链接写坏了）只丢这一条
                        log.info("%s 丢弃一条内容（%s: %s）", title, type(exc).__name__, exc)
                        continue
                    if tidy:
                        found.append(tidy)
                items.extend(found)
                entry["count"] = len(found)
                log.info("%s：%d 条", title, len(found))
            except Exception as exc:  # 任何来源的任何错误都不能中断整个任务
                entry["ok"] = False
                entry["error"] = clean_text(f"{type(exc).__name__}: {exc}", 300)
                log.warning("%s 抓取失败：%s", title, entry["error"])
            finally:
                ctx.http.deadline = None
            entry["seconds"] = round(time.monotonic() - started, 1)
            report.append(entry)
    return items, report


def _entry(name: str, title: str, group: str, error: str = "") -> dict[str, Any]:
    return {
        "name": name,
        "title": title,
        "group": group,
        "ok": not error,
        "count": 0,
        "error": clean_text(error, 300),
        "seconds": 0.0,
    }
