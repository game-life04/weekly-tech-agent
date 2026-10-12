from __future__ import annotations

import pytest

from wta import llm
from wta.llm import Filtered, LLMClient, LLMError, Provider, build_client


class FakeResponse:
    def __init__(self, status=200, content="ok", finish="stop", text="", headers=None, refusal=None):
        self.status_code = status
        self.headers = headers or {}
        self._payload = {"choices": [{"message": {"content": content, "refusal": refusal}, "finish_reason": finish}]}
        self.text = text or str(self._payload)

    def json(self):
        return self._payload


@pytest.fixture
def post(monkeypatch):
    """把网络请求换成预设的回复，并记录每次发出的请求。"""
    state = {"replies": [], "calls": []}

    def fake_post(url, headers, json, timeout):
        state["calls"].append({"url": url, "headers": headers, "body": json})
        reply = state["replies"].pop(0)
        if isinstance(reply, Exception):
            raise reply
        return reply

    monkeypatch.setattr(llm.requests, "post", fake_post)
    monkeypatch.setattr(llm.time, "sleep", lambda seconds: None)
    return state


def provider(name="A", **kwargs):
    return Provider(
        name=name,
        base_url=f"https://{name.lower()}.example/v1/",
        api_key=f"key-{name}",
        model="m",
        interval=0,
        **kwargs,
    )


def test_build_client_picks_configured_providers_in_order(config):
    config["llm"]["providers"] = [
        {
            "name": "一",
            "key_env": "ONE_API_KEY",
            "base_url": "https://one.example/v1",
            "model": "m1",
            "json_mode": True,
            "extra": {"thinking": {"type": "disabled"}},
            "interval": 3,
        },
        {"name": "二", "key_env": "TWO_API_KEY", "base_url": "https://two.example/v1", "model": "m2"},
    ]
    assert build_client(config, {}) is None
    assert build_client(config, {"ONE_API_KEY": ""}) is None  # 没设置的密钥在 Actions 里是空字符串
    only_two = build_client(config, {"TWO_API_KEY": "k2"})
    assert [p.name for p in only_two.providers] == ["二"]
    everything = build_client(
        config,
        {
            "ONE_API_KEY": "k1",
            "TWO_API_KEY": "k2",
            "LLM_API_KEY": "k0",
            "LLM_BASE_URL": "https://own.example/v1",
            "LLM_MODEL": "m0",
        },
    )
    assert [p.name for p in everything.providers] == ["自定义服务", "一", "二"]
    assert everything.providers[1].json_mode and everything.providers[1].extra == {"thinking": {"type": "disabled"}}
    assert everything.max_requests == 30


def test_chat_sends_an_openai_style_request(post):
    post["replies"] = [FakeResponse(content="<think>想一想</think>\n答案")]
    client = LLMClient([provider(json_mode=True, extra={"thinking": {"type": "disabled"}})])
    assert client.chat("系统", "用户", max_tokens=100) == "答案"
    call = post["calls"][0]
    assert call["url"] == "https://a.example/v1/chat/completions"
    assert call["headers"]["Authorization"] == "Bearer key-A"
    assert call["body"]["messages"] == [{"role": "system", "content": "系统"}, {"role": "user", "content": "用户"}]
    assert call["body"]["response_format"] == {"type": "json_object"} and call["body"]["thinking"] == {
        "type": "disabled"
    }
    assert call["body"]["max_tokens"] == 100 and client.requests_made == 1


def test_broken_provider_is_dropped_and_the_next_one_takes_over(post):
    post["replies"] = [FakeResponse(status=401, text="invalid api key"), FakeResponse(content="来自 B")]
    client = LLMClient([provider("A"), provider("B")])
    assert client.chat("s", "u", 50) == "来自 B"
    assert client.providers[0].down and client.provider.name == "B"

    post["replies"] = [FakeResponse(status=429, text='{"error":{"code":"1113","message":"余额不足"}}')]
    alone = LLMClient([provider("A")])
    with pytest.raises(LLMError, match="没有可用"):
        alone.chat("s", "u", 50)
    assert alone.exhausted


def test_rate_limit_is_retried_but_a_long_wait_means_quota_is_gone(post):
    post["replies"] = [FakeResponse(status=429, headers={"Retry-After": "2"}), FakeResponse(content="好了")]
    assert LLMClient([provider()]).chat("s", "u", 50) == "好了"

    post["replies"] = [FakeResponse(status=429, headers={"Retry-After": "3600"})]
    client = LLMClient([provider()])
    with pytest.raises(LLMError):
        client.chat("s", "u", 50)
    assert client.providers[0].down


def test_a_busy_service_is_waited_for_and_not_mistaken_for_an_empty_quota(post, monkeypatch):
    waits = []
    monkeypatch.setattr(llm.time, "sleep", waits.append)
    busy = '{"error":{"code":"1302","message":"您当前使用该API的并发数过高，请降低并发，或联系客服增加限额。"}}'
    post["replies"] = [FakeResponse(status=429, text=busy), FakeResponse(status=429, text=busy), FakeResponse()]
    client = LLMClient([provider()])
    assert client.chat("s", "u", 50) == "ok"
    assert waits == [12.0, 24.0] and not client.providers[0].down  # 提示里有“限额”二字，但这只是忙

    overloaded = '{"error":{"code":"1305","message":"该模型当前访问量过大，请您稍后再试"}}'
    post["replies"] = [FakeResponse(status=429, text=overloaded)] * 3
    with pytest.raises(LLMError, match="访问量过大"):  # 日志里要能看到对方给的原因
        client.chat("s", "u", 50)
    assert not client.providers[0].down


def test_content_filter_is_reported_as_filtered(post):
    post["replies"] = [FakeResponse(status=400, text='{"error":{"code":"1301","message":"内容可能包含敏感信息"}}')]
    with pytest.raises(Filtered):
        LLMClient([provider()]).chat("s", "u", 50)
    post["replies"] = [FakeResponse(finish="content_filter", content="")]
    with pytest.raises(Filtered):
        LLMClient([provider()]).chat("s", "u", 50)
    post["replies"] = [FakeResponse(content="", refusal="I can't help with that")]
    with pytest.raises(Filtered):
        LLMClient([provider()]).chat("s", "u", 50)


def test_unknown_parameter_falls_back_to_a_plain_request(post):
    post["replies"] = [FakeResponse(status=400, text="unknown field response_format"), FakeResponse(content="行了")]
    client = LLMClient([provider(json_mode=True, extra={"thinking": {"type": "disabled"}})])
    assert client.chat("s", "u", 50) == "行了"
    assert "response_format" not in post["calls"][1]["body"] and "thinking" not in post["calls"][1]["body"]


def test_transient_errors_are_retried_then_given_up(post):
    post["replies"] = [llm.requests.ConnectionError("down"), FakeResponse(status=503), FakeResponse(content="")]
    client = LLMClient([provider()])
    with pytest.raises(LLMError, match="空内容"):
        client.chat("s", "u", 50)
    assert client.requests_made == 3 and not client.providers[0].down


def test_request_budget_is_a_hard_limit(post):
    post["replies"] = [FakeResponse(content="1"), FakeResponse(content="2")]
    client = LLMClient([provider()], max_requests=1)
    assert client.chat("s", "u", 50) == "1"
    assert client.exhausted
    with pytest.raises(LLMError, match="上限"):
        client.chat("s", "u", 50)
    assert len(post["calls"]) == 1


def test_timeouts_are_not_retried_and_two_failures_switch_provider(post):
    post["replies"] = [
        llm.requests.ReadTimeout("slow"),
        llm.requests.ReadTimeout("slow"),
        FakeResponse(content="来自 B"),
    ]
    client = LLMClient([provider("A"), provider("B")])
    with pytest.raises(LLMError, match="超时"):
        client.chat("s", "u", 50)
    assert len(post["calls"]) == 1  # 超时不原地重试
    assert client.chat("s", "u", 50) == "来自 B"  # 第二次失败后换下一家，这一轮直接由 B 回答
    assert client.providers[0].down and [p.name for p in client.answered] == ["B"]


def test_a_retired_model_is_recognised_from_a_chinese_error_message(post):
    post["replies"] = [
        FakeResponse(status=400, text='{"error":{"code":"1211","message":"模型不存在，请检查模型代码"}}'),
        FakeResponse(content="来自 B"),
    ]
    client = LLMClient([provider("A", json_mode=True), provider("B")])
    assert client.chat("s", "u", 50) == "来自 B" and len(post["calls"]) == 2


def test_the_whole_stage_has_a_time_budget(post, monkeypatch):
    clock = [1000.0]
    monkeypatch.setattr(llm.time, "monotonic", lambda: clock[0])
    post["replies"] = [FakeResponse(content="1")]
    client = LLMClient([provider()], max_seconds=60)
    assert client.chat("s", "u", 50) == "1" and not client.exhausted
    clock[0] += 61
    assert client.exhausted
    with pytest.raises(LLMError, match="到此为止"):
        client.chat("s", "u", 50)
    assert len(post["calls"]) == 1


def test_keys_only_come_from_api_key_variables_and_only_go_to_https(config):
    config["llm"]["providers"] = [
        {"name": "偷令牌", "key_env": "GITHUB_TOKEN", "base_url": "https://evil.example/v1", "model": "m"},
        {"name": "明文", "key_env": "PLAIN_API_KEY", "base_url": "http://plain.example/v1", "model": "m"},
        {"name": "正常", "key_env": "GOOD_API_KEY", "base_url": "https://good.example/v1", "model": "m"},
    ]
    env = {"GITHUB_TOKEN": "ghs_secret", "PLAIN_API_KEY": "k", "GOOD_API_KEY": "k"}
    assert [p.name for p in build_client(config, env).providers] == ["正常"]
