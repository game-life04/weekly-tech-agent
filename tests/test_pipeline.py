"""整条流程的测试：用假的来源代替网络，检查生成的文件。"""

from __future__ import annotations

import json
from datetime import UTC, date, datetime
from types import SimpleNamespace

import pytest
from fakes import FakeClient

from wta import cli, club, collect, deadlines, excerpt, policy, store
from wta.dates import to_iso
from wta.llm import Filtered, LLMError
from wta.models import Item


def fake_source(name, title, items=None, error=None):
    def fetch(config, ctx):
        if error:
            raise RuntimeError(error)
        return [Item(**row) for row in (items or [])]

    return SimpleNamespace(NAME=name, TITLE=title, fetch=fetch)


def row(n, section="news", **kwargs):
    base = {
        "title": f"Item {n} about LLM",
        "url": f"https://example.com/{section}/{n}",
        "source": "",
        "section": section,
        "heat": 0.5,
        "weight": 0.5,
        "published": to_iso(datetime.now(UTC)),
    }
    return {**base, **kwargs}


@pytest.fixture
def repo(tmp_path, monkeypatch):
    (tmp_path / "config.yaml").write_text(
        "sources:\n  good: {enabled: true}\n  broken: {enabled: true}\n  off: {enabled: false}\n"
        "llm: {enabled: false}\n",
        encoding="utf-8",
    )
    (tmp_path / "README.md").write_text(
        "# 每周科技收集 Agent\n\n<!-- wta:latest:start -->\n<!-- wta:latest:end -->\n\n## 关于\n保留这一段。\n",
        encoding="utf-8",
    )
    sources = {
        "good": fake_source(
            "good", "Good", [row(1), row(2, heat=0.9), row(3, section="opensource"), row(4, section="papers")]
        ),
        "broken": fake_source("broken", "Broken", error="network down"),
        "off": fake_source("off", "Off", [row(99)]),
    }
    monkeypatch.setattr(collect, "SOURCES", sources)
    monkeypatch.setattr(cli, "SOURCES", sources)
    monkeypatch.setattr(excerpt, "fetch", lambda http, url: "")  # 测试不访问网络：原文网页一律取不到

    # 快讯的外部数据源也换成假的：俱乐部统计正好覆盖那一周，政策和会议截稿都没有
    def fake_club(ctx, settings, offset, days=7, window=None):
        return [], {"end": (window or (None, date(2026, 10, 11)))[1].isoformat()}

    monkeypatch.setattr(club, "fetch", fake_club)
    monkeypatch.setattr(policy, "fetch", lambda http, monday, sunday, settings: [])
    monkeypatch.setattr(deadlines, "fetch", lambda http, now, settings: [])
    for name in ("GITHUB_STEP_SUMMARY", "GITHUB_ACTIONS"):  # 在 CI 里跑测试时，别往真实的运行小结里写假日报
        monkeypatch.delenv(name, raising=False)
    return tmp_path, sources


def run(root, *args):
    return cli.main(["--root", str(root), *args])


def test_run_writes_data_pages_and_readme(repo):
    root, _ = repo
    assert run(root, "run", "--date", "2026-10-10") == 0

    payload = store.load_day(root, date(2026, 10, 10))
    assert [i["title"] for i in payload["items"]] == [
        "Item 2 about LLM",
        "Item 1 about LLM",
        "Item 3 about LLM",
        "Item 4 about LLM",
    ]
    assert payload["llm"] is None
    assert {s["name"]: s["ok"] for s in payload["sources"]} == {"good": True, "broken": False}
    assert "network down" in payload["sources"][1]["error"]

    daily = (root / "daily/2026/2026-10-10.md").read_text(encoding="utf-8")
    assert "# AI 日报 · 2026-10-10（周六）" in daily and "Item 2 about LLM" in daily
    assert "Item 99" not in daily  # 没启用的来源不抓
    assert "本次未取到：Broken。" in daily
    assert not (root / "weekly/2026-W41.md").exists()  # 快讯要等一周过完才生成
    assert "2026/2026-10-10.md" in (root / "daily/README.md").read_text(encoding="utf-8")
    assert "还没有快讯：每周一生成上一周的一期" in (root / "weekly/README.md").read_text(encoding="utf-8")

    readme = (root / "README.md").read_text(encoding="utf-8")
    assert "## 每日快讯 · 10.10（周六）" in readme and "每周快讯 ·" not in readme
    assert (root / "daily/2026/2026-10-10-kuaixun.md").is_file() and (
        root / "daily/2026/2026-10-10-kuaixun.html"
    ).is_file()
    assert "[今日快讯](2026-10-10-kuaixun.md)" in daily
    assert "保留这一段。" in readme and readme.startswith("# 每周科技收集 Agent")


def test_rerun_same_day_is_stable_and_next_day_skips_old_items(repo):
    root, sources = repo
    assert run(root, "run", "--date", "2026-10-10") == 0
    first = (root / "daily/2026/2026-10-10.md").read_text(encoding="utf-8")
    assert run(root, "run", "--date", "2026-10-10") == 0
    second = store.load_day(root, date(2026, 10, 10))
    assert len(second["items"]) == 4  # 重跑不会重复
    assert first.count("Item 2 about LLM") == 1

    sources["good"] = fake_source("good", "Good", [row(1), row(2), row(5)])
    assert run(root, "run", "--date", "2026-10-11") == 0
    next_day = store.load_day(root, date(2026, 10, 11))
    assert [i["title"] for i in next_day["items"]] == ["Item 5 about LLM"]  # 昨天登过的不再出现
    readme = (root / "README.md").read_text(encoding="utf-8")
    assert "## 每日快讯 · 10.11（周日）" in readme and "10.10（周六）" not in readme
    assert "[上一期](2026-10-10.md)" in (root / "daily/2026/2026-10-11.md").read_text(encoding="utf-8")


def test_all_sources_failing_writes_nothing(repo, monkeypatch):
    root, sources = repo
    sources["good"] = fake_source("good", "Good", error="also down")
    assert run(root, "run", "--date", "2026-10-10") == 2
    assert store.load_day(root, date(2026, 10, 10)) is None
    assert not (root / "daily").exists()


def test_bad_items_are_dropped(repo):
    root, sources = repo
    sources["good"] = fake_source(
        "good",
        "Good",
        [
            row(1),
            row(2, url="javascript:alert(1)"),
            row(3, title="   "),
            row(4, section="gossip"),
        ],
    )
    assert run(root, "run", "--date", "2026-10-10") == 0
    assert [i["title"] for i in store.load_day(root, date(2026, 10, 10))["items"]] == ["Item 1 about LLM"]


def test_papers_keep_more_of_their_abstract(repo):
    root, sources = repo
    long_text = "word " * 600  # 约 3000 字
    sources["good"] = fake_source(
        "good", "Good", [row(1, summary=long_text), row(2, section="papers", summary=long_text)]
    )
    assert run(root, "run", "--date", "2026-10-10") == 0
    lengths = {i["section"]: len(i["summary"]) for i in store.load_day(root, date(2026, 10, 10))["items"]}
    assert lengths == {"news": 600, "papers": 1500}  # 论文要写问题、方法、结果，摘要留得长一些


def test_render_rebuilds_pages_from_data(repo):
    root, _ = repo
    run(root, "run", "--date", "2026-10-10")
    page = root / "daily/2026/2026-10-10.md"
    original = page.read_text(encoding="utf-8")
    page.unlink()
    assert run(root, "render") == 0
    assert page.read_text(encoding="utf-8") == original


def test_check_reports_failures(repo, capsys):
    root, _ = repo
    assert run(root, "check", "good") == 0
    assert "Good（good）4 条" in capsys.readouterr().out
    assert run(root, "check", "broken") == 1
    assert run(root, "check", "nope") == 2


# ---------------------------------------------------------------- 定时任务、大模型、健康检查
def test_if_missing_does_nothing_when_the_day_already_exists(repo):
    root, sources = repo
    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0
    before = (root / "data/2026/2026-10-10.json").read_text(encoding="utf-8")
    sources["good"] = fake_source("good", "Good", error="不应该再抓取")
    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0
    assert (root / "data/2026/2026-10-10.json").read_text(encoding="utf-8") == before


def test_items_of_uncertain_relevance_need_a_model_to_vouch_for_them(repo):
    root, sources = repo
    sources["good"] = fake_source("good", "Good", [row(1), row(2, heat=1.0, extra={"needs_review": True})])
    assert run(root, "run", "--date", "2026-10-10") == 0
    assert [i["title"] for i in store.load_day(root, date(2026, 10, 10))["items"]] == ["Item 1 about LLM"]


LONG = "A long enough description of the item so that a summary may be written from it, about LLM agents."


def llm_replies(score_of, blocked=()):
    """假大模型：打分请求按 score_of 给分；摘要请求给每条写固定的中文。"""

    def reply(sent):
        rows = sent["items"]
        if any(r["title"] in blocked for r in rows):
            return Filtered("sensitive")
        return {
            "items": [
                {
                    "i": r["i"],
                    "score": score_of(r["title"]),
                    "title_zh": f"中文：{r['title']}",
                    "summary_zh": "一句话中文摘要",
                    "tags": ["测试"],
                }
                for r in rows
            ]
        }

    return reply


@pytest.fixture
def with_llm(repo, monkeypatch):
    root, sources = repo
    (root / "config.yaml").write_text(
        "sources:\n  good: {enabled: true}\nselect: {per_source_cap: 9}\nllm: {enabled: true, review_min_score: 7}\n"
        "kuaixun: {daily: {enabled: false}}\n",  # 这些测试数的是日报的请求次数；每日快讯单独测
        encoding="utf-8",
    )

    def install(client):
        monkeypatch.setattr(cli, "build_client", lambda config, env: client)
        return client

    return root, sources, install


def test_model_scores_decide_the_order_and_write_chinese(with_llm):
    root, sources, install = with_llm
    sources["good"] = fake_source(
        "good",
        "Good",
        [
            row(1, heat=0.9, summary=LONG),
            row(2, heat=0.1, summary=LONG),
            row(3, heat=1.0, summary=LONG, extra={"needs_review": True}),
            row(4, heat=1.0, summary=LONG, extra={"needs_review": True}),
        ],
    )
    scores = {"Item 1 about LLM": 2, "Item 2 about LLM": 9, "Item 3 about LLM": 8, "Item 4 about LLM": 3}
    client = install(FakeClient([llm_replies(scores.get)]))
    assert run(root, "run", "--date", "2026-10-10") == 0

    payload = store.load_day(root, date(2026, 10, 10))
    assert [i["title"] for i in payload["items"]] == ["Item 3 about LLM", "Item 2 about LLM", "Item 1 about LLM"]
    assert payload["llm"] == {"provider": "假服务", "model": "fake-1"}
    assert (
        payload["items"][0]["title_zh"] == "中文：Item 3 about LLM"
        and payload["items"][0]["summary_zh"] == "一句话中文摘要"
    )
    daily = (root / "daily/2026/2026-10-10.md").read_text(encoding="utf-8")
    assert "中文：Item 2 about LLM" in daily and "原题：Item 2 about LLM" in daily
    assert "由 AI 生成（fake-1）" in daily and "Item 4" not in daily  # 存疑且分数低的不登
    assert len(client.calls) == 2  # 打分一次、摘要一次

    assert run(root, "run", "--date", "2026-10-10") == 0  # 当天重跑：打过分、写过摘要的不再请求
    assert len(client.calls) == 2
    assert store.load_day(root, date(2026, 10, 10))["llm"] == {"provider": "假服务", "model": "fake-1"}


def test_items_blocked_by_content_filter_are_left_out(with_llm):
    root, sources, install = with_llm
    sources["good"] = fake_source("good", "Good", [row(1, summary=LONG), row(2, summary=LONG), row(3, summary=LONG)])
    install(FakeClient([llm_replies(lambda title: 6, blocked={"Item 2 about LLM"})]))
    assert run(root, "run", "--date", "2026-10-10") == 0
    assert [i["title"] for i in store.load_day(root, date(2026, 10, 10))["items"]] == [
        "Item 1 about LLM",
        "Item 3 about LLM",
    ]


def test_a_crashing_model_never_stops_the_daily_issue(with_llm):
    root, sources, install = with_llm
    sources["good"] = fake_source("good", "Good", [row(1), row(2, extra={"needs_review": True})])
    install(FakeClient([lambda sent: KeyError("意料之外的错误")]))
    assert run(root, "run", "--date", "2026-10-10") == 0
    payload = store.load_day(root, date(2026, 10, 10))
    assert [i["title"] for i in payload["items"]] == ["Item 1 about LLM"] and payload["items"][0]["title_zh"] == ""


def test_health_warns_after_three_failing_days_and_writes_a_step_summary(repo, monkeypatch, capsys, tmp_path):
    root, _ = repo
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    for day in ("2026-10-08", "2026-10-09"):
        assert run(root, "run", "--date", day) == 0
    assert "连续 3 天" not in capsys.readouterr().out
    assert run(root, "run", "--date", "2026-10-10") == 0
    assert "::warning::Broken 已经连续 3 天抓取失败" in capsys.readouterr().out
    text = summary.read_text(encoding="utf-8")
    assert (
        "## 2026-10-10 日报" in text
        and "| Broken | `RuntimeError: network down` |" in text
        and "大模型：未使用" in text
    )


# ---------------------------------------------------------------- 审查后补的回归测试
def test_scheduled_run_uses_the_beijing_date(repo, monkeypatch):
    root, _ = repo

    class FixedClock(datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2026, 10, 14, 19, 17, tzinfo=UTC)  # 定时任务的触发时刻：北京时间 15 日 03:17

    monkeypatch.setattr(cli, "datetime", FixedClock)
    assert run(root, "run") == 0
    assert store.list_days(root) == [date(2026, 10, 15)]
    assert run(root, "run", "--date", "2026-10-16") == 2  # 未来的日期不接受
    assert store.list_days(root) == [date(2026, 10, 15)]


def test_if_missing_retries_an_empty_issue(repo):
    root, sources = repo
    sources["good"] = fake_source("good", "Good", [])
    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0
    assert store.load_day(root, date(2026, 10, 10))["items"] == []
    sources["good"] = fake_source("good", "Good", [row(1)])
    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0  # 上一次是空的：兜底任务要补
    assert len(store.load_day(root, date(2026, 10, 10))["items"]) == 1


def test_if_missing_fills_in_chinese_an_earlier_run_could_not_write(with_llm):
    root, sources, install = with_llm
    sources["good"] = fake_source("good", "Good", [row(1, summary=LONG), row(2, summary=LONG)])
    install(FakeClient([lambda sent: LLMError("HTTP 429：该模型当前访问量过大")]))
    assert run(root, "run", "--date", "2026-10-10") == 0  # 第一次：大模型一直过载，日报照出，只是没有中文
    first = store.load_day(root, date(2026, 10, 10))
    assert first["llm"] is None and not any(i["title_zh"] for i in first["items"])

    sources["good"] = fake_source("good", "Good", error="不应该再抓取")
    client = install(FakeClient([llm_replies(lambda title: 6)]))
    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0  # 后面的定时任务：只补中文
    filled = store.load_day(root, date(2026, 10, 10))
    assert [i["title"] for i in filled["items"]] == [i["title"] for i in first["items"]]  # 内容和顺序不变
    assert all(i["title_zh"].startswith("中文：") for i in filled["items"])
    assert filled["llm"] == {"provider": "假服务", "model": "fake-1"}
    assert filled["generated_at"] == first["generated_at"]
    assert "中文：Item 1 about LLM" in (root / "daily/2026/2026-10-10.md").read_text(encoding="utf-8")
    assert len(client.calls) == 1  # 只写摘要，不重新打分

    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0  # 都补齐了：什么都不做
    assert len(client.calls) == 1


def test_if_missing_repairs_chinese_that_newer_checks_reject(with_llm):
    root, sources, install = with_llm
    sources["good"] = fake_source("good", "Good", [row(1, summary=LONG), row(2, summary=LONG)])
    install(FakeClient([llm_replies(lambda title: 6)]))
    assert run(root, "run", "--date", "2026-10-10") == 0
    path = root / "data/2026/2026-10-10.json"

    def publish_bad_title(index):  # 模拟检查规则改进之前登出去的内容：中文标题里有原标题没有的名称
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["items"][index]["title_zh"] = payload["items"][index]["title"] + "，推出 GPT-9"
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    def rewrite(sent):  # 补写时模型连摘要也换了一句：不应该被采用
        rows = sent["items"]
        return {
            "items": [{"i": r["i"], "title_zh": f"新标题：{r['title']}", "summary_zh": "改写过的摘要"} for r in rows]
        }

    publish_bad_title(0)
    sources["good"] = fake_source("good", "Good", error="不应该再抓取")
    client = install(FakeClient([rewrite]))
    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0
    fixed = store.load_day(root, date(2026, 10, 10))["items"]
    assert fixed[0]["title_zh"] == "新标题：" + fixed[0]["title"]  # 撤下的标题补写了
    assert fixed[0]["summary_zh"] == "一句话中文摘要"  # 核对过的摘要没有被换掉
    assert "GPT-9" not in (root / "daily/2026/2026-10-10.md").read_text(encoding="utf-8")
    assert len(client.calls) == 1 and len(client.calls[0]["items"]) == 1  # 只补写那一条

    publish_bad_title(1)
    assert run(root, "run", "--date", "2026-10-10", "--if-missing", "--no-llm") == 0  # 没有大模型可用时
    assert store.load_day(root, date(2026, 10, 10))["items"][1]["title_zh"] == ""  # 也要撤下来，宁可显示原标题
    assert "GPT-9" not in (root / "daily/2026/2026-10-10.md").read_text(encoding="utf-8")


ARTICLE = "The article explains how the new agent framework works and what it was tested on, in some detail."


def summary_from_text(sent):
    """假大模型：只有给了原文（text 字段）才写摘要。"""
    rows = sent["items"]
    return {
        "items": [
            {
                "i": r["i"],
                "score": 6,
                "title_zh": f"中文：{r['title']}",
                "summary_zh": "依据原文写的摘要" if "text" in r else "",
            }
            for r in rows
        ]
    }


def test_news_without_a_description_is_summarised_from_the_article(with_llm, monkeypatch):
    root, sources, install = with_llm
    sources["good"] = fake_source("good", "Good", [row(1), row(2, url="https://twitter.com/someone/status/1")])
    fetched = []
    monkeypatch.setattr(excerpt, "fetch", lambda http, url: fetched.append(url) or ARTICLE)
    install(FakeClient([summary_from_text]))
    assert run(root, "run", "--date", "2026-10-10") == 0

    items = {i["url"]: i for i in store.load_day(root, date(2026, 10, 10))["items"]}
    assert fetched == ["https://example.com/news/1"]  # 要登录的网站不去取
    assert items["https://example.com/news/1"]["summary_zh"] == "依据原文写的摘要"
    assert items["https://example.com/news/1"]["extra"]["evidence"] == ARTICLE  # 存下来，复查摘要时要用
    assert items["https://twitter.com/someone/status/1"]["summary_zh"] == ""
    daily = (root / "daily/2026/2026-10-10.md").read_text(encoding="utf-8")
    assert "依据原文写的摘要" in daily and ARTICLE not in daily  # 摘录只给大模型看，不登在页面上


def test_later_runs_add_summaries_to_an_issue_published_without_them(with_llm, monkeypatch):
    root, sources, install = with_llm
    sources["good"] = fake_source("good", "Good", [row(1), row(2, url="https://twitter.com/someone/status/1")])
    assert run(root, "run", "--date", "2026-10-10", "--no-llm") == 0  # 出刊时没用上大模型

    monkeypatch.setattr(excerpt, "fetch", lambda http, url: ARTICLE)
    sources["good"] = fake_source("good", "Good", error="不应该再抓取")
    client = install(FakeClient([summary_from_text]))
    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0
    items = {i["url"]: i for i in store.load_day(root, date(2026, 10, 10))["items"]}
    assert items["https://example.com/news/1"]["summary_zh"] == "依据原文写的摘要"
    assert all(i["title_zh"].startswith("中文：") for i in items.values())
    assert len(client.calls) == 1  # 写摘要一次

    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0  # 都处理过了：什么都不做
    assert len(client.calls) == 1


def test_published_memory_reaches_back_exactly_remember_days(repo):
    root, sources = repo
    (root / "config.yaml").write_text(
        "sources:\n  good: {enabled: true}\ndedupe: {remember_days: 3}\nllm: {enabled: false}\n", encoding="utf-8"
    )
    sources["good"] = fake_source("good", "Good", [row(1)])
    assert run(root, "run", "--date", "2026-10-01") == 0
    assert run(root, "run", "--date", "2026-10-04") == 0
    assert store.load_day(root, date(2026, 10, 4))["items"] == []  # 第 3 天：还记得
    assert run(root, "run", "--date", "2026-10-05") == 0
    assert len(store.load_day(root, date(2026, 10, 5))["items"]) == 1  # 第 4 天：不记得了


def test_one_malformed_item_never_takes_down_the_run(repo):
    root, sources = repo
    sources["good"] = fake_source(
        "good",
        "Good",
        [
            row(1),
            row(2, url="https://[broken/x"),
            row(3, metrics={"stars": "1.2k", "points": 7}),
            row(4, extra=None),
            row(5, published=datetime(2026, 10, 9, tzinfo=UTC)),
            row(6, tags=None),
        ],
    )
    assert run(root, "run", "--date", "2026-10-10") == 0
    items = {i["title"]: i for i in store.load_day(root, date(2026, 10, 10))["items"]}
    assert "Item 2 about LLM" not in items and len(items) >= 2  # 坏链接那条被丢掉，其余照常
    assert all(isinstance(v, float) for i in items.values() for v in i["metrics"].values())


def test_broken_readme_markers_are_reported_not_guessed(repo, capsys, monkeypatch):
    root, _ = repo
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    damaged = "# 每周科技收集 Agent\n\n<!-- wta:latest:start -->\n\n## 关于\n保留这一段。\n"
    (root / "README.md").write_text(damaged, encoding="utf-8")
    assert run(root, "run", "--date", "2026-10-10") == 0
    assert (root / "README.md").read_text(encoding="utf-8") == damaged  # 不猜着改
    assert "::warning::README.md 没有更新" in capsys.readouterr().out
    assert (root / "daily/2026/2026-10-10.md").is_file()  # 其他页面照常生成


def test_model_reply_with_a_lone_surrogate_does_not_break_saving(with_llm):
    root, sources, install = with_llm
    sources["good"] = fake_source("good", "Good", [row(1, summary=LONG)])
    broken = chr(0xD83D)
    reply = {
        "items": [
            {"i": 0, "score": 8, "title_zh": "标题" + broken, "summary_zh": "摘要" + broken, "tags": ["测" + broken]}
        ]
    }
    install(FakeClient([lambda sent: reply]))
    assert run(root, "run", "--date", "2026-10-10") == 0
    (item,) = store.load_day(root, date(2026, 10, 10))["items"]
    assert (item["title_zh"], item["summary_zh"], item["tags"]) == ("标题", "摘要", ["测"])


def test_ai_note_follows_the_text_not_the_bookkeeping(with_llm):
    root, sources, install = with_llm
    sources["good"] = fake_source("good", "Good", [row(1, summary=LONG)])
    client = install(FakeClient([llm_replies(lambda title: 8)]))
    client.provider = None  # 服务在写完摘要之后被停用
    assert run(root, "run", "--date", "2026-10-08") == 0
    assert "中文标题和摘要由 AI 生成（fake-1）" in (root / "daily/2026/2026-10-08.md").read_text(encoding="utf-8")

    sources["good"] = fake_source("good", "Good", [row(2)])
    assert run(root, "run", "--date", "2026-10-09", "--no-llm") == 0
    assert "AI 生成" not in (root / "daily/2026/2026-10-09.md").read_text(encoding="utf-8")


# ---------------------------------------------------------------- 每周快讯
class MondayClock(datetime):
    @classmethod
    def now(cls, tz=None):
        return cls(2026, 10, 11, 19, 17, tzinfo=UTC)  # 北京时间 10-12（周一）03:17


def test_monday_run_also_builds_last_weeks_kuaixun(repo, monkeypatch):
    root, sources = repo
    rows = [row(1), row(2, heat=0.9), row(3, section="opensource"), row(4, section="papers")]
    sources["good"] = fake_source("good", "Good", [{**r, "summary": LONG} for r in rows])
    monkeypatch.setattr(cli, "datetime", MondayClock)
    assert run(root, "run", "--date", "2026-10-10") == 0
    page = (root / "weekly/2026-W41.md").read_text(encoding="utf-8")
    assert page.startswith("# 每周科技快讯 · 10.05–10.11") and "Item 2 about LLM" in page
    assert (root / "weekly/2026-W41.html").read_text(encoding="utf-8").startswith("<!doctype html>")
    index = (root / "weekly/README.md").read_text(encoding="utf-8")
    assert "[2026 年第 41 周：Item 2 about LLM](2026-W41.md)（10.05–10.11）" in index  # 第 1 期从 W42 算起
    readme = (root / "README.md").read_text(encoding="utf-8")
    assert readme.index("## 每日快讯 · 10.10（周六）") < readme.index("## 每周快讯 · 10.05–10.11")
    issue = json.loads((root / "data/weekly/2026-W41.json").read_text(encoding="utf-8"))["kuaixun"]
    assert issue["pending"] == 4 and issue["tries"] == 0  # 没有大模型：标题和正文都用日报的
    assert store.list_days(root) == [date(2026, 10, 10)]  # 周记录不算一天

    before = (root / "data/weekly/2026-W41.json").read_text(encoding="utf-8")
    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0  # 没有大模型可用：不重做
    assert (root / "data/weekly/2026-W41.json").read_text(encoding="utf-8") == before


def everything(sent):
    """假大模型：日报的打分、摘要和快讯的写法一起给，各个阶段只取自己要的字段。"""
    return {
        "items": [
            {
                "i": r["i"],
                "score": 6,
                "title_zh": f"中文：{r['title']}",
                "summary_zh": "一句话中文摘要",
                "tags": ["测试"],
                "cat": "overseas",
                "headline": f"测试团队发布{r['title']}",
                "body": "这是快讯正文。",
            }
            for r in sent["items"]
        ]
    }


def test_later_runs_finish_a_kuaixun_written_without_a_model(with_llm, monkeypatch):
    root, sources, install = with_llm
    monkeypatch.setattr(cli, "datetime", MondayClock)
    assert run(root, "run", "--date", "2026-10-10", "--no-llm") == 0
    sources["good"] = fake_source("good", "Good", error="不应该再抓取")
    client = install(FakeClient([everything]))
    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0
    issue = json.loads((root / "data/weekly/2026-W41.json").read_text(encoding="utf-8"))["kuaixun"]
    assert issue["pending"] == 0 and issue["tries"] == 1 and "fake-1" in issue["models"]
    page = (root / "weekly/2026-W41.md").read_text(encoding="utf-8")
    assert "**测试团队发布Item 2 about LLM**<br>" in page and "这是快讯正文。" in page
    assert "AI 根据原文整理" in page
    calls = len(client.calls)  # 日报补中文两次（论文单独一次）、快讯一次
    assert calls == 3

    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0  # 都写好了：什么都不做
    assert len(client.calls) == calls


def test_kuaixun_command(repo, monkeypatch):
    root, _ = repo
    monkeypatch.setattr(cli, "datetime", MondayClock)
    assert run(root, "run", "--date", "2026-10-10", "--no-llm") == 0
    (root / "weekly/2026-W41.md").unlink()
    assert run(root, "kuaixun", "--no-llm") == 0  # 不写 --week 就是上一周
    assert (root / "weekly/2026-W41.md").is_file()
    assert run(root, "kuaixun", "--week", "2026-W42") == 2  # 这一周还没过完
    assert run(root, "kuaixun", "--week", "2026-W39") == 2  # 没有日报数据
    with pytest.raises(SystemExit):
        run(root, "kuaixun", "--week", "2026-10-05")


def test_render_rebuilds_kuaixun_pages_from_data(repo, monkeypatch):
    root, _ = repo
    monkeypatch.setattr(cli, "datetime", MondayClock)
    assert run(root, "run", "--date", "2026-10-10") == 0
    page, html = root / "weekly/2026-W41.md", root / "weekly/2026-W41.html"
    original = page.read_text(encoding="utf-8")
    page.unlink()
    html.unlink()
    (root / "data/weekly/2026-W40.json").write_text(json.dumps({"overview": "旧版周报留下的记录"}), encoding="utf-8")
    assert run(root, "render") == 0
    assert page.read_text(encoding="utf-8") == original and html.is_file()
    assert not (root / "weekly/2026-W40.md").exists()  # 没有快讯的旧记录不生成页面


def test_each_daily_issue_also_gets_a_daily_kuaixun(with_llm):
    root, sources, install = with_llm
    (root / "config.yaml").write_text(
        "sources:\n  good: {enabled: true}\nselect: {per_source_cap: 9}\nllm: {enabled: true}\n", encoding="utf-8"
    )
    sources["good"] = fake_source("good", "Good", [row(1, summary=LONG), row(2, summary=LONG)])
    client = install(FakeClient([everything]))
    assert run(root, "run", "--date", "2026-10-10") == 0
    issue = store.load_day(root, date(2026, 10, 10))["kuaixun"]
    assert issue["kind"] == "daily" and issue["pending"] == 0 and issue["tries"] == 1
    page = (root / "daily/2026/2026-10-10-kuaixun.md").read_text(encoding="utf-8")
    assert page.startswith("# 每日科技快讯 · 10.10") and "## 今日快讯" in page
    assert "**测试团队发布Item 1 about LLM**<br>" in page and "[完整日报（含热度和原题）](2026-10-10.md)" in page
    readme = (root / "README.md").read_text(encoding="utf-8")
    assert "## 每日快讯 · 10.10（周六）" in readme and "测试团队发布Item 2 about LLM" in readme
    assert "[每日快讯](2026/2026-10-10-kuaixun.md)" in (root / "daily/README.md").read_text(encoding="utf-8")

    calls = len(client.calls)
    sources["good"] = fake_source("good", "Good", error="不应该再抓取")
    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0  # 都写好了：什么都不做
    assert len(client.calls) == calls


def test_days_from_before_the_feature_get_a_daily_kuaixun_on_the_next_run(repo):
    root, _ = repo
    assert run(root, "run", "--date", "2026-10-10") == 0
    path = root / "data/2026/2026-10-10.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    del payload["kuaixun"]  # 模拟这个功能上线之前的数据
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    assert run(root, "run", "--date", "2026-10-10", "--if-missing") == 0
    assert "kuaixun" in store.load_day(root, date(2026, 10, 10))
