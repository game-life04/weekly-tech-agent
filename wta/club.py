"""快讯的“俱乐部动态”：俱乐部 GitHub 组织上一周的开源活动，全部由程序根据接口数据写成，不经过大模型。

- 统计和最活跃的仓库来自俱乐部的开源仪表盘（Open-Source-Dashboard，osd.openatom.club）的公开接口。
  仪表盘按“最近 N 天”统计（每周快讯用 7 天，每日快讯用 1 天），不能指定日期：页面上写的统计日期
  以接口返回的为准，可能和快讯的日期差一天。
- 新建的仓库和新发布的版本来自 GitHub 官方接口。新建的仓库如果也是最活跃的仓库，合成一条登。
- 总数由各仓库的数字相加，去掉 exclude 里的仓库（例如本项目自己：机器人每天的提交不算俱乐部活动）；
  只有机器人在动的仓库（贡献者为 0）不算“活跃”。贡献者人数直接用仪表盘的统计（已去掉机器人，
  但没法去掉 exclude 里那几个仓库的人）。
"""

from __future__ import annotations

import logging
import re
from datetime import date, timedelta
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


def _label(days: int) -> str:
    """标题里的时间说法：7 天写“一周”，1 天不写（正文开头有日期）。"""
    return "一周" if days == 7 else "" if days == 1 else f"{days} 天"


def summary_entry(
    settings: dict[str, Any], repos: list[dict[str, Any]], people: Any, when: tuple[date, date], days: int = 7
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
        "headline": f"{name}{_label(days)}合并 {total['closed_merged_prs']} 个 PR、提交 {total['new_commits']} 次",
        "when": date_span(*when),
        "date": when[1].isoformat(),
        "body": body + "。",
        "url": settings["dashboard"].rstrip("/") + "/",
        "via": VIA,
    }


def repo_entries(
    settings: dict[str, Any],
    repos: list[dict[str, Any]],
    when: tuple[date, date],
    created: dict[str, dict] | None = None,
    days: int = 7,
) -> list[dict]:
    """最活跃的几个仓库。这一周新建的写明“新建”，不再单独登一条新建仓库的消息。"""
    exclude = {name.casefold() for name in settings.get("exclude") or []}
    found = []
    for repo in _active(repos, exclude)[: int(settings.get("top_repos", 3))]:
        name = clean_text(repo.get("name"), 60)
        sig = clean_text((repo.get("sig") or {}).get("name"), 30)
        merged, commits = _number(repo.get("closed_merged_prs")), _number(repo.get("new_commits"))
        new_prs, people = _number(repo.get("new_prs")), _number(repo.get("active_contributors"))
        if merged:
            action = f"合并 {merged} 个 PR"
        elif commits:
            action = f"提交 {commits} 次"
        elif new_prs:
            action = f"新增 {new_prs} 个 PR"
        else:  # 只有 issue 之类的活动
            action = f"{people} 位贡献者参与"
        fresh = (created or {}).get(name)
        opening = f"{sig + '的 ' if sig else ''}{name} 仓库"
        if fresh:
            opening += f"于{fresh['day'].month}月{fresh['day'].day}日新建" + (
                f"（{fresh['about']}）" if fresh["about"] else ""
            )
            opening += f"，{_label(days) + '内' if _label(days) else '当天'}"
        counts = [
            ("新增 PR {} 个", _number(repo.get("new_prs"))),
            ("合并 {} 个", merged),
            ("提交 {} 次", commits),
            ("新增代码 {} 行", _number(repo.get("lines_added"))),
        ]
        done = "、".join(text.format(value) for text, value in counts if value)  # 是 0 的不写
        body = f"{opening}{done}，{_number(repo.get('active_contributors'))} 位贡献者参与。"
        found.append(
            {
                "cat": "club",
                "headline": f"{'新仓库 ' if fresh else ''}{name} {_label(days)}{action}",
                "when": date_span(*when),
                "date": when[1].isoformat(),
                "body": body,
                "url": clean_text(repo.get("url")),
                "via": "GitHub",
            }
        )
    return found


def _within(value: object, monday: date, sunday: date, offset: float) -> date | None:
    moment = parse_time(value)
    day = local_date(moment, offset) if moment else None
    return day if day and monday <= day <= sunday else None


def new_repos(ctx: Context, settings: dict[str, Any], monday: date, sunday: date, offset: float) -> dict[str, dict]:
    """这一周新建的公开仓库：{仓库名: {"day", "about", "url"}}。"""
    found = {}
    params = {"sort": "created", "direction": "desc", "per_page": 30}
    for repo in api_get(ctx, f"/orgs/{settings['org']}/repos", params) or []:
        day = _within(repo.get("created_at"), monday, sunday, offset)
        name = str(repo.get("name", ""))
        if day and not repo.get("fork") and not repo.get("private") and _REPO_NAME.fullmatch(name):
            found[name] = {
                "day": day,
                "about": clean_text(repo.get("description"), 100),
                "url": clean_text(repo.get("html_url")),
            }
    return found


def github_entries(
    ctx: Context,
    settings: dict[str, Any],
    repos: list[dict[str, Any]],
    monday: date,
    sunday: date,
    offset: float,
    created: dict[str, dict],
    shown: set[str],
) -> list[dict[str, Any]]:
    """这一周新建的仓库（已经作为最活跃的仓库登了的除外）和新发布的版本。"""
    found: list[dict[str, Any]] = []
    for name, info in created.items():
        if name in shown:
            continue
        day = info["day"]
        found.append(
            {
                "cat": "club",
                "headline": f"俱乐部新建 {name} 仓库",
                "when": f"{day.month}月{day.day}日",
                "date": day.isoformat(),
                "body": f"俱乐部在 GitHub 上新建 {name} 仓库"
                + (f"，仓库简介：{info['about']}" if info["about"] else "")
                + "。",
                "url": info["url"],
                "via": "GitHub",
            }
        )
    exclude = {name.casefold() for name in settings.get("exclude") or []}
    for repo in _active(repos, exclude)[: int(settings.get("release_repos", 8))]:
        name = str(repo["name"])
        for release in api_get(ctx, f"/repos/{settings['org']}/{name}/releases", {"per_page": 5}) or []:
            day = _within(release.get("published_at"), monday, sunday, offset)
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
    ctx: Context, settings: dict[str, Any], offset: float, *, days: int = 7, window: tuple[date, date] | None = None
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """返回（快讯条目，这次的统计日期）。仪表盘取不到时抛异常；GitHub 那一半取不到只记日志。

    days 是仪表盘统计最近几天；window 是新仓库和新版本算哪几天，不给就用仪表盘这次统计的日期。
    这几天里一点开发活动都没有时，不登统计。
    """
    api = settings["dashboard"].rstrip("/") + "/api/v1"
    params = {"range": f"{days}d"}
    # 统计到哪一天只有 growth-analysis 会说，它只认 7d 这类常用区间：取它的结束日期，再往前推 days 天
    growth = ctx.http.get_json(f"{api}/organization/growth-analysis", params={"range": "7d"})
    repos = (ctx.http.get_json(f"{api}/organization/repositories", params=params) or {}).get("repositories")
    people = ctx.http.get_json(f"{api}/contributors/stats", params=params)
    week = period(growth)
    if week is None or not isinstance(repos, list):
        raise RuntimeError("仪表盘返回的数据格式和预期不同")
    when = (week[1] - timedelta(days=days - 1), week[1])
    monday, sunday = window or when
    # 仓库名会拼进接口路径、写进页面：不是正常写法的整个不要
    repos = [repo for repo in repos if isinstance(repo, dict) and _REPO_NAME.fullmatch(str(repo.get("name", "")))]
    try:
        created = new_repos(ctx, settings, monday, sunday, offset)
    except Exception as exc:  # 新仓库只是补充，取不到不影响周统计
        log.warning("取不到俱乐部的新仓库：%s", clean_text(str(exc), 200))
        created = {}
    exclude = {name.casefold() for name in settings.get("exclude") or []}
    entries = []
    if any(
        _number(repo.get(f))
        for repo in repos
        for f in ("new_prs", "new_commits")
        if repo["name"].casefold() not in exclude
    ):
        top = repo_entries(settings, repos, when, created, days)
        entries = [summary_entry(settings, repos, people, when, days), *top]
    shown = {str(repo["name"]) for repo in _active(repos, exclude)[: int(settings.get("top_repos", 3))]}
    try:
        entries += github_entries(ctx, settings, repos, monday, sunday, offset, created, shown)
    except Exception as exc:
        log.warning("取不到俱乐部的新版本：%s", clean_text(str(exc), 200))
    return entries, {"start": when[0].isoformat(), "end": when[1].isoformat()}
