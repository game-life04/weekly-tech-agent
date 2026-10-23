"""把最新一期每周快讯同步成 GitHub Release：在仓库点 Watch → Custom → Releases 的人会收到邮件通知。

由定时任务在提交生成的文件之后运行（python -m wta release）。只处理最新一期：还没有这个 Release 就建一个
（标签名就是周编号，例如 2026-W42）；已经有了、而且内容变了（例如大模型后来补写了几条）就更新。
令牌用 Actions 自带的 GITHUB_TOKEN，只发给 api.github.com；没有令牌（本地运行、别人 Fork）就什么都不做。
"""

from __future__ import annotations

import logging
from collections.abc import Mapping
from typing import Any

import requests

from . import REPO_URL, render

log = logging.getLogger(__name__)

API = "https://api.github.com"


def body_of(kx: dict[str, Any], config: dict[str, Any]) -> str:
    """Release 的正文：链接都写成完整网址（Release 页面不在仓库目录里，相对链接会失效）。"""
    page, sheet = render.kuaixun_paths(kx)
    headline = render._kx_headline(kx)
    blocks = [f"**本期头条：{render.md_escape(headline)}**"] if headline else []
    blocks.append(
        f"[在仓库里看完整版]({REPO_URL}/blob/main/{page}) · [公众号排版版]({REPO_URL}/blob/main/{sheet})"
        f" · [往期快讯]({REPO_URL}/blob/main/weekly/README.md)"
    )
    blocks += render._kx_body_md(kx, level=2)
    blocks.append(render._kx_footer_md(kx, config))
    return "\n\n".join(blocks) + "\n"


def sync(kx: dict[str, Any], config: dict[str, Any], token: str, slug: str, http: Any = requests) -> str:
    """建或更新这一期的 Release，返回 created / updated / unchanged。"""
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    tag = kx["week"]
    title = render.kx_title(kx) + (f"：{render._kx_headline(kx)}" if render._kx_headline(kx) else "")
    body = body_of(kx, config)
    found = http.get(f"{API}/repos/{slug}/releases/tags/{tag}", headers=headers, timeout=30)
    if found.status_code == 404:
        made = http.post(
            f"{API}/repos/{slug}/releases",
            headers=headers,
            json={"tag_name": tag, "target_commitish": "main", "name": title, "body": body},
            timeout=30,
        )
        made.raise_for_status()
        return "created"
    found.raise_for_status()
    release = found.json()
    if release.get("name") == title and release.get("body") == body:
        return "unchanged"
    changed = http.patch(
        f"{API}/repos/{slug}/releases/{release['id']}",
        headers=headers,
        json={"name": title, "body": body},
        timeout=30,
    )
    changed.raise_for_status()
    return "updated"


def run(issues: list[dict[str, Any]], config: dict[str, Any], env: Mapping[str, str], http: Any = requests) -> int:
    token = env.get("GITHUB_TOKEN") or env.get("GH_TOKEN")
    if not issues:
        log.info("还没有每周快讯，不用发 Release")
        return 0
    if not token:
        log.info("没有 GITHUB_TOKEN，跳过发 Release（只在定时任务里做）")
        return 0
    slug = env.get("GITHUB_REPOSITORY") or render.repo_slug()
    latest = issues[-1]
    try:
        result = sync(latest, config, token, slug, http)
    except requests.RequestException as exc:
        log.warning("同步 Release 失败：%s", exc)
        return 1
    log.info(
        "%s 的 Release：%s", latest["week"], {"created": "已建", "updated": "已更新", "unchanged": "没有变化"}[result]
    )
    return 0
