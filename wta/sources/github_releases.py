"""GitHub 版本发布：关注列表里的仓库最近有没有值得一提的新版本。

关注列表在 config.yaml 的 sources.github_releases.repos 里，每一项是仓库名，
或者 {repo: 仓库名, tag_regex: 只认匹配的标签, trust_flag_only: true}。

不能直接用“最新版本”接口，原因都是实测遇到的：
- 一个仓库发多个包时，“最新”可能是别的包（langchain 仓库的最新是 langchain-core）；
- 有的仓库一天发十几个预发布构建，正式版被淹没（llama.cpp）；
- 预发布标记不可靠，要结合标签名里的 alpha / beta / rc 一起判断。
所以这里自己读版本列表、自己分类，只报主版本和次版本更新；补丁版本不报，
发版特别频繁的仓库只报主版本更新。
"""

from __future__ import annotations

import logging
import re
from datetime import timedelta
from typing import Any

from ..dates import parse_time, to_iso
from ..models import Item
from ..textutil import clean_text
from ._github import RateLimited, api_get
from .base import Context

log = logging.getLogger(__name__)

NAME = "github_releases"
TITLE = "GitHub 版本发布"
MAX_SECONDS = 240  # 三十多个仓库逐个请求，时间上限放宽一些

ROUTINE = 12  # 30 天内正式版达到这个数，就算“发版特别频繁”
_VERSION = re.compile(r"(\d+)\.(\d+)(?:\.(\d+))?(?:\.(\d+))?")
_DATE = re.compile(r"(?<!\d)(20\d{2})-?(\d{2})-?(\d{2})(?!\d)")
_PRE_SUFFIX = re.compile(
    r"^[-._+]?(?:(?:alpha|beta|preview|pre|rc|dev|nightly|canary|next|snapshot|exp|experimental)(?![a-z])"
    r"|(?:a|b|c)\d+(?![a-z]))",
    re.IGNORECASE,
)
_ROLLING = re.compile(r"(?i)(?:^|[-_/])(nightly|latest|canary|edge|preview|dev|tip|main|master)(?:$|[-_/])")
_LEVEL_TEXT = {"major": "主版本更新", "minor": "次版本更新", "calver": "新版本"}
_LEVEL_HEAT = {"major": 0.9, "minor": 0.65, "calver": 0.5}


def parse_tag(tag: str) -> dict[str, Any]:
    """把标签拆成 系列前缀 + 版本号 + 是否预发布。

    'langchain-core==1.6.9' → 前缀 'langchain-core=='，版本 (1, 6, 9)
    'rust-v0.163.0-alpha.5' → 前缀 'rust-v'，版本 (0, 163, 0)，预发布
    '2026-07-28'            → 按日期编号的版本（calver）
    'nightly'               → 没有版本号
    """
    match = _VERSION.search(tag)
    if match:
        version = tuple(int(g) for g in match.groups() if g is not None)
        pre = bool(_PRE_SUFFIX.match(tag[match.end() :]))
        return {"prefix": tag[: match.start()], "version": version, "pre": pre, "calver": version[0] >= 2000}
    match = _DATE.search(tag)
    if match:
        version = tuple(int(g) for g in match.groups())
        pre = bool(_PRE_SUFFIX.match(tag[match.end() :]))
        return {"prefix": tag[: match.start()], "version": version, "pre": pre, "calver": True}
    return {"prefix": tag, "version": None, "pre": bool(_ROLLING.search(tag)), "calver": False}


def classify(
    releases: list[dict[str, Any]], tag_regex: str = "", trust_flag_only: bool = False
) -> list[dict[str, Any]]:
    """给每个版本（新的在前）标上 kind 和 level。

    kind：stable（正式版）/ pre（预发布）/ other（没有版本号，或被 tag_regex 排除）
    level：major / minor / patch / calver，只有正式版才有。和同一系列里更早的正式版比较得出，
           所以 v3.0.2 之后才发的 v2.6.25（旧分支的补丁）会被正确地判为 patch。
    """
    wanted = re.compile(tag_regex) if tag_regex else None
    result = []
    for release in releases:
        parsed = parse_tag(release["tag"])
        kind = "stable"
        if (wanted and not wanted.search(release["tag"])) or parsed["version"] is None:
            kind = "other"
        elif release["prerelease"] or (parsed["pre"] and not trust_flag_only):
            kind = "pre"
        result.append({**release, **parsed, "kind": kind, "level": None})
    for index, release in enumerate(result):
        if release["kind"] != "stable":
            continue
        if release["calver"]:
            release["level"] = "calver"
            continue
        version = release["version"]
        older = [
            r["version"] for r in result[index + 1 :] if r["kind"] == "stable" and r["prefix"] == release["prefix"]
        ]
        if not older:  # 没有可比较的：x.y 或 x.y.0 算次版本，其余算补丁
            release["level"] = "minor" if len(version) < 3 or version[2] == 0 else "patch"
        elif version[0] > max(o[0] for o in older):
            release["level"] = "major"
        elif version[:2] > max(o[:2] for o in older):
            release["level"] = "minor"
        else:
            release["level"] = "patch"
    return result


def _normalize(raw: dict[str, Any]) -> dict[str, Any]:
    return {
        "tag": raw["tag_name"],
        "prerelease": bool(raw.get("prerelease")),
        "published": parse_time(raw.get("published_at") or raw.get("created_at")),
        "url": raw["html_url"],
        "notes": raw.get("body") or "",
    }


def _watch(ctx: Context, entry: dict[str, Any], since) -> Item | None:
    repo = entry["repo"]
    raw = api_get(ctx, f"/repos/{repo}/releases", {"per_page": 30})
    if raw is None:
        log.warning("关注的仓库 %s 不存在了（可能改名或删除），请更新 config.yaml", repo)
        return None
    releases = [_normalize(r) for r in raw if not r.get("draft")]
    releases = sorted((r for r in releases if r["published"]), key=lambda r: r["published"], reverse=True)
    if not releases:
        return None

    def run_classify() -> list[dict[str, Any]]:
        return classify(releases, entry.get("tag_regex", ""), bool(entry.get("trust_flag_only")))

    classified = run_classify()
    # 30 条里没有正式版，或者 30 条还不够覆盖时间窗口（预发布太多），再问一次“最新正式版”
    if not any(r["kind"] == "stable" for r in classified) or (
        len(releases) >= 30 and releases[-1]["published"] > since
    ):
        latest = api_get(ctx, f"/repos/{repo}/releases/latest")
        if latest and latest["tag_name"] not in {r["tag"] for r in releases}:
            releases.append(_normalize(latest))
            releases.sort(key=lambda r: r["published"], reverse=True)
            classified = run_classify()

    stable = [r for r in classified if r["kind"] == "stable"]
    routine = sum(1 for r in stable if (ctx.now - r["published"]).days < 30) >= ROUTINE
    notable = [
        r
        for r in stable
        if r["published"] > since and (r["level"] == "major" or (r["level"] != "patch" and not routine))
    ]
    if not notable:
        return None
    best = max(notable, key=lambda r: (_LEVEL_HEAT[r["level"]], r["version"], r["published"]))
    return Item(
        title=f"{repo} {best['tag']}",
        url=best["url"],
        source=NAME,
        section="opensource",
        published=to_iso(best["published"]),
        summary=_LEVEL_TEXT[best["level"]],
        heat=_LEVEL_HEAT[best["level"]],
        extra={"evidence": clean_text(best["notes"], 1500), "level": best["level"]},
    )


def fetch(config: dict[str, Any], ctx: Context) -> list[Item]:
    since = ctx.now - timedelta(days=float(config.get("days", 3)))
    weight = float(config.get("weight", 0.7))
    items: list[Item] = []
    failed: list[str] = []
    for entry in config.get("repos") or []:
        entry = {"repo": entry} if isinstance(entry, str) else entry
        try:
            item = _watch(ctx, entry, since)
        except RateLimited:
            raise  # 额度没了，后面的仓库也不用试了
        except Exception as exc:  # 一个仓库出错不影响其他仓库
            failed.append(entry["repo"])
            log.warning("读取 %s 的版本列表失败：%s", entry["repo"], exc)
            continue
        if item:
            item.weight = weight
            items.append(item)
    if failed and len(failed) == len(config.get("repos") or []):
        raise RuntimeError("关注列表里的仓库全部读取失败")
    return items
