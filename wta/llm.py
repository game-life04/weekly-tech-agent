"""大模型接口。只依赖 OpenAI 风格的 chat/completions，所以大多数服务都能直接接。

用哪家服务：
1. 设置了环境变量 LLM_API_KEY、LLM_BASE_URL、LLM_MODEL 就优先用它；
2. 然后按 config.yaml 里 llm.providers 的顺序，用配置了密钥的那些；
3. 一个都没有就不用大模型，整个流程照常运行，只是没有中文标题和摘要。

几道保险，保证大模型出问题时不会拖垮当天的日报：
- 一家服务不可用（密钥失效、欠费、模型下线、额度用完）或接连两次失败时，自动换下一家；
- 每次运行的请求总数有上限，总用时也有上限，到了就停；
- 超时不原地重试：服务端“连上了但不回”的时候，重试只会把时间耗光。
"""

from __future__ import annotations

import logging
import re
import time
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

import requests

from .http import USER_AGENT
from .textutil import clean_text

log = logging.getLogger(__name__)

_THINK = re.compile(r"<think>.*?</think>", re.DOTALL)
_FILTERED = re.compile(r"1301|content[_ ]filter|sensitive|敏感|不安全|违规", re.IGNORECASE)
_NO_QUOTA = re.compile(r"1113|insufficient|balance|quota|billing|余额|欠费|额度|限额|使用上限", re.IGNORECASE)
# 智谱的并发过高、频率过高、请求过多：过一会儿就好，不是额度用完（它们的提示里也有“增加限额”这样的字眼）
_BUSY = re.compile(r"\b130[235]\b|请求过多|并发数过高|频率过高")
_NO_MODEL = re.compile(
    r"model.{0,40}(not exist|not found|does not exist|decommission|deprecat)"
    r"|模型不存在|(模型|API).{0,40}(不存在|已下线)",
    re.IGNORECASE,
)


class LLMError(RuntimeError):
    """这一次请求没成功（可以换一批内容再试）。"""


class Filtered(LLMError):
    """内容被服务商的审核拦下了。重试同样的内容没有用，调用方应当缩小范围定位是哪一条。"""


class ProviderDown(LLMError):
    """这家服务现在用不了（密钥、余额、额度或模型的问题），应当换下一家。"""


@dataclass
class Provider:
    name: str
    base_url: str  # 不含 /chat/completions
    api_key: str
    model: str
    json_mode: bool = False  # 是否支持 response_format: json_object
    extra: dict[str, Any] = field(default_factory=dict)  # 这家特有的请求参数，例如关闭“思考”
    interval: float = 3.0  # 两次请求之间至少隔几秒
    down: bool = False
    last_call: float = 0.0
    failures: int = 0  # 接连失败了几次（成功一次就清零）


class LLMClient:
    def __init__(
        self, providers: list[Provider], max_requests: int = 30, max_seconds: float = 480.0, timeout: float = 90.0
    ):
        self.providers = providers
        self.max_requests = max_requests
        self.max_seconds = max_seconds  # 从第一次请求算起，整个大模型阶段最多用这么久
        self.timeout = timeout  # 单次请求的读超时
        self.requests_made = 0
        self.answered: list[Provider] = []  # 实际给出过回复的服务，页脚的标注以它为准
        self._deadline: float | None = None

    @property
    def provider(self) -> Provider | None:
        return next((p for p in self.providers if not p.down), None)

    @property
    def exhausted(self) -> bool:
        """再也发不出请求了：次数用完、时间用完，或者没有可用的服务。"""
        out_of_time = self._deadline is not None and time.monotonic() >= self._deadline
        return self.requests_made >= self.max_requests or out_of_time or self.provider is None

    def chat(self, system: str, user: str, max_tokens: int) -> str:
        """发一轮对话，返回模型的文字回复。失败抛 LLMError；被内容审核拦下抛 Filtered。"""
        while True:
            provider = self.provider
            if provider is None:
                raise LLMError("没有可用的大模型服务")
            try:
                reply = self._call(provider, system, user, max_tokens)
            except Filtered:
                raise
            except ProviderDown as exc:
                provider.down = True
                log.warning("大模型服务“%s”不可用，停用：%s", provider.name, exc)
            except LLMError as exc:
                provider.failures += 1
                others = any(p is not provider and not p.down for p in self.providers)
                if provider.failures < 2 or not others or self.exhausted:
                    raise
                provider.down = True  # 接连两次失败，而且还有别家可用：这一轮改发给下一家
                log.warning("大模型服务“%s”接连失败，换下一家：%s", provider.name, exc)
            else:
                provider.failures = 0
                if provider not in self.answered:
                    self.answered.append(provider)
                return reply

    def _post(self, provider: Provider, body: dict[str, Any]) -> requests.Response:
        now = time.monotonic()
        if self._deadline is None:
            self._deadline = now + self.max_seconds
        if self.requests_made >= self.max_requests:
            raise LLMError(f"本次运行的大模型请求已达上限（{self.max_requests} 次）")
        pause = max(0.0, provider.interval - (now - provider.last_call))
        left = self._deadline - now - pause
        if left <= 1:
            raise LLMError(f"大模型阶段已经用了 {self.max_seconds:.0f} 秒，到此为止")
        if pause:
            time.sleep(pause)
        self.requests_made += 1
        try:
            return requests.post(
                provider.base_url.rstrip("/") + "/chat/completions",
                headers={"Authorization": f"Bearer {provider.api_key}", "User-Agent": USER_AGENT},
                json=body,
                timeout=(10, min(self.timeout, left)),
            )
        finally:
            provider.last_call = time.monotonic()

    def _call(self, provider: Provider, system: str, user: str, max_tokens: int) -> str:
        use_json_mode, use_extra = provider.json_mode, bool(provider.extra)
        last_error = "未知错误"
        for attempt in range(1, 4):
            body: dict[str, Any] = {
                "model": provider.model,
                "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
                "temperature": 0.2,
                "max_tokens": max_tokens,
                "stream": False,
            }
            if use_json_mode:
                body["response_format"] = {"type": "json_object"}
            if use_extra:
                body.update(provider.extra)
            wait = 5.0 * attempt
            try:
                response = self._post(provider, body)
            except requests.Timeout as exc:
                raise LLMError("请求超时") from exc  # 不原地重试，见文件开头
            except requests.RequestException as exc:
                last_error = type(exc).__name__  # 不带详情：异常文字里可能包含请求地址
            else:
                status, text = response.status_code, clean_text(response.text, 300)
                if status == 200:
                    return self._read(response)
                if status in (401, 402, 403, 404) or (status == 400 and _NO_MODEL.search(text)):
                    raise ProviderDown(f"HTTP {status}：{text}")
                if status == 429:
                    retry_after = response.headers.get("Retry-After", "")
                    # 对方没说要等多久就多等一会儿：免费服务在白天会一阵阵地过载，几秒钟缓不过来
                    wait = float(retry_after) if retry_after.isdigit() else 12.0 * attempt
                    if wait > 60 or (_NO_QUOTA.search(text) and not _BUSY.search(text)):
                        raise ProviderDown(f"HTTP 429：{text}")
                    last_error = f"HTTP 429：{text}"
                elif status in (400, 422) and _FILTERED.search(text):
                    raise Filtered(text)
                elif status in (400, 422) and (use_json_mode or use_extra):
                    use_json_mode = use_extra = False  # 可能是不认识某个参数：改成最朴素的请求再试
                    last_error, wait = f"HTTP {status}：{text}", 0.0
                elif status >= 500:
                    last_error = f"HTTP {status}"
                else:
                    raise LLMError(f"HTTP {status}：{text}")
            if attempt < 3 and wait:
                time.sleep(wait)
        raise LLMError(last_error)

    @staticmethod
    def _read(response: requests.Response) -> str:
        try:
            choice = response.json()["choices"][0]
            message = choice.get("message") or {}
        except (ValueError, KeyError, IndexError, TypeError, AttributeError) as exc:
            raise LLMError("返回的格式不是 chat/completions") from exc
        if choice.get("finish_reason") in ("content_filter", "sensitive") or message.get("refusal"):
            raise Filtered("回复被内容审核拦下")
        content = message.get("content")
        reply = _THINK.sub("", content).strip() if isinstance(content, str) else ""
        if not reply:  # 多半是输出长度被“思考”占满了；原样重发还是一样的结果
            raise LLMError(f"模型返回了空内容（finish_reason={choice.get('finish_reason')}）")
        if choice.get("finish_reason") == "length":
            log.info("模型的回复达到了长度上限，后半截被截掉了")
        return reply


def build_client(config: dict[str, Any], env: Mapping[str, str]) -> LLMClient | None:
    """按文件开头说的顺序找出可用的服务；一个都没有就返回 None。"""
    settings = config.get("llm") or {}
    candidates = [
        {
            "name": "自定义服务",
            "key_env": "LLM_API_KEY",
            "base_url": env.get("LLM_BASE_URL", ""),
            "model": env.get("LLM_MODEL", ""),
        },
        *(settings.get("providers") or []),
    ]
    providers: list[Provider] = []
    for entry in candidates:
        key_env, base_url, model = str(entry.get("key_env", "")), str(entry.get("base_url", "")), entry.get("model")
        # 密钥只从名字以 _API_KEY 结尾的环境变量里取、只发给 https 地址：
        # 防止有人改一行配置，就把仓库令牌之类的东西当作“密钥”发到别的服务器
        if not key_env.endswith("_API_KEY") or not base_url.startswith("https://") or not model:
            continue
        if env.get(key_env):
            providers.append(
                Provider(
                    name=str(entry.get("name") or model),
                    base_url=base_url,
                    api_key=env[key_env],
                    model=str(model),
                    json_mode=bool(entry.get("json_mode")),
                    extra=dict(entry.get("extra") or {}),
                    interval=float(entry.get("interval", 3)),
                )
            )
    if not providers:
        return None
    return LLMClient(
        providers,
        max_requests=int(settings.get("max_requests", 30)),
        max_seconds=float(settings.get("max_seconds", 480)),
    )
