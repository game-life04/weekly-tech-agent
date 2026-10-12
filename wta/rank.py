"""打分和选稿。

综合分（0~10）由热度、来源权重、新鲜度三部分加权得到；如果大模型也给了评分，
再和它按比例合成。选稿时每个栏目有名额，同一来源在一个栏目里的条数有上限，
避免某一个来源刷屏。
"""

from __future__ import annotations

from collections import Counter
from datetime import datetime

from .dates import parse_time
from .models import SECTIONS, Item

HEAT_SHARE, WEIGHT_SHARE, FRESH_SHARE = 0.5, 0.3, 0.2
HALF_LIFE_HOURS = 48.0  # 发布 48 小时后，新鲜度减半
LLM_SHARE = 0.6  # 大模型打了分的内容：最终分里大模型占六成，规则分占四成


def freshness(published: str, now: datetime) -> float:
    """新鲜度 0~1；不知道发布时间的给中间值。"""
    moment = parse_time(published)
    if moment is None:
        return 0.5
    age_hours = max(0.0, (now - moment).total_seconds() / 3600)
    return 0.5 ** (age_hours / HALF_LIFE_HOURS)


def heuristic_score(item: Item, now: datetime) -> float:
    heat = min(max(item.heat, 0.0), 1.0)
    weight = min(max(item.weight, 0.0), 1.0)
    return 10 * (HEAT_SHARE * heat + WEIGHT_SHARE * weight + FRESH_SHARE * freshness(item.published, now))


def apply_scores(items: list[Item], now: datetime) -> None:
    """给每条内容算综合分，写进 item.score。"""
    for item in items:
        score = heuristic_score(item, now)
        llm_score = item.extra.get("llm_score")
        if isinstance(llm_score, (int, float)) and not isinstance(llm_score, bool):
            score = (1 - LLM_SHARE) * score + LLM_SHARE * min(max(float(llm_score), 0.0), 10.0)
        item.score = round(score, 2)


def select(
    items: list[Item], quotas: dict[str, int], per_source_cap: int, caps: dict[str, int] | None = None
) -> list[Item]:
    """按栏目名额挑出入选内容。返回结果按栏目顺序排列，栏目内按综合分从高到低。

    per_source_cap 是同一来源在一个栏目里的条数上限；caps 可以给个别来源（按显示名）单独设上限。
    """
    caps = caps or {}
    chosen: list[Item] = []
    for section in SECTIONS:
        quota = quotas.get(section, 0)
        used: Counter[str] = Counter()
        picked = 0
        pool = sorted((i for i in items if i.section == section), key=lambda i: i.score, reverse=True)
        for item in pool:
            if picked >= quota:
                break
            origin = item.via or item.source
            if used[origin] >= caps.get(origin, per_source_cap):
                continue
            used[origin] += 1
            picked += 1
            chosen.append(item)
    return chosen
