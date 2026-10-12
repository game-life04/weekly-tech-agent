"""来源登记表。新增来源：在本目录加一个文件，然后在这里登记。约定见 base.py。"""

from __future__ import annotations

from types import ModuleType

from . import github_new, github_releases, github_trending, hackernews, hot_models, papers, qbitai, rss

SOURCES: dict[str, ModuleType] = {
    module.NAME: module
    for module in (hackernews, rss, qbitai, github_trending, github_new, github_releases, hot_models, papers)
}
