"""网络层的测试：把 requests 的会话换成假的，检查重试、限流、大小和时间上限。"""

from __future__ import annotations

import pytest
import requests

from wta import http
from wta.http import Http, HttpError


class Raw:
    """假的响应：可以当上下文管理器用，按块给出响应体。"""

    def __init__(self, status=200, body=b"ok", headers=None, chunks=None):
        self.status_code = status
        self.headers = headers or {}
        self.url = "https://final.example/"
        self.encoding = None
        self._chunks = chunks if chunks is not None else [body]

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def iter_content(self, size):
        yield from self._chunks


@pytest.fixture
def client(monkeypatch):
    """返回 (Http, 回复队列, 调用记录)。队列里放 Raw 或异常。"""
    monkeypatch.setattr(http.time, "sleep", lambda seconds: None)
    client, replies, calls = Http(), [], []

    def fake_get(url, **kwargs):
        calls.append({"url": url, **kwargs})
        reply = replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        return reply

    monkeypatch.setattr(client.session, "get", fake_get)
    return client, replies, calls


def test_default_headers_never_carry_credentials():
    assert "Authorization" not in Http().session.headers  # 令牌只能逐个请求地加，否则会发给所有网站
    assert "weekly-tech-agent" in Http().session.headers["User-Agent"]


def test_transient_failures_are_retried(client):
    get, replies, calls = client
    replies += [requests.ConnectionError("reset"), Raw(503), Raw(200, b'{"a": 1}')]
    response = get.get("https://x.example/a", params={"q": 1})
    assert response.json() == {"a": 1} and response.text == '{"a": 1}' and response.url == "https://final.example/"
    assert len(calls) == 3 and calls[0]["params"] == {"q": 1} and calls[0]["stream"] is True

    replies += [Raw(502), Raw(502), Raw(502)]
    with pytest.raises(HttpError, match="HTTP 502") as error:
        get.get("https://x.example/a")
    assert error.value.status == 502


def test_client_errors_and_read_timeouts_are_not_retried(client):
    get, replies, calls = client
    replies += [Raw(404)]
    with pytest.raises(HttpError) as error:
        get.get("https://x.example/a")
    assert error.value.status == 404 and len(calls) == 1

    replies += [requests.ReadTimeout("slow")]
    with pytest.raises(HttpError, match="读取超时"):
        get.get("https://x.example/a")
    assert len(calls) == 2  # 连上了但不回数据：不重试


@pytest.mark.parametrize(
    ("status", "headers"),
    [
        (403, {"x-ratelimit-remaining": "0"}),
        (429, {"x-ratelimit-remaining": "0"}),
        (429, {"Retry-After": "600"}),  # 要等十分钟：不等了
        (403, {"Retry-After": "60"}),  # GitHub 的次级限流
    ],
)
def test_rate_limits_are_reported_without_retrying(client, status, headers):
    get, replies, calls = client
    replies += [Raw(status, headers=headers)]
    with pytest.raises(HttpError) as error:
        get.get("https://api.example/a")
    assert error.value.rate_limited and len(calls) == 1


def test_short_retry_after_is_honoured(client):
    get, replies, calls = client
    replies += [Raw(429, headers={"Retry-After": "3"}), Raw(200)]
    assert get.get("https://x.example/a").content == b"ok" and len(calls) == 2


def test_oversized_bodies_are_abandoned_while_reading(client, monkeypatch):
    get, replies, _ = client
    monkeypatch.setattr(http, "MAX_BYTES", 10)
    seen = []

    def chunks():
        for chunk in (b"12345", b"67890", b"abcde", b"never read"):
            seen.append(chunk)
            yield chunk

    replies += [Raw(200, chunks=chunks())]
    with pytest.raises(HttpError, match="超过"):
        get.get("https://x.example/big")
    assert seen == [b"12345", b"67890", b"abcde"]  # 超限后立刻停止，后面的不再读


def test_deadline_stops_requests(client, monkeypatch):
    get, replies, calls = client
    clock = [100.0]
    monkeypatch.setattr(http.time, "monotonic", lambda: clock[0])
    get.deadline = 130.0
    replies += [Raw(200)]
    get.get("https://x.example/a")
    assert calls[0]["timeout"] == (10, 30)

    clock[0] = 125.0
    replies += [Raw(200)]
    get.get("https://x.example/a")
    assert calls[1]["timeout"] == (5.0, 5.0)  # 只剩 5 秒：超时跟着压缩

    clock[0] = 131.0
    with pytest.raises(HttpError, match="时间上限"):
        get.get("https://x.example/a")
    assert len(calls) == 2  # 过了时间上限就不再发请求
