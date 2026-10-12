"""检查仓库里真正的 config.yaml 和 README.md。

改配置是最常见的贡献方式，写错一行（订阅漏了 name、正则少个括号）会让每天的任务出问题，
所以在这里把能提前发现的错误都拦下来。
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from wta import render
from wta.config import load_config
from wta.llm import build_client
from wta.models import SECTIONS
from wta.sources import SOURCES
from wta.textutil import KeywordMatcher

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="module")
def real():
    return load_config(ROOT / "config.yaml")


def test_top_level_sections_have_the_right_shape(real):
    for name in ("sections", "select", "dedupe", "keywords", "sources", "llm"):
        assert isinstance(real[name], dict), f"{name} 必须是键值对"
    for section in SECTIONS:
        assert isinstance(real["sections"][section]["daily"], int)
        assert isinstance(real["sections"][section]["weekly"], int)
        assert real["sections"][section]["title"]
    assert isinstance(real["select"]["per_source_cap"], int)
    assert all(isinstance(cap, int) for cap in real["select"]["caps"].values())
    assert isinstance(real["dedupe"]["remember_days"], int)
    assert isinstance(real["utc_offset_hours"], (int, float))
    assert set(real["sources"]) <= set(SOURCES), "sources 下有代码里不存在的来源名"


def test_keywords_compile_and_behave(real):
    matcher = KeywordMatcher(real["keywords"])  # 正则写错会在这里报出是哪一条
    assert matcher.match("OpenAI releases a new LLM") and matcher.match("国产大模型发布")
    assert not matcher.match("He said he would maintain the garage")
    assert not matcher.match("Claude Shannon and information theory")


def test_every_source_expands_and_feeds_are_well_formed(real):
    for name, module in SOURCES.items():
        if hasattr(module, "expand"):
            assert module.expand(real["sources"].get(name) or {}), f"{name} 展开后没有任何单元"
    feeds = real["sources"]["rss"]["feeds"]
    names = [feed["name"] for feed in feeds]  # 漏了 name 会在这里报 KeyError
    assert len(names) == len(set(names)), "订阅的 name 不能重复"
    for feed in feeds:
        assert feed["url"].startswith("https://"), feed["name"]
        assert feed.get("section", "news") in SECTIONS, feed["name"]
        assert 0 <= feed.get("weight", 0.5) <= 1, feed["name"]
        if "title_match" in feed:
            re.compile(feed["title_match"])


def test_watched_repositories_and_paper_themes(real):
    for entry in real["sources"]["github_releases"]["repos"]:
        entry = {"repo": entry} if isinstance(entry, str) else entry
        assert re.fullmatch(r"[\w.-]+/[\w.-]+", entry["repo"]), entry
        re.compile(entry.get("tag_regex", ""))
    for theme in real["sources"]["papers"]["themes"].values():
        assert theme["title"] and theme["phrases"]


def test_llm_providers_are_usable(real):
    assert build_client(real, {}) is None
    for provider in real["llm"]["providers"]:
        client = build_client(real, {provider["key_env"]: "k"})
        assert client is not None, (
            f"{provider['name']} 的配置不会被采用（密钥变量名要以 _API_KEY 结尾，地址要是 https）"
        )
        assert client.providers[0].name == provider["name"]


def test_readme_markers_are_intact():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert readme.count(render.LATEST_START) == 1 and readme.count(render.LATEST_END) == 1
    assert readme.index(render.LATEST_START) < readme.index(render.LATEST_END)
