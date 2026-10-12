from __future__ import annotations

import pytest

from wta.dedupe import canonical_url, dedupe, item_id, similar_titles
from wta.models import Item


@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("http://www.example.com/post/", "https://example.com/post"),
        ("https://example.com/post?utm_source=x&id=3#top", "https://example.com/post?id=3"),
        ("https://example.com/p?b=2&a=1", "https://example.com/p?a=1&b=2"),
        ("https://arxiv.org/abs/2510.01234v2", "https://arxiv.org/pdf/2510.01234"),
        ("https://huggingface.co/papers/2510.01234", "http://arxiv.org/abs/2510.01234"),
        ("https://github.com/Vllm-Project/vLLM.git", "https://github.com/vllm-project/vllm/"),
    ],
)
def test_same_page_same_canonical_url(a, b):
    assert canonical_url(a) == canonical_url(b)
    assert item_id(a) == item_id(b)


@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("https://example.com/Post", "https://example.com/post"),  # 路径区分大小写
        ("https://example.com/p?id=1", "https://example.com/p?id=2"),
        ("https://github.com/a/b", "https://github.com/a/b/releases/tag/v1"),
        ("https://arxiv.org/abs/2510.01234", "https://arxiv.org/abs/2510.01235"),
    ],
)
def test_different_pages_stay_different(a, b):
    assert canonical_url(a) != canonical_url(b)


def test_similar_titles():
    assert similar_titles("OpenAI releases GPT-6 today", "OpenAI Releases GPT-6 Today!", 0.92)
    assert not similar_titles("OpenAI releases GPT-6", "Anthropic releases Claude 6", 0.92)
    assert not similar_titles("v1.2.3", "v1.2.4", 0.92)  # 短标题只认完全相同
    assert not similar_titles("Meta releases Llama 3.1 today", "Meta releases Llama 3.2 today", 0.92)  # 数字不同
    assert not similar_titles("", "", 0.92)


def test_same_url_keeps_higher_weight_and_merges(make_item):
    blog = make_item(title="Introducing X", url="https://lab.com/x", via="Lab Blog", weight=0.9, heat=0.2)
    hn = make_item(
        title="Introducing X",
        url="https://lab.com/x?utm_source=hn",
        via="Hacker News",
        weight=0.6,
        heat=0.8,
        metrics={"points": 500},
        extra={"discussion": "https://news.ycombinator.com/item?id=1"},
    )
    result = dedupe([hn, blog])
    assert len(result) == 1
    kept = result[0]
    assert kept.via == "Lab Blog"
    assert kept.heat == 0.8
    assert kept.metrics["points"] == 500
    assert kept.also_in == ["Hacker News"]
    assert kept.extra["discussion"].startswith("https://news.ycombinator.com")


def test_news_with_near_identical_titles_merge(make_item):
    a = make_item(title="Mistral releases a new open model", url="https://a.com/1", via="A", weight=0.7)
    b = make_item(title="Mistral releases a new open model!", url="https://b.com/2", via="B", weight=0.5)
    result = dedupe([b, a])
    assert [i.via for i in result] == ["A"]
    assert result[0].also_in == ["B"]


def test_same_feed_never_merges_by_title(make_item):
    a = make_item(title="Quoting a well known researcher", url="https://blog.example/1", via="Blog")
    b = make_item(title="Quoting a well known researcher", url="https://blog.example/2", via="Blog")
    assert len(dedupe([a, b])) == 2  # 同一个订阅里标题相同的两篇，是两篇不同的文章


def test_repos_and_papers_only_merge_by_url(make_item):
    a = make_item(title="awesome-llm-apps", url="https://github.com/a/awesome-llm-apps", section="opensource")
    b = make_item(title="awesome-llm-apps", url="https://github.com/b/awesome-llm-apps", section="opensource")
    assert len(dedupe([a, b])) == 2


def test_merge_keeps_chinese_text_from_earlier_run(make_item):
    old = make_item(
        url="https://example.com/a",
        weight=0.5,
        title_zh="旧标题",
        summary_zh="旧摘要",
        tags=["模型"],
        extra={"llm_score": 8},
    )
    fresh = make_item(url="https://example.com/a", weight=0.9)
    kept = dedupe([fresh, old])[0]
    assert (kept.title_zh, kept.summary_zh, kept.tags) == ("旧标题", "旧摘要", ["模型"])
    assert kept.extra["llm_score"] == 8


def test_doubt_about_relevance_does_not_spread_to_a_trusted_copy(make_item):
    feed = make_item(title="Notes on a new release", url="https://blog.example/notes", via="Blog", weight=0.7)
    post = make_item(
        title="Notes on a new release",
        url="https://blog.example/notes",
        via="Hacker News",
        weight=0.6,
        source="hackernews",
        extra={"needs_review": True, "discussion": "https://news.ycombinator.com/item?id=1"},
    )
    for pair in ([feed, post], [post, feed]):
        kept = dedupe([Item.from_dict(i.to_dict()) for i in pair])[0]
        assert "needs_review" not in kept.extra and kept.extra["discussion"]  # 订阅那一份已经说明了相关性
    both = dedupe([Item.from_dict(post.to_dict()), Item.from_dict({**post.to_dict(), "via": "Hacker News 2"})])[0]
    assert both.extra["needs_review"] is True  # 两份都存疑才继续存疑


def test_a_hacker_news_post_never_replaces_the_publishers_link(make_item):
    title = "OpenAI launches GPT-6 with a 2M-token context window"
    media = make_item(title=title, url="https://techcrunch.com/gpt-6", via="TechCrunch", weight=0.45, summary="Real.")
    post = make_item(
        title=title,
        url="https://techcrunch-news.example/gpt-6",
        via="Hacker News",
        weight=0.6,
        source="hackernews",
        metrics={"points": 22},
    )
    (kept,) = dedupe([post, media])
    assert kept.url == "https://techcrunch.com/gpt-6" and kept.via == "TechCrunch"
    assert kept.also_in == ["Hacker News"] and kept.metrics == {"points": 22}


def test_merged_copies_are_remembered(make_item):
    a = make_item(title="Mistral releases a new open model", url="https://a.com/1", via="A", weight=0.7)
    b = make_item(title="Mistral releases a new open model!", url="https://b.com/2", via="B", weight=0.5)
    (kept,) = dedupe([a, b])
    assert kept.merged_ids == [item_id("https://b.com/2")]  # 之后几天 B 那一份单独出现，也算已经登过


def test_the_same_model_on_two_hubs_is_one_item():
    assert canonical_url("https://www.modelscope.cn/models/Qwen/Qwen3-8B") == canonical_url(
        "https://huggingface.co/qwen/qwen3-8b"
    )
    assert canonical_url("https://modelscope.cn/studios/a/b") != canonical_url("https://huggingface.co/a/b")
