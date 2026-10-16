"""测试用的假网络：按网址前缀返回预设内容，不发真实请求。"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from types import SimpleNamespace
from typing import Any

from wta.http import HttpError
from wta.sources.base import Context
from wta.textutil import KeywordMatcher

NOW = datetime(2026, 10, 11, 12, 0, tzinfo=UTC)
KEYWORDS = {"exact": ["AI", "LLMs?", "RAG"], "any_case": ["agents?", "language models?", "大模型", "openai"]}


class FakeResponse:
    def __init__(self, url: str, body: Any):
        self.url = url
        self.status_code = 200
        if isinstance(body, bytes):
            self.content = body
        elif isinstance(body, str):
            self.content = body.encode("utf-8")
        else:
            self.content = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.text = self.content.decode("utf-8", errors="replace")

    def json(self):
        return json.loads(self.text)


class FakeHttp:
    """routes: {网址前缀: 内容}。内容可以是字节、字符串、可转成 JSON 的对象、异常，或接收 (url, params) 的函数。"""

    def __init__(self, routes: dict[str, Any]):
        self.routes = routes
        self.deadline = None
        self.calls: list[dict[str, Any]] = []

    def get(self, url, *, params=None, headers=None, timeout=None, retries=None, max_seconds=None):
        self.calls.append({"url": url, "params": params or {}, "headers": headers or {}})
        for prefix in sorted(self.routes, key=len, reverse=True):  # 最长的前缀优先
            if url.startswith(prefix):
                body = self.routes[prefix]
                if callable(body):
                    body = body(url, params or {})
                if isinstance(body, Exception):
                    raise body
                return FakeResponse(url, body)
        raise HttpError(f"HTTP 404：{url}", 404)

    def get_json(self, url, **kwargs):
        return self.get(url, **kwargs).json()

    def get_text(self, url, **kwargs):
        return self.get(url, **kwargs).text


def context(routes: dict[str, Any], env: dict[str, str] | None = None, now: datetime = NOW) -> Context:
    return Context(http=FakeHttp(routes), now=now, keywords=KeywordMatcher(KEYWORDS), env=env or {})


class FakeClient:
    """按顺序给出预设回复的假大模型；回复可以是字典、字符串、异常，或一个根据输入生成回复的函数。"""

    def __init__(self, replies, max_requests=20):
        self.replies = list(replies)
        self.calls: list[dict] = []
        self.systems: list[str] = []  # 每次请求用的系统提示词
        self.max_requests = max_requests
        self.provider = SimpleNamespace(name="假服务", model="fake-1")

    @property
    def requests_made(self):
        return len(self.calls)

    @property
    def answered(self):
        return [SimpleNamespace(name="假服务", model="fake-1")] if self.calls else []

    @property
    def exhausted(self):
        return len(self.calls) >= self.max_requests

    def chat(self, system, user, max_tokens):
        sent = json.loads(user)
        self.calls.append(sent)
        self.systems.append(system)
        reply = self.replies[0] if callable(self.replies[0]) else self.replies.pop(0)
        if callable(reply):
            reply = reply(sent)
        if isinstance(reply, Exception):
            raise reply
        return reply if isinstance(reply, str) else json.dumps(reply, ensure_ascii=False)
