"""HTTP 请求封装：统一 User-Agent、超时、重试、大小上限和时间上限。所有来源都通过它访问网络。"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass, field
from typing import Any

import requests

from . import REPO_URL, __version__

log = logging.getLogger(__name__)

# 很多网站会拒绝 python-requests 的默认标识，也有网站拒绝伪装成浏览器的标识；
# 老老实实写明自己是谁、仓库在哪，实测通过率最高，也方便站长联系。
USER_AGENT = f"weekly-tech-agent/{__version__} (+{REPO_URL})"
_RETRY_STATUS = {429, 500, 502, 503, 504}
MAX_BYTES = 20 * 1024 * 1024  # 解压后超过 20 MB 的响应视为异常（个别仓库的版本列表有 8 MB 多）
MAX_SECONDS = 60.0  # 一次请求从发出到读完最多这么久
MAX_RETRY_AFTER = 30.0  # 对方要求等待超过这么久，就不等了，按“额度用完”处理


class HttpError(RuntimeError):
    def __init__(self, message: str, status: int | None = None, rate_limited: bool = False):
        super().__init__(message)
        self.status = status
        self.rate_limited = rate_limited  # 对方明确表示额度用完了，短时间内重试没有意义


@dataclass
class Response:
    """读完并检查过大小的响应。"""

    url: str
    status_code: int
    content: bytes
    encoding: str | None = None
    headers: dict[str, str] = field(default_factory=dict)

    @property
    def text(self) -> str:
        return self.content.decode(self.encoding or "utf-8", errors="replace")

    def json(self) -> Any:
        return json.loads(self.content)


class Http:
    def __init__(self, timeout: tuple[float, float] = (10, 30), retries: int = 3, backoff: float = 2.0):
        self.timeout = timeout
        self.retries = retries
        self.backoff = backoff
        self.deadline: float | None = None  # time.monotonic() 时刻；过了就不再发请求（调度器按来源设置）
        self.session = requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT  # 注意：令牌不能放在这里，否则会发给所有网站

    def _remaining(self, limit: float) -> float:
        left = limit if self.deadline is None else min(limit, self.deadline - time.monotonic())
        if left <= 0:
            raise HttpError("超过了这个来源的时间上限")
        return left

    def _read(self, url: str, params, headers, timeout: tuple[float, float], limit: float) -> Response:
        """发一次请求并把响应体读完。边读边数：超过大小上限或总时限立刻放弃，而不是先全部下载。"""
        started = time.monotonic()
        budget = self._remaining(limit)
        timeout = (min(timeout[0], budget), min(timeout[1], budget))
        with self.session.get(url, params=params, headers=headers, timeout=timeout, stream=True) as response:
            chunks: list[bytes] = []
            size = 0
            for chunk in response.iter_content(65536):  # 拿到的是解压之后的字节
                size += len(chunk)
                if size > MAX_BYTES:
                    raise HttpError(f"响应超过 {MAX_BYTES // 1024 // 1024} MB：{url}", response.status_code)
                if time.monotonic() - started > budget:
                    raise HttpError(f"读取超过 {budget:.0f} 秒：{url}", response.status_code)
                chunks.append(chunk)
            encoding = response.encoding if "charset" in response.headers.get("Content-Type", "").lower() else None
            return Response(response.url, response.status_code, b"".join(chunks), encoding, dict(response.headers))

    def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        timeout: tuple[float, float] | None = None,
        retries: int | None = None,
        max_seconds: float = MAX_SECONDS,
    ) -> Response:
        """GET 请求。连接失败、429 和 5xx 会按 2s、4s…… 退避重试；读超时不重试；最终失败抛 HttpError。"""
        attempts = retries or self.retries
        last_error, last_status = "未知错误", None
        for attempt in range(1, attempts + 1):
            wait = self.backoff**attempt
            try:
                response = self._read(url, params, headers, timeout or self.timeout, max_seconds)
            except requests.ReadTimeout as exc:  # 连上了但不回数据：再试多半还是等，白白耗时间
                raise HttpError(f"读取超时：{url}") from exc
            except requests.RequestException as exc:
                last_error, last_status = f"{type(exc).__name__}: {exc}", None
            else:
                status = last_status = response.status_code
                retry_after = response.headers.get("Retry-After", "")
                wait_asked = float(retry_after) if retry_after.isdigit() else 0.0
                out_of_quota = response.headers.get("x-ratelimit-remaining") == "0" or wait_asked > MAX_RETRY_AFTER
                if status in (403, 429) and (out_of_quota or (status == 403 and retry_after)):
                    raise HttpError(f"HTTP {status}（对方限流）：{url}", status, rate_limited=True)
                if status in _RETRY_STATUS:
                    last_error, wait = f"HTTP {status}", max(wait, wait_asked)
                elif status >= 400:
                    raise HttpError(f"HTTP {status}：{url}", status)
                else:
                    return response
            if attempt < attempts:
                log.debug("第 %d 次请求失败（%s），%.0f 秒后重试：%s", attempt, last_error, wait, url)
                time.sleep(min(wait, self._remaining(max_seconds)))
        raise HttpError(f"{last_error}：{url}", last_status)

    def get_json(self, url: str, **kwargs: Any) -> Any:
        response = self.get(url, **kwargs)
        try:
            return response.json()
        except ValueError as exc:
            raise HttpError(f"返回的不是 JSON：{url}", response.status_code) from exc

    def get_text(self, url: str, **kwargs: Any) -> str:
        return self.get(url, **kwargs).text
