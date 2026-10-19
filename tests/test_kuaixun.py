"""每周快讯的测试：三个外部数据源的解析、大模型改写的核对与兜底、什么时候该生成。"""

from __future__ import annotations

from datetime import UTC, date, datetime

import pytest
from fakes import FakeClient, FakeHttp, context

from wta import club, deadlines, excerpt, kuaixun, policy, store
from wta.dates import to_iso
from wta.dedupe import item_id
from wta.http import HttpError
from wta.llm import LLMError
from wta.models import Item
from wta.publish import save_week_note

MONDAY, SUNDAY = date(2026, 10, 5), date(2026, 10, 11)
NOW = datetime(2026, 10, 11, 19, 30, tzinfo=UTC)  # 北京时间 10-12（周一）03:30


# ------------------------------------------------------------------ 政策动向
def gov(title, day, url="https://www.gov.cn/zhengce/202610/content_1.htm", subtitle=""):
    return {"TITLE": title, "SUB_TITLE": subtitle, "URL": url, "DOCRELPUBTIME": day}


def test_policy_keeps_related_items_of_the_week_from_both_lists():
    latest, news = policy.FEEDS
    http = FakeHttp(
        {
            latest: [
                gov("国务院关于深入实施“人工智能+”行动的意见", "2026-10-06"),
                gov("关于印发人工智能标准的通知", "2026-10-12", url="https://www.gov.cn/zhengce/2.htm"),  # 下一周的
                gov("关于粮食收购的通知", "2026-10-07", url="https://www.gov.cn/zhengce/3.htm"),  # 不相关
                gov("人工智能产业的转载", "2026-10-07", url="https://example.com/4.htm"),  # 不是政府网的链接
                "坏数据",
                gov("人工智能", "不是日期", url="https://www.gov.cn/zhengce/5.htm"),
            ],
            news: [
                gov("国务院常务会议听取人工智能行动汇报", "2026-10-09", url="https://www.gov.cn/yaowen/6.htm"),
                gov("某领导考察人工智能企业", "2026-10-08", url="https://www.gov.cn/yaowen/7.htm"),  # 时政活动
                gov("国务院关于深入实施“人工智能+”行动的意见", "2026-10-06"),  # 两个列表里重复
            ],
        }
    )
    settings = {"keywords": ["人工智能"], "exclude": ["考察"]}
    items = policy.fetch(http, MONDAY, SUNDAY, settings)
    assert [item.title for item in items] == [
        "国务院关于深入实施“人工智能+”行动的意见",
        "国务院常务会议听取人工智能行动汇报",
    ]
    first = items[0]
    assert (first.source, first.section, first.via) == ("policy", "news", "中国政府网")
    assert first.published == "2026-10-05T16:00:00Z" and first.extra["kx_day"] == "2026-10-06"
    assert first.id == item_id(first.url)


def test_policy_survives_one_list_failing_but_not_both():
    latest, news = policy.FEEDS
    http = FakeHttp({latest: HttpError("HTTP 500", 500), news: [gov("人工智能新闻", "2026-10-06")]})
    assert len(policy.fetch(http, MONDAY, SUNDAY, {"keywords": ["人工智能"]})) == 1
    with pytest.raises(RuntimeError):
        policy.fetch(FakeHttp({}), MONDAY, SUNDAY, {"keywords": ["人工智能"]})


# ------------------------------------------------------------------ 活动预告
def conference(title, rank="A", sub="AI", zone="AoE", timeline=None, **edition):
    return {
        "title": title,
        "description": f"{title} Conference",
        "sub": sub,
        "rank": {"ccf": rank},
        "confs": [
            {"year": 2027, "link": f"https://{title.lower()}.org", "timezone": zone, "timeline": timeline, **edition}
        ],
    }


def test_deadlines_convert_to_beijing_time_and_keep_the_window():
    data = [
        conference(
            "CVPR",
            timeline=[{"deadline": "2026-11-16 23:59:59", "abstract_deadline": "2026-11-10 23:59:59"}],
            date="June 20-25, 2027",
            place="Seattle, USA",
        ),
        conference("ICML", zone="UTC+8", timeline=[{"deadline": "2026-10-20 12:00:00", "comment": "Regular round"}]),
        conference("PTCONF", zone="PT", timeline=[{"deadline": "2026-10-30 23:59:59"}]),
        conference("LATE", timeline=[{"deadline": "2027-03-01 23:59:59"}]),  # 超出窗口
        conference("PAST", timeline=[{"deadline": "2026-10-01 23:59:59"}]),  # 已经截止
        conference("TBD", timeline=[{"deadline": "TBD"}]),
        conference("MARS", zone="Mars Time", timeline=[{"deadline": "2026-10-20 23:59:59"}]),  # 时区认不出
        conference("CRANK", rank="C", timeline=[{"deadline": "2026-10-20 23:59:59"}]),
        conference("NETS", sub="NW", timeline=[{"deadline": "2026-10-20 23:59:59"}]),
        "坏数据",
    ]
    settings = {"subjects": ["AI"], "ranks": ["A", "B"], "days": 45}
    found = deadlines.entries(data, datetime(2026, 10, 12, 3, 30), settings)
    assert [entry["headline"] for entry in found] == [
        "ICML 2027 论文截稿",
        "PTCONF 2027 论文截稿",
        "CVPR 2027 论文截稿",
    ]
    icml, pt, cvpr = found
    assert icml["when"] == "10月20日" and "Regular round的论文提交截止时间为北京时间10月20日 12:00" in icml["body"]
    assert "北京时间10月31日 14:59" in pt["body"]  # 太平洋夏令时 UTC-7
    assert cvpr["body"] == (
        "CVPR Conference（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，"
        "摘要截止时间为11月11日 19:59。会议将于 June 20-25, 2027 在 Seattle, USA 举行。"
    )
    assert cvpr["url"] == "https://cvpr.org" and cvpr["via"] == "会议官网" and cvpr["cat"] == "events"


def test_deadline_timezones():
    assert deadlines.to_beijing("2026-12-01 23:59:59", "UTC-12") == datetime(2026, 12, 2, 19, 59, 59)
    assert deadlines.to_beijing("2026-12-01 23:59:59", "UTC") == datetime(2026, 12, 2, 7, 59, 59)
    assert deadlines.to_beijing("2026-12-01 23:59:59", "PT") == datetime(2026, 12, 2, 15, 59, 59)  # 冬令时 UTC-8
    assert deadlines.to_beijing("2026-12-01 23:59:59", "CET") is None


# ------------------------------------------------------------------ 俱乐部动态
DASHBOARD = "https://osd.example"
SETTINGS = {
    "name": "开源俱乐部",
    "org": "club-org",
    "dashboard": DASHBOARD,
    "exclude": ["weekly-tech-agent"],
    "top_repos": 2,
    "release_repos": 3,
}


def repo(name, merged=0, commits=0, prs=0, people=1, active=True, sig="Agent SIG", added=10):
    return {
        "name": name,
        "url": f"https://github.com/club-org/{name}",
        "sig": {"name": sig},
        "new_prs": prs,
        "closed_merged_prs": merged,
        "new_issues": 1,
        "new_commits": commits,
        "lines_added": added,
        "lines_deleted": 1,
        "active_contributors": people,
        "is_active": active,
    }


def club_routes(github=None):
    api = f"{DASHBOARD}/api/v1"
    repos = [
        repo("busy", merged=5, commits=9, prs=6, people=3),
        repo("quiet", merged=0, commits=2, prs=0, people=1),
        repo("weekly-tech-agent", merged=9, commits=30, prs=9, people=1),  # 本项目自己，不计入
        repo("bot-only", merged=4, commits=4, prs=4, people=0),  # 只有机器人在动
        repo("idle", active=False, people=0),
        repo("../evil", merged=1, commits=1, prs=1, people=1),  # 名字不正常：不拿去拼接口路径
    ]
    routes = {
        f"{api}/organization/growth-analysis": {"period": {"current": {"start": "2026-10-05", "end": "2026-10-11"}}},
        f"{api}/organization/repositories": {"range": "7d", "repositories": repos},
        f"{api}/contributors/stats": {"unique_contributors": 4, "new_contributors": 1},
    }
    return {**routes, **(github or {})}


def test_club_summary_counts_without_excluded_repositories():
    github = {
        "https://api.github.com/orgs/club-org/repos": [
            {
                "name": "fresh",
                "created_at": "2026-10-07T02:00:00Z",
                "html_url": "https://github.com/club-org/fresh",
                "description": "新的仓库",
                "fork": False,
                "private": False,
            },
            {"name": "old", "created_at": "2026-09-01T02:00:00Z", "html_url": "https://github.com/club-org/old"},
            {"name": "forked", "created_at": "2026-10-07T02:00:00Z", "fork": True},
        ],
        "https://api.github.com/repos/club-org/busy/releases": [
            {
                "tag_name": "v1.2.0",
                "name": "Autumn",
                "published_at": "2026-10-09T08:00:00Z",
                "html_url": "https://github.com/club-org/busy/releases/tag/v1.2.0",
            },
            {"tag_name": "v1.3.0-rc", "published_at": "2026-10-10T08:00:00Z", "draft": True},
            {"tag_name": "v1.1.0", "published_at": "2026-09-20T08:00:00Z"},
        ],
    }
    ctx = context(club_routes(github), now=NOW)
    entries, period = club.fetch(ctx, SETTINGS, MONDAY, SUNDAY, 8)
    assert period == {"start": "2026-10-05", "end": "2026-10-11"}
    summary, busy, quiet, fresh, release = entries
    assert summary["headline"] == "开源俱乐部一周合并 9 个 PR、提交 15 次"
    assert summary["when"] == "10月5日至11日"
    assert summary["body"] == (
        "据俱乐部开源仪表盘统计，开源俱乐部跟踪的 4 个仓库中有 2 个有人参与开发，共新增 PR 10 个、合并 9 个，"
        "提交 15 次，新增代码 40 行、删除 4 行，4 位贡献者参与，其中 1 位是第一次贡献。"
    )
    assert summary["url"] == "https://osd.example/"
    assert busy["headline"] == "busy 一周合并 5 个 PR" and "Agent SIG的 busy 仓库" in busy["body"]
    assert quiet["headline"] == "quiet 一周提交 2 次"
    assert fresh["headline"] == "俱乐部新建 fresh 仓库" and fresh["when"] == "10月7日" and "新的仓库" in fresh["body"]
    assert release["headline"] == "busy 发布 v1.2.0" and release["body"] == "busy 发布新版本 v1.2.0（Autumn）。"
    assert not any("evil" in str(entry) for entry in entries)  # 名字不正常的仓库整个不要
    assert not any("evil" in call["url"] for call in ctx.http.calls)


def test_club_keeps_the_statistics_when_github_fails_and_raises_when_the_dashboard_fails():
    entries, _ = club.fetch(context(club_routes(), now=NOW), SETTINGS, MONDAY, SUNDAY, 8)  # GitHub 全是 404
    assert len(entries) == 3  # 周统计和两个最活跃的仓库
    with pytest.raises(HttpError):
        club.fetch(context({}, now=NOW), SETTINGS, MONDAY, SUNDAY, 8)


# ------------------------------------------------------------------ 生成一期
def story(n, *, section="news", day=6, score=5.0, **kwargs):
    url = kwargs.pop("url", f"https://example.com/{section}/{n}")
    base = {
        "title": f"Story {n} about Qwen4",
        "url": url,
        "source": "rss",
        "section": section,
        "via": "Example",
        "published": to_iso(datetime(2026, 10, day, 2, tzinfo=UTC)),
        "summary": f"Alibaba released Qwen4 for story {n}, with a 1M context window.",
        "score": score,
        "id": item_id(url),
        "title_zh": f"第 {n} 条的中文标题",
        "summary_zh": f"第 {n} 条的中文摘要。",
    }
    return Item(**{**base, **kwargs})


CLUB = {"cat": "club", "headline": "俱乐部一周合并 3 个 PR", "when": "10月5日至11日", "date": "2026-10-11",
        "body": "统计。", "url": "https://osd.example/", "via": "俱乐部开源仪表盘"}  # fmt: skip
EVENT = {"cat": "events", "headline": "CVPR 2027 论文截稿", "when": "11月17日", "date": "2026-11-17",
         "body": "截稿。", "url": "https://cvpr.org", "via": "会议官网"}  # fmt: skip


@pytest.fixture
def week(tmp_path, config, monkeypatch):
    """一周的日报数据，外部数据源都换成假的。"""
    root = tmp_path
    days = {
        date(2026, 10, 6): [story(1, score=9), story(2, score=4, title="通义千问发布 Qwen4", via="量子位")],
        date(2026, 10, 8): [story(3, section="opensource", day=1, score=7), story(4, section="papers", score=6)],
    }
    for day, items in days.items():
        payload = {"date": day.isoformat(), "llm": {"model": "daily-model"}, "items": [i.to_dict() for i in items]}
        store.save_day(root, day, payload)
    calls = {"club": 0}

    def fake_club(ctx, settings, monday, sunday, offset):
        calls["club"] += 1
        return [CLUB], {"start": "2026-10-05", "end": "2026-10-11"}

    gov_item = Item(
        title="国务院关于人工智能的意见",
        url="https://www.gov.cn/zhengce/1.htm",
        source="policy",
        section="news",
        via="中国政府网",
        published=to_iso("2026-10-07T00:00:00+08:00"),
        id=item_id("https://www.gov.cn/zhengce/1.htm"),
        extra={"kx_day": "2026-10-07"},
    )
    monkeypatch.setattr(club, "fetch", fake_club)
    monkeypatch.setattr(policy, "fetch", lambda http, monday, sunday, settings: [Item.from_dict(gov_item.to_dict())])
    monkeypatch.setattr(deadlines, "fetch", lambda http, now, settings: [dict(EVENT)])
    page = (
        "国务院印发关于人工智能的意见，部署六项重点任务，推动人工智能与实体经济深度融合，"
        "培育新质生产力，到 2030 年形成完善的产业生态。"
    )
    monkeypatch.setattr(excerpt, "fetch", lambda http, url: page)
    return root, config, calls


def build(root, config, client=None, **kwargs):
    return kuaixun.build(root, config, MONDAY, client=client, http=FakeHttp({}), env={}, now=NOW, **kwargs)


def by_cat(issue):
    found = {}
    for entry in issue["entries"]:
        found.setdefault(entry["cat"], []).append(entry)
    return found


def test_without_a_model_the_issue_uses_the_daily_chinese(week):
    root, config, _ = week
    issue = build(root, config)
    assert [entry["cat"] for entry in issue["entries"]] == [
        "club",
        "policy",
        "domestic",
        "overseas",
        "opensource",
        "papers",
        "events",
    ]
    cats = by_cat(issue)
    assert cats["overseas"][0]["headline"] == "第 1 条的中文标题" and cats["overseas"][0]["when"] == "10月6日"
    assert cats["domestic"][0]["headline"] == "第 2 条的中文标题"  # 原标题是中文：算国内
    assert cats["opensource"][0]["when"] == "10月8日消息"  # 发布日期不在这一周：写日报登出那天的消息
    assert cats["policy"][0]["body"] == "据中国政府网消息：国务院关于人工智能的意见。"
    assert issue["pending"] == 5 and issue["tries"] == 0 and issue["written"] == {}
    assert issue["models"] == ["daily-model"] and issue["club_period"]["end"] == "2026-10-11"
    assert [source["ok"] for source in issue["sources"]] == [True, True, True]


def kx_reply(rows_by_title):
    """假大模型：按原标题给出预设的快讯写法，没写到的条目给 skip。"""

    def reply(sent):
        out = []
        for row in sent["items"]:
            written = rows_by_title.get(row["title"], {"cat": "skip"})
            out.append({"i": row["i"], **written})
        return {"items": out}

    return reply


def test_model_sorts_rewrites_and_drops_duplicates(week):
    root, config, _ = week
    replies = {
        "Story 1 about Qwen4": {
            "cat": "domestic",
            "headline": "阿里巴巴发布Qwen4模型",
            "body": "10月6日，Qwen4 支持 1M 上下文。",
        },
        "通义千问发布 Qwen4": {"cat": "domestic", "headline": "通义千问发布Qwen4", "body": "同一件事。", "same": 0},
        "Story 3 about Qwen4": {"cat": "overseas", "headline": "Qwen4 开源 GPT-9 版本", "body": "It is open."},
        "Story 4 about Qwen4": {"cat": "papers", "headline": "Qwen4 技术报告", "body": "论文介绍了 Qwen4。"},
        "国务院关于人工智能的意见": {
            "cat": "domestic",
            "headline": "国务院印发人工智能意见",
            "body": "部署六项重点任务。",
        },
    }
    client = FakeClient([kx_reply(replies)])
    issue = build(root, config, client)
    cats = by_cat(issue)
    assert cats["domestic"] == [
        {
            "cat": "domestic",
            "headline": "阿里巴巴发布Qwen4模型",
            "when": "10月6日",
            "date": "2026-10-06",
            "body": "Qwen4 支持 1M 上下文。",  # 模型自己写的日期去掉，由程序加
            "url": "https://example.com/news/1",
            "via": "Example",
            "id": item_id("https://example.com/news/1"),
            "ai": True,
        }
    ]  # 第 2 条和第 1 条是同一件事，不登
    opensource = cats["opensource"][0]  # 开源圈的条目只能留在开源项目，大模型给的 overseas 不算
    assert opensource["headline"] == "第 3 条的中文标题"  # 写出了资料里没有的 GPT-9：退回日报的中文标题
    assert opensource["body"] == "第 3 条的中文摘要。"  # 正文没写成中文：退回日报的摘要
    assert cats["papers"][0]["headline"] == "Qwen4 技术报告"
    assert cats["policy"][0]["headline"] == "国务院印发人工智能意见"  # 政府网的条目只能进政策动向
    assert "overseas" not in cats
    assert issue["pending"] == 0 and issue["tries"] == 1 and issue["models"] == ["daily-model", "fake-1"]
    assert all(row.get("section") for call in client.calls for row in call["items"])
    policy_rows = [row for call in client.calls for row in call["items"] if row["source"] == "中国政府网"]
    assert "部署六项重点任务" in policy_rows[0]["text"]  # 政策条目先到原文网页取了一段，给大模型当资料

    save_week_note(root, "2026-W41", {"kuaixun": issue})
    again = build(root, config, FakeClient([]))  # 重新生成：写好的直接沿用，不再请求
    assert again["entries"] == issue["entries"] and again["tries"] == 1  # 没有要写的：不算补了一次
    fresh = FakeClient([kx_reply({})])
    build(root, config, fresh, reuse=False)  # --rewrite：全部重写
    assert len(fresh.calls) == 1


def test_an_overloaded_model_leaves_items_pending(week):
    root, config, _ = week
    issue = build(root, config, FakeClient([LLMError("HTTP 429")] * 10))
    assert issue["pending"] == 5 and issue["tries"] == 1 and len(issue["entries"]) == 7  # 照样出刊


def test_caps_limit_each_section(week):
    root, config, _ = week
    config["kuaixun"]["caps"]["overseas"] = 0
    config["kuaixun"]["caps"]["club"] = 0
    cats = by_cat(build(root, config))
    assert "overseas" not in cats and "club" not in cats


def test_failed_sources_keep_what_the_last_run_had(week, monkeypatch):
    root, config, _ = week
    save_week_note(root, "2026-W41", {"kuaixun": build(root, config)})

    def down(*args):
        raise HttpError("HTTP 502", 502)

    for module in (club, policy, deadlines):
        monkeypatch.setattr(module, "fetch", down)
    issue = build(root, config)
    cats = by_cat(issue)
    assert cats["club"] == [CLUB] and cats["events"] == [EVENT] and len(cats["policy"]) == 1
    assert issue["club_period"]["end"] == "2026-10-11"
    assert [source["ok"] for source in issue["sources"]] == [False, False, False]


def test_due(week):
    root, config, _ = week
    tuesday, monday = date(2026, 10, 13), date(2026, 10, 12)
    assert kuaixun.due(root, tuesday, llm_ready=False) == MONDAY  # 还没有：生成
    assert kuaixun.due(root, date(2026, 10, 20), llm_ready=True) is None  # 上一周没有日报

    issue = build(root, config)  # 没有大模型：5 条待补
    save_week_note(root, "2026-W41", {"kuaixun": issue})
    assert kuaixun.due(root, tuesday, llm_ready=False) is None
    assert kuaixun.due(root, tuesday, llm_ready=True) == MONDAY  # 有大模型了：补写
    current = kuaixun.PROMPT_VERSION
    save_week_note(root, "2026-W41", {"kuaixun": {**issue, "tries": kuaixun.MAX_TRIES, "prompt": current}})
    assert kuaixun.due(root, tuesday, llm_ready=True) is None  # 补过几次了，不再试

    stale = {**issue, "pending": 0, "prompt": current, "club_period": {"start": "2026-10-04", "end": "2026-10-10"}}
    save_week_note(root, "2026-W41", {"kuaixun": stale})
    assert kuaixun.due(root, monday, llm_ready=False) == MONDAY  # 周一：俱乐部统计还差一天，再取一次
    assert kuaixun.due(root, tuesday, llm_ready=False) is None  # 过了周一就不再追


def test_assemble_drops_repeats_and_fixes_company_sections():
    def written(n, cat, headline, score):
        item = story(n, score=score)
        item.extra["kx"] = {"cat": cat, "headline": headline, "body": "正文。"}
        return item

    items = [
        written(1, "overseas", "Google 发布 Gemini 4 Argon", 9),
        written(2, "overseas", "Google AI 发布 Gemini 4 Argon 模型", 8),  # 同一件事，另一个来源
        written(3, "domestic", "OpenAI 推出 Rosalind 学术计划", 7),  # 大模型把 OpenAI 分进了国内
        written(4, "opensource", "DeepSeek 开源 V4.1 Flash", 6),  # AI 动态里公司开源的模型进国内动态
        written(5, "overseas", "OpenAI 发布 GPT-6", 5),
        written(6, "overseas", "OpenAI 发布 GPT-6 mini", 4),  # 只差一个词：不算同一件事
    ]
    companies = {"domestic": ["DeepSeek"], "overseas": ["OpenAI", "Google"]}
    chosen = kuaixun.assemble(items, {"domestic": 5, "overseas": 5, "opensource": 5}, MONDAY, SUNDAY, 8, companies)
    assert [entry["headline"] for entry in chosen["overseas"]] == [
        "Google 发布 Gemini 4 Argon",
        "OpenAI 推出 Rosalind 学术计划",
        "OpenAI 发布 GPT-6",
        "OpenAI 发布 GPT-6 mini",
    ]
    assert [(entry["headline"], entry["cat"]) for entry in chosen["domestic"]] == [
        ("DeepSeek 开源 V4.1 Flash", "domestic")
    ]
    assert chosen["opensource"] == []


def test_a_changed_prompt_rewrites_the_issue_once(week):
    root, config, _ = week
    replies = {
        "Story 1 about Qwen4": {"cat": "overseas", "headline": "阿里巴巴发布Qwen4模型", "body": "阿里巴巴发布 Qwen4。"}
    }
    first = build(root, config, FakeClient([kx_reply(replies)]))
    save_week_note(root, "2026-W41", {"kuaixun": {**first, "prompt": "old"}})
    tuesday = date(2026, 10, 13)
    assert kuaixun.due(root, tuesday, llm_ready=True) == MONDAY
    assert kuaixun.due(root, tuesday, llm_ready=False) is None
    kept = build(root, config)  # 没有大模型：沿用旧写法，也不改指纹，等有大模型时再重写
    assert kept["written"] == first["written"] and kept["prompt"] == "old"
    client = FakeClient([kx_reply(replies)])
    again = build(root, config, client)
    assert len(client.calls) == 1 and again["prompt"] == kuaixun.PROMPT_VERSION and again["tries"] == 1


def test_shortlist_keeps_room_for_chinese_news():
    pool = [story(n, score=10 - n) for n in range(1, 5)]
    pool += [story(n, score=1, title=f"国产模型第 {n} 条") for n in range(5, 8)]
    pool.append(story(9, section="papers", score=5))
    picked = kuaixun.shortlist(pool, {"news": 2, "papers": 1}, chinese=2)
    assert [item.title for item in picked] == [
        "Story 1 about Qwen4",
        "Story 2 about Qwen4",
        "Story 9 about Qwen4",
        "国产模型第 5 条",
        "国产模型第 6 条",
    ]
    assert len(kuaixun.shortlist(pool, {"news": 2})) == 2  # 不另外取
