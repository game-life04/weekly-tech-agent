"""来源的约定。

每个来源是 wta/sources/ 下的一个文件，只需要提供三样东西：

    NAME = "hackernews"       # 内部名，和 config.yaml 里 sources 下的键一致
    TITLE = "Hacker News"     # 显示给读者看的名字
    def fetch(config, ctx) -> list[Item]: ...

fetch 拿到的 config 是 config.yaml 里这个来源自己的那一段，ctx 是下面的 Context。
抓取失败直接抛异常就行，调度器会记录下来并继续跑其他来源。

fetch 返回的 Item 至少要填 title、url、source、section，其中：
- section 只能是 news、opensource、papers 之一；
- published 用 dates.to_iso(...) 转成字符串，拿不到发布时间就留空（不要拿抓取时间冒充）；
- metrics 的值必须是数字，页面认识的名字见 render.py 的 _METRIC_LABELS；
- extra 里只放能存成 JSON 的东西（字符串、数字、列表、字典）。
可选的模块级常量 MAX_SECONDS 是这个来源最多能用多少秒（默认 90）。
写好后在 wta/sources/__init__.py 里登记一下。
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime

from ..http import Http
from ..textutil import KeywordMatcher


@dataclass
class Context:
    http: Http  # 发请求用，自带重试和超时
    now: datetime  # 当前时间（UTC，带时区）
    keywords: KeywordMatcher  # 判断内容是否和 AI / 大模型相关
    env: Mapping[str, str]  # 环境变量，例如 GITHUB_TOKEN
