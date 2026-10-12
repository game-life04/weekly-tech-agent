"""数据模型：收集到的每一条内容都是一个 Item。"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, fields
from typing import Any

# 三个栏目的内部名字；显示用的中文标题写在 config.yaml 里
SECTIONS = ("news", "opensource", "papers")


@dataclass
class Item:
    title: str
    url: str
    source: str  # 来源的内部名，例如 "hackernews"
    section: str  # news / opensource / papers
    via: str = ""  # 显示给读者看的来源名，例如 "Hacker News"、"OpenAI"
    published: str = ""  # 发布时间，ISO 8601（UTC）；拿不到就留空
    summary: str = ""  # 来源自带的简介，可能是英文
    heat: float = 0.0  # 热度 0~1，由各来源按自己的指标换算
    weight: float = 0.5  # 来源的重要程度 0~1，来自配置
    metrics: dict[str, float] = field(default_factory=dict)  # 原始指标：points、stars、upvotes……
    extra: dict[str, Any] = field(default_factory=dict)  # 其他信息：讨论链接、编程语言……
    id: str = ""  # 规范化链接的哈希，去重用
    score: float = 0.0  # 综合分 0~10
    title_zh: str = ""  # 中文标题和摘要由大模型填写；没有大模型时为空
    summary_zh: str = ""
    tags: list[str] = field(default_factory=list)
    also_in: list[str] = field(default_factory=list)  # 同一条内容还出现在哪些来源
    merged_ids: list[str] = field(default_factory=list)  # 合并进来的其他几份的 id，跨天去重用

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Item:
        known = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in data.items() if k in known})
