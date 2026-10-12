"""各个来源的测试：用假网络喂预设数据，检查解析、筛选和出错时的行为。"""

from __future__ import annotations

from datetime import timedelta

import pytest
from fakes import NOW, context

from wta.dates import to_iso
from wta.http import HttpError
from wta.sources import github_new, github_releases, github_trending, hackernews, hot_models, papers, qbitai, rss
from wta.sources._github import RateLimited


@pytest.fixture(autouse=True)
def no_waiting(monkeypatch):
    """来源里为了礼貌而加的等待，在测试里全部跳过。"""
    for module in (github_trending, github_new, papers):
        monkeypatch.setattr(module.time, "sleep", lambda seconds: None)
    monkeypatch.setattr(papers, "ARXIV_INTERVAL", 0)


def ts(hours_ago: float) -> int:
    return int((NOW - timedelta(hours=hours_ago)).timestamp())


# ------------------------------------------------------------------ Hacker News
def hn_routes(hits, newest_hours_ago=0.2):
    return {
        f"{hackernews.API}/search_by_date": {"hits": [{"created_at_i": ts(newest_hours_ago)}]},
        f"{hackernews.API}/search": {"hits": hits},
    }


def test_hackernews_keeps_related_stories_and_flags_big_unrelated_ones():
    hits = [
        {
            "objectID": "1",
            "title": "New LLM beats everything",
            "url": "https://a.com/llm",
            "points": 300,
            "num_comments": 120,
            "created_at_i": ts(5),
        },
        {
            "objectID": "2",
            "title": "The Mathocalypse",
            "url": "https://b.com/math",
            "points": 400,
            "created_at_i": ts(6),
        },
        {
            "objectID": "3",
            "title": "A boring database post",
            "url": "https://c.com/db",
            "points": 90,
            "created_at_i": ts(7),
        },
        {"objectID": "4", "title": "Ask HN: how do you use AI agents?", "points": 60, "created_at_i": ts(8)},
        {
            "objectID": "5",
            "title": "New LLM beats everything!",
            "url": "https://mirror.com/llm",
            "points": 40,
            "created_at_i": ts(9),
        },
        {"objectID": "6", "title": "", "points": 500, "created_at_i": ts(1)},
    ]
    ctx = context(hn_routes(hits))
    items = hackernews.fetch({"review_points": 250}, ctx)
    assert [i.title for i in items] == [
        "New LLM beats everything",
        "The Mathocalypse",
        "Ask HN: how do you use AI agents?",
    ]
    llm, math, ask = items
    assert llm.metrics == {"points": 300, "comments": 120} and llm.extra == {
        "discussion": hackernews.ITEM_URL.format("1")
    }
    assert llm.published == to_iso(ts(5)) and llm.section == "news" and 0 < llm.heat < 1
    assert math.extra["needs_review"] is True  # 标题里没有关键词但分数很高：交给大模型判断
    assert ask.url == hackernews.ITEM_URL.format("4")  # 没有外链的帖子，链接指向讨论页
    query = ctx.http.calls[1]["params"]["numericFilters"]
    assert f"created_at_i>{ts(48)}" in query and "points>=20" in query


def test_hackernews_refuses_a_stale_index():
    with pytest.raises(RuntimeError, match="没有更新"):
        hackernews.fetch({}, context(hn_routes([], newest_hours_ago=10)))
    with pytest.raises(RuntimeError, match="格式不对"):
        hackernews.fetch({}, context({**hn_routes([]), f"{hackernews.API}/search": {"message": "oops"}}))


# -------------------------------------------------------------------------- RSS
def rss_feed(*entries: tuple[str, str, float | None, str]) -> str:
    items = ""
    for title, link, hours_ago, description in entries:
        date = (
            f"<pubDate>{(NOW - timedelta(hours=hours_ago)).strftime('%a, %d %b %Y %H:%M:%S GMT')}</pubDate>"
            if hours_ago is not None
            else ""
        )
        items += f"<item><title>{title}</title><link>{link}</link>{date}<description>{description}</description></item>"
    return f'<?xml version="1.0"?><rss version="2.0"><channel><title>T</title>{items}</channel></rss>'


def test_rss_expand_gives_each_feed_its_own_unit():
    units = rss.expand(
        {"max_age_hours": 24, "feeds": [{"name": "甲", "url": "u1"}, {"name": "乙", "url": "u2", "max_age_hours": 96}]}
    )
    assert [(name, title) for name, title, _ in units] == [("rss:甲", "甲"), ("rss:乙", "乙")]
    assert units[0][2]["max_age_hours"] == 24 and units[1][2]["max_age_hours"] == 96
    assert rss.expand({}) == []


def test_rss_filters_by_age_relevance_and_cap():
    feed = rss_feed(
        ("New AI model", "https://x.com/1", 2, "about a model"),
        ("Cooking tips", "https://x.com/2", 3, "nothing relevant"),
        ("No date", "https://x.com/3", None, "AI"),
        ("LLM agents everywhere", "https://x.com/4", 5, "more"),
        ("Yet another AI story", "https://x.com/5", 6, "more"),
        ("Old AI news", "https://x.com/6", 100, "old"),
    )
    config = {
        "name": "测试源",
        "url": "https://x.com/feed",
        "max_age_hours": 48,
        "max_items": 2,
        "only_related": True,
        "weight": 0.7,
        "section": "opensource",
    }
    items = rss.fetch(config, context({"https://x.com/feed": feed}))
    assert [i.title for i in items] == [
        "New AI model",
        "LLM agents everywhere",
    ]  # 无关的、没日期的、太旧的、超出名额的都不要
    first = items[0]
    assert (first.via, first.section, first.heat, first.weight) == ("测试源", "opensource", 0.7, 0.7)
    assert first.summary == "about a model" and first.published == to_iso(NOW - timedelta(hours=2))


def test_rss_title_match_no_summary_and_future_dates():
    feed = rss_feed(
        ("科技爱好者周刊（第 414 期）", "https://r.com/414", -30, "正文"), ("另一篇", "https://r.com/x", 1, "正文")
    )
    config = {
        "name": "周刊",
        "url": "https://r.com/feed",
        "max_age_hours": 72,
        "title_match": "科技爱好者周刊",
        "no_summary": True,
    }
    (item,) = rss.fetch(config, context({"https://r.com/feed": feed}))
    assert item.title == "科技爱好者周刊（第 414 期）" and item.summary == ""
    assert item.published == to_iso(NOW)  # 写到未来的日期按“现在”算


def test_rss_empty_or_broken_feed_is_an_error():
    config = {"name": "空", "url": "https://e.com/feed", "max_age_hours": 48}
    with pytest.raises(RuntimeError, match="一条内容都没有"):
        rss.fetch(config, context({"https://e.com/feed": rss_feed()}))
    with pytest.raises(ValueError, match="网页"):
        rss.fetch(config, context({"https://e.com/feed": "<html><body>blocked</body></html>"}))


# ----------------------------------------------------------------------- 量子位
def test_qbitai_maps_posts_and_drops_old_ones():
    posts = [
        {
            "date_gmt": (NOW - timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%S"),
            "link": "https://www.qbitai.com/1.html",
            "title": {"rendered": "大模型新进展"},
            "excerpt": {"rendered": "<p>一句话摘要</p>"},
        },
        {
            "date_gmt": (NOW - timedelta(hours=80)).strftime("%Y-%m-%dT%H:%M:%S"),
            "link": "https://www.qbitai.com/2.html",
            "title": {"rendered": "旧文章"},
            "excerpt": {"rendered": ""},
        },
    ]
    (item,) = qbitai.fetch({}, context({qbitai.API: posts}))
    assert (item.title, item.summary, item.section) == ("大模型新进展", "<p>一句话摘要</p>", "news")
    assert item.published == to_iso(NOW - timedelta(hours=3))
    with pytest.raises(RuntimeError):
        qbitai.fetch({}, context({qbitai.API: {"code": "rest_no_route"}}))


# -------------------------------------------------------------- GitHub Trending
def trending_page(*repos: tuple[str, str, str, str, str]) -> str:
    articles = ""
    for name, description, language, stars, gained in repos:
        articles += f"""
        <article class="Box-row">
          <h2 class="h3"><a href="/{name}" data-view-component="true"> {name.replace("/", " / ")} </a></h2>
          <p class="col-9">{description}</p>
          <div><span itemprop="programmingLanguage">{language}</span>
            <a href="/{name}/stargazers"><svg></svg> {stars}</a> <a href="/{name}/forks">12</a>
            <span><svg></svg> {gained} stars today</span></div>
        </article>"""
    return f"<html><body><a href='/login'>Sign in</a>{articles}</body></html>"


def test_trending_parser_reads_the_semantic_markers():
    page = trending_page(
        ("octo/agent-kit", "Build AI agents &amp; tools", "Python", "12,345", "1,024"), ("x/y", "", "", "7", "1")
    )
    assert github_trending.parse_trending(page) == [
        {
            "name": "octo/agent-kit",
            "description": "Build AI agents & tools",
            "language": "Python",
            "stars": 12345,
            "gained": 1024,
        },
        {"name": "x/y", "description": "", "language": "", "stars": 7, "gained": 1},
    ]
    assert github_trending.parse_trending("<html><body>redesigned</body></html>") == []


def test_trending_merges_lists_keeps_related_repos_and_survives_one_bad_list():
    routes = {
        github_trending.URL: trending_page(
            ("octo/agent-kit", "Build AI agents", "Python", "12,345", "1,024"),
            ("games/tetris", "A classic game", "C", "900", "300"),
        ),
        f"{github_trending.URL}/python": trending_page(
            ("octo/agent-kit", "Build AI agents", "Python", "12,345", "1,024"),
            ("py/llm-tool", "Run LLMs locally", "Python", "50", "20"),
        ),
        f"{github_trending.URL}/rust": HttpError("HTTP 503"),
    }
    items = github_trending.fetch({"languages": ["", "python", "rust"]}, context(routes))
    assert sorted(i.title for i in items) == ["octo/agent-kit", "py/llm-tool"]
    kit = next(i for i in items if i.title == "octo/agent-kit")
    assert kit.url == "https://github.com/octo/agent-kit" and kit.metrics == {"stars_today": 1024, "stars": 12345}
    assert kit.summary == "Build AI agents" and kit.extra == {"language": "Python"}

    with pytest.raises(RuntimeError, match="一个仓库都没解析出来"):
        github_trending.fetch({"languages": [""]}, context({github_trending.URL: "<html>redesigned</html>"}))


# ------------------------------------------------------------- GitHub 版本发布
@pytest.mark.parametrize(
    ("tag", "prefix", "version", "pre", "calver"),
    [
        ("v1.2.3", "v", (1, 2, 3), False, False),
        ("langchain-core==1.6.9", "langchain-core==", (1, 6, 9), False, False),
        ("rust-v0.163.0-alpha.5", "rust-v", (0, 163, 0), True, False),
        ("v2.0.0rc1", "v", (2, 0, 0), True, False),
        ("v0.1.905-beta", "v", (0, 1, 905), True, False),
        ("2026-07-28", "", (2026, 7, 28), False, True),
        ("v2026.10.1", "v", (2026, 10, 1), False, True),
        ("nightly", "nightly", None, True, False),
        ("b11556", "b11556", None, False, False),
    ],
)
def test_parse_tag(tag, prefix, version, pre, calver):
    parsed = github_releases.parse_tag(tag)
    assert (parsed["prefix"], parsed["version"], parsed["pre"], parsed["calver"]) == (prefix, version, pre, calver)


def release(tag, days_ago, prerelease=False, body="notes", draft=False):
    return {
        "tag_name": tag,
        "prerelease": prerelease,
        "draft": draft,
        "body": body,
        "published_at": to_iso(NOW - timedelta(days=days_ago)),
        "html_url": f"https://github.com/o/r/releases/tag/{tag}",
    }


def levels(tags, **kwargs):
    releases = [{"tag": t, "prerelease": False} for t in tags]
    return {r["tag"]: (r["kind"], r["level"]) for r in github_releases.classify(releases, **kwargs)}


def test_classify_compares_with_older_releases_of_the_same_series():
    assert levels(["v2.6.25", "v3.0.2", "v3.0.1", "v3.0.0", "v2.6.24", "v2.5.0"]) == {
        "v2.6.25": ("stable", "patch"),  # 新版本之后才发的旧分支补丁，不算次版本
        "v3.0.2": ("stable", "patch"),
        "v3.0.1": ("stable", "patch"),
        "v3.0.0": ("stable", "major"),
        "v2.6.24": ("stable", "minor"),
        "v2.5.0": ("stable", "minor"),  # 没有更早的可比：x.y.0 算次版本
    }
    assert levels(["v1.3.0-rc1", "nightly", "v1.2.0"]) == {
        "v1.3.0-rc1": ("pre", None),
        "nightly": ("other", None),
        "v1.2.0": ("stable", "minor"),
    }
    monorepo = levels(["langchain-core==1.6.9", "langchain==1.4.0", "langchain==1.3.2"], tag_regex=r"^langchain==\d")
    assert monorepo["langchain-core==1.6.9"] == ("other", None) and monorepo["langchain==1.4.0"] == ("stable", "minor")
    assert levels(["v0.2.0-beta", "v0.1.0-beta"], trust_flag_only=True)["v0.2.0-beta"] == ("stable", "minor")
    assert levels(["2026-07-28"])["2026-07-28"] == ("stable", "calver")


def test_releases_reports_only_notable_new_versions():
    routes = {
        "https://api.github.com/repos/o/minor/releases": [
            release("v1.3.0", 1, body="## What's new\n- streaming"),
            release("v1.2.9", 9),
        ],
        "https://api.github.com/repos/o/patch/releases": [release("v1.2.10", 1), release("v1.2.9", 9)],
        "https://api.github.com/repos/o/old/releases": [release("v2.0.0", 30), release("v1.9.0", 60)],
        "https://api.github.com/repos/o/draft/releases": [release("v9.0.0", 1, draft=True), release("v8.0.0", 40)],
        "https://api.github.com/repos/o/busy/releases": [release(f"v1.{n}.0", 30 - n) for n in range(29, 14, -1)],
    }
    config = {"repos": ["o/minor", "o/patch", "o/old", "o/draft", "o/busy", "o/gone"], "days": 3, "weight": 0.7}
    ctx = context(routes, env={"GITHUB_TOKEN": "t0ken"})
    (item,) = github_releases.fetch(config, ctx)
    assert item.title == "o/minor v1.3.0" and item.url.endswith("/releases/tag/v1.3.0")
    assert item.summary == "次版本更新" and item.extra == {"evidence": "## What's new - streaming", "level": "minor"}
    assert (item.section, item.weight, item.heat) == ("opensource", 0.7, 0.65)
    assert all(call["headers"]["Authorization"] == "Bearer t0ken" for call in ctx.http.calls)  # 令牌只发给官方接口


def test_releases_asks_for_latest_when_prereleases_hide_the_stable_one():
    builds = [release(f"b{n}", 0.01 * n, prerelease=True) for n in range(30)]
    routes = {
        "https://api.github.com/repos/o/r/releases/latest": release("v0.6.0", 1),
        "https://api.github.com/repos/o/r/releases": builds,
    }
    (item,) = github_releases.fetch({"repos": [{"repo": "o/r"}]}, context(routes))
    assert item.title == "o/r v0.6.0"


def test_releases_stops_on_rate_limit_and_fails_when_nothing_works():
    limited = context({"https://api.github.com/": HttpError("HTTP 403", 403, rate_limited=True)})
    with pytest.raises(RateLimited):
        github_releases.fetch({"repos": ["o/a", "o/b"]}, limited)
    assert len(limited.http.calls) == 1  # 额度没了就不再试后面的仓库
    with pytest.raises(RuntimeError, match="全部读取失败"):
        github_releases.fetch({"repos": ["o/a"]}, context({"https://api.github.com/": HttpError("HTTP 500", 500)}))


# --------------------------------------------------------------- GitHub 新项目
def test_github_new_merges_queries_and_ranks_by_stars_per_day():
    def search(url, params):
        base = [
            {
                "full_name": "a/llm-router",
                "html_url": "https://github.com/a/llm-router",
                "description": "Route LLM calls",
                "stargazers_count": 3000,
                "created_at": to_iso(NOW - timedelta(days=3)),
                "language": "Go",
            }
        ]
        if params["q"].startswith("topic:mcp"):
            base.append(
                {
                    "full_name": "b/gym-tracker",
                    "html_url": "https://github.com/b/gym-tracker",
                    "description": "Track workouts",
                    "stargazers_count": 9000,
                    "created_at": to_iso(NOW - timedelta(days=2)),
                    "language": "Dart",
                }
            )
        if params["q"].startswith("topic:llm"):
            raise HttpError("HTTP 422", 422)
        return {"items": base}

    ctx = context({"https://api.github.com/search/repositories": search})
    (item,) = github_new.fetch({"topics": ["llm", "mcp"], "days": 30}, ctx)
    assert item.title == "a/llm-router"  # 贴了话题标签但简介和 AI 无关的仓库不要
    assert item.metrics == {"stars": 3000} and item.extra == {"language": "Go", "age_days": 3}
    assert len(ctx.http.calls) == 3 and "created:>=2026-09-11 stars:>=100" in ctx.http.calls[0]["params"]["q"]

    with pytest.raises(RuntimeError, match="都失败了"):
        github_new.fetch({"topics": ["llm"]}, context({"https://api.github.com/": HttpError("HTTP 500", 500)}))


# -------------------------------------------------------------------- 热门模型
def test_hot_models_filters_repacks_and_unwanted_models():
    models = [
        {
            "id": "Qwen/Qwen3-8B",
            "likes": 1500,
            "downloads": 90000,
            "pipeline_tag": "text-generation",
            "tags": ["license:apache-2.0"],
            "createdAt": "2026-10-09T00:00:00.000Z",
        },
        {"id": "someone/Qwen3-8B-GGUF", "likes": 900, "tags": ["base_model:quantized:Qwen/Qwen3-8B"]},
        {"id": "Qwen/Qwen3-8B-GGUF", "likes": 800, "tags": ["base_model:quantized:Qwen/Qwen3-8B"]},
        {"id": "x/Model-Uncensored", "likes": 700, "tags": []},
        {"id": "y/clean", "likes": 5, "tags": ["not-for-all-audiences"]},
    ]
    units = hot_models.expand({"max_items": 8, "weight": 0.5})
    assert [title for _, title, _ in units] == ["Hugging Face 热门模型", "魔搭 ModelScope 热门模型"]
    assert [name for name, _, _ in hot_models.expand({"modelscope": False})] == ["hot_models:huggingface"]

    items = hot_models.fetch(units[0][2], context({hot_models.HF_API: models}))
    assert [i.title for i in items] == ["Qwen/Qwen3-8B", "Qwen/Qwen3-8B-GGUF"]  # 同一作者自己的量化版保留
    first = items[0]
    assert first.summary == "文本生成模型，许可证 apache-2.0" and first.via == "Hugging Face 热门模型"
    assert first.extra["links"] == [["国内镜像", "https://hf-mirror.com/Qwen/Qwen3-8B"]] and first.weight == 0.5

    scope = {
        "success": True,
        "data": {
            "models": [
                {
                    "id": "iic/SenseVoice",
                    "likes": 300,
                    "downloads": 10,
                    "tasks": ["auto-speech-recognition"],
                    "created_at": "2026-10-01T00:00:00Z",
                    "description": "",
                }
            ]
        },
    }
    (item,) = hot_models.fetch(units[1][2], context({hot_models.MODELSCOPE_API: scope}))
    assert item.url == "https://www.modelscope.cn/models/iic/SenseVoice" and item.via == "魔搭 ModelScope 热门模型"
    with pytest.raises(RuntimeError):
        hot_models.fetch(units[1][2], context({hot_models.MODELSCOPE_API: {"success": False, "code": 500}}))


# ------------------------------------------------------------------------ 论文
def hf_row(paper_id, title, upvotes, code=None):
    return {
        "paper": {
            "id": paper_id,
            "title": title,
            "summary": f"Abstract of {title}",
            "upvotes": upvotes,
            "publishedAt": "2026-10-09T10:00:00.000Z",
            "githubRepo": code,
        }
    }


def arxiv_feed(*entries: tuple[str, str, list[str], str]) -> str:
    body = ""
    for paper_id, title, categories, comment in entries:
        cats = "".join(f'<category term="{c}"/>' for c in categories)
        body += (
            f"<entry><id>http://arxiv.org/abs/{paper_id}v2</id><title>{title}</title><summary>About {title}</summary>"
            f"<published>2026-10-08T12:00:00Z</published>{cats}<arxiv:comment>{comment}</arxiv:comment></entry>"
        )
    return f'<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">{body}</feed>'


PAPERS_CONFIG = {
    "days": 2,
    "categories": ["cs.CL", "cs.AI"],
    "popular": {"top": 10, "min_upvotes": 20, "weight": 0.6},
    "gate_upvotes": 5,
    "watch_weight": 0.8,
    "themes": {"speech": {"title": "语音", "phrases": ["text to speech", "TTS"], "max_items": 2}},
}


def test_papers_popular_lane_and_watch_lane():
    def daily(url, params):
        if params["date"] == "2026-10-11":
            return [
                hf_row("2610.00001", "Popular LLM paper", 150, "https://github.com/a/b"),
                hf_row("2610.00002", "Vision only", 90),
                hf_row("2610.00003", "Too few votes", 3),
            ]
        return [hf_row("2610.00004", "A TTS model", 8)]

    def arxiv(url, params):
        if "id_list" in params:
            return arxiv_feed(
                ("2610.00001", "Popular LLM paper", ["cs.CL"], ""), ("2610.00002", "Vision only", ["cs.CV"], "")
            )
        return arxiv_feed(
            ("2610.00004", "A TTS model", ["cs.CL", "eess.AS"], ""),
            ("2610.00005", "TTS with code", ["cs.CL"], "Code at https://github.com/x/y"),
            ("2610.00006", "TTS nobody noticed", ["cs.CL"], "12 pages"),
        )

    ctx = context({papers.HF_DAILY: daily, papers.ARXIV_API: arxiv})
    items = papers.fetch(PAPERS_CONFIG, ctx)
    assert [(i.via, i.title) for i in items] == [
        ("Hugging Face 热门论文", "Popular LLM paper"),  # 纯视觉的被分类筛掉，点赞太少的不进热门线
        ("arXiv · 语音", "A TTS model"),
        ("arXiv · 语音", "TTS with code"),  # 没人点赞但放了代码，可以进；两样都没有的不进
    ]
    popular, voted, coded = items
    assert popular.url == "https://arxiv.org/abs/2610.00001" and popular.metrics == {"upvotes": 150}
    assert popular.extra == {"links": [["代码", "https://github.com/a/b"]]} and popular.weight == 0.6
    assert voted.metrics == {"upvotes": 8} and voted.weight == 0.8 and coded.heat == 0.3
    query = next(c["params"]["search_query"] for c in ctx.http.calls if "search_query" in c["params"])
    expected = '(cat:cs.CL OR cat:cs.AI) AND (ti:"text to speech" OR ti:"TTS")'
    assert query == expected + " AND submittedDate:[202610090000 TO 202610112359]"


def test_papers_survive_partial_outages():
    def daily(url, params):
        return [hf_row("2610.00001", "Popular LLM paper", 150)] if params["date"] == "2026-10-11" else []

    arxiv_down = context({papers.HF_DAILY: daily, papers.ARXIV_API: HttpError("HTTP 503", 503)})
    assert [i.title for i in papers.fetch(PAPERS_CONFIG, arxiv_down)] == ["Popular LLM paper"]  # 分类查不到就不筛

    hf_down = context(
        {
            papers.HF_DAILY: HttpError("HTTP 500", 500),
            papers.ARXIV_API: arxiv_feed(("2610.00005", "TTS with code", ["cs.CL"], "github.com/x/y")),
        }
    )
    assert [i.title for i in papers.fetch(PAPERS_CONFIG, hf_down)] == ["TTS with code"]

    with pytest.raises(RuntimeError, match="Daily Papers"):
        papers.fetch(
            PAPERS_CONFIG, context({papers.HF_DAILY: HttpError("HTTP 500", 500), papers.ARXIV_API: HttpError("x", 503)})
        )


def test_hf_daily_papers_follows_pages_until_a_short_one():
    def daily(url, params):
        if params["date"] != "2026-10-11":
            return []
        return [hf_row(f"2610.{params['p']}{n:04d}", "t", 1) for n in range(100 if params["p"] == 0 else 7)]

    ctx = context({papers.HF_DAILY: daily})
    assert len(papers.hf_daily_papers(ctx, days=1)) == 107
    assert [c["params"]["p"] for c in ctx.http.calls] == [0, 1]
