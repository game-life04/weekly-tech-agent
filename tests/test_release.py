"""每周快讯同步成 GitHub Release；RSS 订阅源。测试不访问网络。"""

from __future__ import annotations

import xml.dom.minidom
from types import SimpleNamespace

from test_render import kx_issue

from wta import release, render


class FakeGitHub:
    """按顺序记下请求；GET 返回预设的 Release（None 表示 404）。"""

    def __init__(self, existing=None):
        self.existing = existing
        self.calls = []

    def _reply(self, status, data=None):
        return SimpleNamespace(status_code=status, json=lambda: data, raise_for_status=lambda: None)

    def get(self, url, **kwargs):
        self.calls.append(("GET", url, None))
        return self._reply(404) if self.existing is None else self._reply(200, self.existing)

    def post(self, url, json=None, **kwargs):
        self.calls.append(("POST", url, json))
        return self._reply(201)

    def patch(self, url, json=None, **kwargs):
        self.calls.append(("PATCH", url, json))
        return self._reply(200)


def test_release_is_created_then_kept_in_sync(config):
    issue = kx_issue(number=1, title="阿里发布 Qwen4")
    github = FakeGitHub()
    assert release.sync(issue, config, "token", "owner/repo", github) == "created"
    method, url, sent = github.calls[-1]
    assert (method, url) == ("POST", "https://api.github.com/repos/owner/repo/releases")
    assert sent["tag_name"] == "2026-W41" and sent["name"] == "每周科技快讯 第 1 期 · 10.05–10.11：阿里发布 Qwen4"
    assert "https://github.com/game-life04/weekly-tech-agent/blob/main/weekly/2026-W41.md" in sent["body"]
    assert "](README.md)" not in sent["body"]  # Release 页面里相对链接会失效

    same = FakeGitHub({"id": 7, "name": sent["name"], "body": sent["body"]})
    assert release.sync(issue, config, "token", "owner/repo", same) == "unchanged"
    stale = FakeGitHub({"id": 7, "name": sent["name"], "body": "旧的"})
    assert release.sync(issue, config, "token", "owner/repo", stale) == "updated"
    assert stale.calls[-1][:2] == ("PATCH", "https://api.github.com/repos/owner/repo/releases/7")


def test_release_needs_a_token_and_an_issue(config):
    github = FakeGitHub()
    assert release.run([kx_issue()], config, {}, github) == 0 and github.calls == []
    assert release.run([], config, {"GITHUB_TOKEN": "t"}, github) == 0 and github.calls == []
    assert release.run([kx_issue()], config, {"GITHUB_TOKEN": "t", "GITHUB_REPOSITORY": "a/b"}, github) == 0
    assert github.calls[0][1] == "https://api.github.com/repos/a/b/releases/tags/2026-W41"


def test_feed_is_valid_atom_with_newest_first():
    daily = kx_issue(kind="daily", day="2026-10-12", start="2026-10-12", end="2026-10-12")
    weekly = kx_issue(number=1, title="阿里发布 Qwen4")
    feed = render.render_feed([weekly, daily])
    document = xml.dom.minidom.parseString(feed.encode("utf-8"))
    titles = [node.firstChild.data for node in document.getElementsByTagName("title")]
    assert titles == [
        "每周科技收集 Agent：AI 与开源快讯",
        "每日科技快讯 · 10.12",
        "每周科技快讯 第 1 期 · 10.05–10.11：阿里发布 Qwen4",
    ]
    content = document.getElementsByTagName("content")[1].firstChild.data
    assert '<a href="https://example.com/a%28b%29">阿里发布 Qwen4</a>：10月6日，支持长上下文。' in content
    assert "<script>" not in content  # 外部文字一律转义
    assert render.render_feed([]).count("<entry>") == 0
