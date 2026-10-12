"""访问 GitHub 官方接口（api.github.com）的小工具，几个 GitHub 来源共用。"""

from __future__ import annotations

from typing import Any

from ..http import HttpError
from .base import Context

API = "https://api.github.com"


class RateLimited(RuntimeError):
    """接口额度用完了：这一轮不用再试，等下一个小时。"""


def api_get(ctx: Context, path: str, params: dict[str, Any] | None = None) -> Any:
    """GET 一个接口并返回解析好的 JSON；资源不存在（404）时返回 None。

    令牌只通过这里发给 api.github.com，不会带到别的网站。在 GitHub Actions 里用自带的
    GITHUB_TOKEN（每小时 1000 次）；本地不设令牌也能跑，但每小时只有 60 次。
    """
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    token = ctx.env.get("GITHUB_TOKEN") or ctx.env.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        return ctx.http.get_json(API + path, params=params, headers=headers)
    except HttpError as exc:
        if exc.status == 404:
            return None
        if exc.rate_limited:
            raise RateLimited("GitHub 接口额度用完了（本地运行可以设置环境变量 GITHUB_TOKEN 提高额度）") from exc
        raise
