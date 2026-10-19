"""快讯的“俱乐部动态”：俱乐部 GitHub 组织上一周的开源活动，全部由程序根据接口数据写成，不经过大模型。

- 周统计和最活跃的仓库来自俱乐部的开源仪表盘（Open-Source-Dashboard，osd.openatom.club）的公开接口。
  仪表盘按“最近 7 天”统计，不能指定日期：页面上写的统计区间以接口返回的为准，可能和快讯的那一周差一天。
- 新建的仓库和新发布的版本来自 GitHub 官方接口。
- 总数由各仓库的数字相加，去掉 exclude 里的仓库（例如本项目自己：机器人每天的提交不算俱乐部活动）；
  只有机器人在动的仓库（贡献者为 0）不算“活跃”。贡献者人数直接用仪表盘的统计（已去掉机器人，
  但没法去掉 exclude 里那几个仓库的人）。
"""

from __future__ import annotations

import logging
import re
from datetime import date
from typing import Any

from .dates import date_span, local_date, parse_time
from .sources._github import api_get
from .sources.base import Context
from .textutil import clean_text

log = logging.getLogger(__name__)

VIA = "俱乐部开源仪表盘"
_REPO_NAME = re.compile(r"[A-Za-z0-9._-]{1,100}")
_FIELDS = ("new_prs", "closed_merged_prs", "new_issues", "new_commits", "lines_added", "lines_deleted")


def _number(value: object) -> int:
    return int(value) if isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0 else 0


def period(growth: Any) -> tuple[date, date] | None:
    """仪表盘这次统计的起止日期。"""
    try:
        current = growth["period"]["current"]
        return date.fromisoformat(current["start"]), date.fromisoformat(current["end"])
    except (KeyError, TypeError, ValueError):
        return None


def _active(repos: list[dict[str, Any]], exclude: set[str]) -> list[dict[str, Any]]:
    rows = [
        repo
        for repo in repos
        if isinstance(repo, dict)
        and repo.get("is_active")
        and str(repo.get("name", "")).casefold() not in exclude
        and _number(repo.get("active_contributors")) > 0
    ]
    activity = ("closed_merged_prs", "new_commits", "new_prs", "active_contributors")
    return sorted(rows, key=lambda repo: tuple(_number(repo.get(name)) for name in activity), reverse=True)


def summary_entry(
    settings: dict[str, Any], repos: list[dict[str, Any]], people: Any, when: tuple[date, date]
) -> dict[str, Any]:
    exclude = {name.casefold() for name in settings.get("exclude") or []}
    counted = [repo for repo in repos if isinstance(repo, dict) and str(repo.get("name", "")).casefold() not in exclude]
    total = {name: sum(_number(repo.get(name)) for repo in counted) for name in _FIELDS}
    active = _active(repos, exclude)
    people = people if isinstance(people, dict) else {}
    contributors, newcomers = _number(people.get("unique_contributors")), _number(people.get("new_contributors"))
    name = settings.get("name") or "俱乐部"
    body = (
        f"据{VIA}统计，{name}跟踪的 {len(counted)} 个仓库中有 {len(active)} 个有人参与开发，"
        f"共新增 PR {total['new_prs']} 个、合并 {total['closed_merged_prs']} 个，提交 {total['new_commits']} 次，"
        f"新增代码 {total['lines_added']} 行、删除 {total['lines_deleted']} 行"
    )
    if contributors:
        body += f"，{contributors} 位贡献者参与" + (f"，其中 {newcomers} 位是第一次贡献" if newcomers else "")
    return {
        "cat": "club",
        "headline": f"{name}一周合并 {total['closed_merged_prs']} 个 PR、提交 {total['new_commits']} 次",
        "when": date_span(*when),
        "date": when[1].isoformat(),
        "body": body + "。",
        "url": settings["dashboard"].rstrip("/") + "/",
        "via": VIA,
    }


def repo_entries(settings: dict[str, Any], repos: list[dict[str, Any]], when: tuple[date, date]) -> list[dict]:
    exclude = {name.casefold() for name in settings.get("exclude") or []}
    found = []
    for repo in _active(repos, exclude)[: int(settings.get("top_repos", 3))]:
        name = clean_text(repo.get("name"), 60)
        sig = clean_text((repo.get("sig") or {}).get("name"), 30)
        merged, commits = _number(repo.get("closed_merged_prs")), _number(repo.get("new_commits"))
        action = f"合并 {merged} 个 PR" if merged else f"提交 {commits} 次"
        body = (
            f"{sig + '的 ' if sig else ''}{name} 仓库新增 PR {_number(repo.get('new_prs'))} 个、合并 {merged} 个，"
            f"提交 {commits} 次，新增代码 {_number(repo.get('lines_added'))} 行，"
            f"{_number(repo.get('active_contributors'))} 位贡献者参与。"
        )
        found.append(
            {
                "cat": "club",
                "headline": f"{name} 一周{action}",
                "when": date_span(*when),
                "date": when[1].isoformat(),
                "body": body,
                "url": clean_text(repo.get("url")),
                "via": "GitHub",
            }
        )
    return found


def github_entries(
    ctx: Context, settings: dict[str, Any], repos: list[dict[str, Any]], monday: date, sunday: date, offset: float
) -> list[dict[str, Any]]:
    """这一周新建的仓库和新发布的版本。"""
    org = settings["org"]
    found: list[dict[str, Any]] = []

    def within(value: object) -> date | None:
        moment = parse_time(value)
        day = local_date(moment, offset) if moment else None
        return day if day and monday <= day <= sunday else None

    for repo in api_get(ctx, f"/orgs/{org}/repos", {"sort": "created", "direction": "desc", "per_page": 30}) or []:
        day = within(repo.get("created_at"))
        if not day or repo.get("fork") or repo.get("private"):
            continue
        name = clean_text(repo.get("name"), 60)
        about = clean_text(repo.get("description"), 100)
        found.append(
            {
                "cat": "club",
                "headline": f"俱乐部新建 {name} 仓库",
                "when": f"{day.month}月{day.day}日",
                "date": day.isoformat(),
                "body": f"俱乐部在 GitHub 上新建 {name} 仓库" + (f"，仓库简介：{about}" if about else "") + "。",
                "url": clean_text(repo.get("html_url")),
                "via": "GitHub",
            }
        )
    exclude = {name.casefold() for name in settings.get("exclude") or []}
    for repo in _active(repos, exclude)[: int(settings.get("release_repos", 8))]:
        name = str(repo["name"])
        for release in api_get(ctx, f"/repos/{org}/{name}/releases", {"per_page": 5}) or []:
            day = within(release.get("published_at"))
            if not day or release.get("draft"):
                continue
            tag = clean_text(release.get("tag_name"), 40)
            title = clean_text(release.get("name"), 60)
            found.append(
                {
                    "cat": "club",
                    "headline": f"{name} 发布 {tag}",
                    "when": f"{day.month}月{day.day}日",
                    "date": day.isoformat(),
                    "body": f"{name} 发布新版本 {tag}" + (f"（{title}）" if title and title != tag else "") + "。",
                    "url": clean_text(release.get("html_url")),
                    "via": "GitHub",
                }
            )
    return sorted(found, key=lambda entry: entry["date"])


def fetch(
    ctx: Context, settings: dict[str, Any], monday: date, sunday: date, offset: float
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """返回（快讯条目，这次的统计信息）。仪表盘取不到时抛异常；GitHub 那一半取不到只记日志。"""
    api = settings["dashboard"].rstrip("/") + "/api/v1"
    params = {"range": "7d"}
    growth = ctx.http.get_json(f"{api}/organization/growth-analysis", params=params)
    repos = (ctx.http.get_json(f"{api}/organization/repositories", params=params) or {}).get("repositories")
    people = ctx.http.get_json(f"{api}/contributors/stats", params=params)
    when = period(growth)
    if when is None or not isinstance(repos, list):
        raise RuntimeError("仪表盘返回的数据格式和预期不同")
    # 仓库名会拼进接口路径、写进页面：不是正常写法的整个不要
    repos = [repo for repo in repos if isinstance(repo, dict) and _REPO_NAME.fullmatch(str(repo.get("name", "")))]
    entries = [summary_entry(settings, repos, people, when), *repo_entries(settings, repos, when)]
    try:
        entries += github_entries(ctx, settings, repos, monday, sunday, offset)
    except Exception as exc:  # 新仓库和新版本只是补充，取不到不影响周统计
        log.warning("取不到俱乐部的新仓库和新版本：%s", clean_text(str(exc), 200))
    return entries, {"start": when[0].isoformat(), "end": when[1].isoformat()}
