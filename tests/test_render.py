from __future__ import annotations

from datetime import date

import pytest

from wta import render
from wta.render import fmt_num, md_escape, md_url, render_item, replace_latest_block

DAY = date(2026, 10, 11)


def payload_of(*items, **extra):
    return {
        "date": DAY.isoformat(),
        "generated_at": "2026-10-10T23:21:00Z",
        "llm": None,
        "sources": [
            {"name": "fake", "title": "Fake", "ok": True, "count": 3, "seconds": 0.1, "error": ""},
            {"name": "bad", "title": "Broken", "ok": False, "count": 0, "seconds": 0.1, "error": "boom"},
        ],
        "items": [i.to_dict() for i in items],
        **extra,
    }


@pytest.mark.parametrize(
    ("value", "text"),
    [(532, "532"), (1000, "1k"), (12345, "12.3k"), (1234567, "1.2M"), (99.9, "99")],
)
def test_fmt_num(value, text):
    assert fmt_num(value) == text


def test_md_escape_neutralises_markup():
    assert md_escape("a [link](http://evil) *b* _c_ `d`") == r"a \[link\](http:\//evil) \*b\* \_c\_ \`d\`"
    assert md_escape("x < y && y > z") == "x &lt; y &amp;&amp; y &gt; z"
    assert md_escape("<script>alert(1)</script>ok <b>bold</b>") == "ok bold"
    assert md_escape("line1\n# heading\n- item") == "line1 # heading - item"


@pytest.mark.parametrize("url", ["javascript:alert(1)", "data:text/html,x", "ftp://x.com/a", "", "//x.com/a"])
def test_md_url_rejects_non_http(url):
    assert md_url(url) == ""


def test_md_url_encodes_characters_that_break_links():
    assert md_url("https://en.wikipedia.org/wiki/GPT_(model)") == "https://en.wikipedia.org/wiki/GPT_%28model%29"
    assert md_url(" https://x.com/a b ") == "https://x.com/a%20b"
    assert md_url("https://x.com/中文") == "https://x.com/中文"


def test_render_item_is_one_line_and_escapes_everything(make_item):
    item = make_item(
        title="Evil](https://evil.example) title\n# not a heading",
        url="https://example.com/a(b)",
        summary="- not a list\n<img src=x onerror=alert(1)>",
        via="Hacker News",
        metrics={"points": 1532, "comments": 210, "stars": 0},
        extra={"discussion": "https://news.ycombinator.com/item?id=1"},
        also_in=["OpenAI"],
        tags=["模型发布", "智能体"],
    )
    line = render_item(3, item)
    assert "\n" not in line
    assert line.startswith(
        "**3. [Evil\\](https:\\//evil.example) title # not a heading](https://example.com/a%28b%29)**"
    )
    assert "<img" not in line
    meta = "Hacker News · 1.5k 分 · 210 评论 · 同时见于 OpenAI · #模型发布 #智能体 · [讨论](https://news.ycombinator.com/item?id=1)"
    assert meta in line


def test_render_item_prefers_chinese_and_keeps_original_title(make_item):
    item = make_item(title="Original title", title_zh="中文标题", summary="English summary", summary_zh="中文摘要")
    line = render_item(1, item)
    assert line.startswith("**1. [中文标题](https://example.com/a)**<br>中文摘要<br>")
    assert "原题：Original title" in line
    assert "English summary" not in line


def test_render_daily_structure_and_relative_links(make_item, config):
    items = [
        make_item(title="News one"),
        make_item(title="owner/repo", url="https://github.com/owner/repo", section="opensource"),
    ]
    text = render.render_daily(DAY, payload_of(*items), config, previous=date(2026, 10, 10))
    assert text.startswith("# AI 日报 · 2026-10-11（周日）\n")
    assert "今日收录 **2** 条" in text
    assert "[本周周报](../../weekly/2026-W41.md)" in text
    assert "[上一期](2026-10-10.md)" in text
    assert "[往期目录](../README.md)" in text
    assert "## 🗞️ AI 动态" in text and "## 📄 前沿论文" in text
    assert "这个栏目暂时没有新内容。" in text  # 论文栏目为空
    assert "本期候选来自：Fake 3。" in text and "本次未取到：Broken。" in text
    assert "2026-10-11 07:21（北京时间）" in text
    assert "AI 生成" not in text  # 没用大模型时不出现这句提示


def test_footer_mentions_model_when_llm_used(make_item, config):
    item = make_item(title_zh="中文标题")
    text = render.render_daily(DAY, payload_of(item, llm={"model": "some-model"}), config, None)
    assert "中文标题和摘要由 AI 生成（some-model），可能有误，请以原文为准。" in text
    assert "上一期" not in text


def test_render_weekly_picks_best_across_days(make_item, config):
    config["sections"]["news"]["weekly"] = 2
    monday = date(2026, 10, 5)
    payloads = {
        monday: payload_of(make_item(title="low", url="https://x.com/1", via="A", score=2.0)),
        date(2026, 10, 6): payload_of(
            make_item(title="high", url="https://x.com/2", via="B", score=9.0),
            make_item(title="mid", url="https://x.com/3", via="C", score=5.0),
        ),
    }
    text = render.render_weekly(monday, payloads, config, today=date(2026, 10, 6), overview="本周 *重点*")
    assert text.startswith("# AI 周报 · 2026 年第 41 周（10-05 ~ 10-11）")
    assert "共收录 **3** 条" in text and "精选 **2** 条" in text
    assert "本周还没结束" in text
    assert "[周一 10-05](../daily/2026/2026-10-05.md) · [周二 10-06](../daily/2026/2026-10-06.md)" in text
    assert "## 本周看点\n\n本周 \\*重点\\*" in text
    assert text.index("high") < text.index("mid") and "low" not in text
    done = render.render_weekly(monday, payloads, config, today=date(2026, 10, 11))
    assert "本周内容已收齐。" in done and "本周看点" not in done


def test_replace_latest_block():
    block = f"{render.LATEST_START}\nNEW\n{render.LATEST_END}"
    readme = f"# Title\n\n{render.LATEST_START}\nOLD\n{render.LATEST_END}\n\n## About\n"
    updated = replace_latest_block(readme, block)
    assert updated == f"# Title\n\n{block}\n\n## About\n"
    assert replace_latest_block(updated, block) == updated  # 重复执行不变
    assert replace_latest_block("# Title\n", block) == f"# Title\n\n{block}\n"  # 没有标记就加在文末


def test_indexes(config):
    daily = render.render_daily_index([(date(2026, 9, 30), 5), (date(2026, 10, 11), 21), (date(2026, 10, 10), 20)])
    assert daily.index("2026 年 10 月") < daily.index("2026 年 9 月")
    assert "- [10-11（周日）](2026/2026-10-11.md) · 21 条" in daily
    weekly = render.render_weekly_index([(date(2026, 10, 5), 87), (date(2026, 9, 28), 60)])
    assert "- [2026 年第 41 周（10-05 ~ 10-11）](2026-W41.md) · 收录 87 条" in weekly
    assert weekly.index("第 41 周") < weekly.index("第 40 周")


def test_render_item_shows_extra_links_and_ignores_bad_ones(make_item):
    item = make_item(
        extra={
            "links": [["代码", "https://github.com/a/b"], ["坏链接", "javascript:alert(1)"], "不是一对", ["缺地址"]]
        },
    )
    line = render_item(1, item)
    assert "[代码](https://github.com/a/b)" in line and "坏链接" not in line and "不是一对" not in line


def test_md_escape_stops_math_and_autolinks():
    out = md_escape("costs $5, see https://evil.example or www.evil.example, mail a@b.com")
    assert "<span>$</span>5" in out and "://" not in out and "www." not in out and "a@b" not in out
    assert "https:" in out and "evil.example" in out  # 文字还在，只是不会被渲染成链接


def test_damaged_readme_markers_are_refused():
    block = f"{render.LATEST_START}\nNEW\n{render.LATEST_END}"
    for readme in (
        f"# T\n{render.LATEST_START}\nOLD\n",  # 只剩开始标记
        f"# T\nOLD\n{render.LATEST_END}\n",  # 只剩结束标记
        f"# T\n{render.LATEST_END}\n{render.LATEST_START}\n",  # 顺序颠倒
        f"# T\n{block}\n{block}\n",  # 重复
    ):
        with pytest.raises(ValueError, match="标记损坏"):
            replace_latest_block(readme, block)
