"""原文摘录的测试：网页解析、跳过的网站、每条只试一次、总时间上限。不访问网络。"""

from __future__ import annotations

from types import SimpleNamespace

from fakes import FakeHttp

from wta import excerpt
from wta.http import HttpError

ARTICLE = """<!doctype html><html><head>
<title>Ignored</title>
<meta name="description" content="A team turned a text embedding model into a speech-to-text model.">
<meta property="og:description" content="We turned EmbeddingGemma 2 into a speech-to-text model with an encoder.">
<script>var tracking = "<p>not text</p>";</script>
</head><body>
<nav><p>Home | Blog | About us and other navigation links that are long enough</p></nav>
<header><p>Posted by someone on a Tuesday, with a long enough byline to count</p></header>
<article>
<p>We turned EmbeddingGemma 2 into a speech-to-text model with an encoder.</p>
<p>Short.</p>
<p>The encoder is trained on 5,000 hours of public speech &amp; aligned to the text embedding space.
<p>It runs on a laptop CPU in real time and the code is released under Apache 2.0 for anyone to use.</p>
</article>
<footer><p>Copyright notice and other footer text that should never be used as evidence</p></footer>
</body></html>"""


def test_page_text_keeps_the_description_and_the_first_paragraphs():
    text = excerpt.page_text(ARTICLE)
    assert text.startswith("We turned EmbeddingGemma 2 into a speech-to-text model with an encoder.")  # 最长的描述
    assert text.count("We turned EmbeddingGemma 2") == 1  # 描述和第一段一样：只留一份
    assert "5,000 hours of public speech & aligned" in text  # 没写 </p> 的段落也认
    assert "Apache 2.0" in text
    for unwanted in ("navigation", "byline", "footer", "tracking", "Short.", "Ignored"):
        assert unwanted not in text
    assert len(excerpt.page_text("<p>" + "word " * 2000 + "</p>")) <= excerpt.LIMIT + 1


def test_sites_behind_a_login_are_skipped():
    assert excerpt.fetchable("https://blog.example.com/post")
    for url in (
        "https://twitter.com/karpathy/status/1",
        "https://mobile.twitter.com/a",
        "https://x.com/a/status/1",
        "https://www.linkedin.com/pulse/x",
        "https://news.ycombinator.com/item?id=1",
        "ftp://example.com/file",
        "not a url",
    ):
        assert not excerpt.fetchable(url), url
    assert excerpt.fetchable("https://notx.com/a")  # 只是名字里带 x.com 的网站不跳过


def test_non_html_responses_give_no_excerpt():
    pdf = SimpleNamespace(headers={"content-type": "application/pdf"}, text="%PDF-1.7")
    http = SimpleNamespace(get=lambda url, **kwargs: pdf)
    assert excerpt.fetch(http, "https://example.com/paper.pdf") == ""


def test_enrich_fetches_each_missing_description_once(make_item):
    wanted = make_item(title="Show HN: a model", url="https://blog.example.com/post")
    broken = make_item(title="Broken link", url="https://down.example.com/x")
    skipped = [
        make_item(title="Tweet", url="https://twitter.com/a/status/1"),
        make_item(
            title="Has text",
            url="https://a.example.com/1",
            summary="A description that is long enough for the model to write a summary from.",
        ),
        make_item(title="Already written", url="https://a.example.com/2", summary_zh="已经有中文摘要了"),
        make_item(title="A repo", url="https://github.com/a/b", section="opensource"),
        make_item(title="Tried before", url="https://a.example.com/3", extra={"excerpt_tried": True}),
    ]
    wanted.extra["llm_done"] = True  # 之前写过中文标题，但没有摘要
    http = FakeHttp({"https://blog.example.com/": ARTICLE, "https://down.example.com/": HttpError("HTTP 404", 404)})

    assert excerpt.enrich([wanted, broken, *skipped], http) == 2
    assert [call["url"] for call in http.calls] == [wanted.url, broken.url]
    assert wanted.extra["evidence"].startswith("We turned EmbeddingGemma 2")
    assert "llm_done" not in wanted.extra  # 下次写摘要时补上
    assert broken.extra["excerpt_tried"] and "evidence" not in broken.extra
    assert http.deadline is None  # 用完把时间上限还原

    assert excerpt.enrich([wanted, broken], http) == 0 and len(http.calls) == 2  # 每条只试一次


def test_enrich_respects_its_time_budget(make_item):
    item = make_item(title="Late", url="https://blog.example.com/late")
    http = FakeHttp({"https://blog.example.com/": ARTICLE})
    assert excerpt.enrich([item], http, seconds=0) == 0
    assert http.calls == [] and "excerpt_tried" not in item.extra  # 没试过的留给下一次
