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
    assert "[每周快讯](../../weekly/README.md)" in text
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


def kx_issue(**extra):
    entry = {"when": "10月6日", "date": "2026-10-06", "via": "Example", "ai": False}
    return {
        "week": "2026-W41",
        "start": "2026-10-05",
        "end": "2026-10-11",
        "generated_at": "2026-10-11T19:30:00Z",
        "models": ["fake-1"],
        "club_period": {"start": "2026-10-04", "end": "2026-10-10"},
        "sources": [{"name": "policy", "title": "中国政府网", "ok": False, "error": "boom"}],
        "entries": [
            {**entry, "cat": "club", "headline": "俱乐部一周合并 3 个 PR", "when": "10月4日至10日", "body": "统计。",
             "url": "https://osd.example/", "via": "俱乐部开源仪表盘"},
            {**entry, "cat": "overseas", "headline": "Evil *corp* 发布 [x](javascript:alert(1))",
             "body": "<script>alert(1)</script>正文 $5", "url": "javascript:alert(1)", "ai": True},
            {**entry, "cat": "domestic", "headline": "阿里发布 Qwen4", "body": "支持长上下文。",
             "url": "https://example.com/a(b)"},
            {**entry, "cat": "events", "headline": "CVPR 2027 论文截稿", "when": "11月17日", "body": "截稿。",
             "url": "https://cvpr.example/", "via": "会议官网"},
        ],
        **extra,
    }  # fmt: skip


def test_render_kuaixun_markdown(config):
    text = render.render_kuaixun(kx_issue(), config)
    assert text.startswith("# 每周科技快讯 · 10.05–10.11\n")
    assert "本期为您带来：**10.05–10.11 快讯** · **近期活动预告**" in text
    assert "[公众号排版版](2026-W41.html)" in text
    order = ["## 新闻速览", "## 上周快讯", "### 俱乐部动态", "### 国内动态", "### 海外动态", "## 活动预告"]
    assert [text.index(h) for h in order] == sorted(text.index(h) for h in order)  # 栏目按固定顺序
    assert "### 政策动向" not in text and "### 活动预告" not in text  # 空栏目不出现；活动预告不再分栏
    assert (
        "**阿里发布 Qwen4**<br>10月6日，支持长上下文。<br><sub>（来源：[Example](https://example.com/a%28b%29)）</sub>"
        in text
    )
    # 外部文字里的排版符号、脚本和公式都失效，坏链接只留来源名
    evil = (
        "**Evil \\*corp\\* 发布 \\[x\\](javascript:alert(1))**<br>"
        "10月6日，正文 <span>$</span>5<br><sub>（来源：Example）</sub>"
    )
    assert evil in text and "<script>" not in text
    assert "标题和正文由 AI 根据原文整理（fake-1）" in text
    assert "俱乐部动态的统计日期为10月4日至10日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。" in text
    assert "会议截稿时间来自[CCFDDL](https://ccfddl.com/)" in text and "本期未取到：中国政府网。" in text
    assert "/issues)。" in text and "于 2026-10-12 03:30（北京时间）自动生成。" in text

    quiet = render.render_kuaixun(kx_issue(entries=[], sources=[]), config)
    assert "这一期没有收集到内容。" in quiet and "新闻速览" not in quiet and "AI 根据原文" not in quiet


def test_render_kuaixun_html_for_wechat(config):
    page = render.render_kuaixun_html(kx_issue(), config)
    assert page.startswith("<!doctype html>") and "<title>每周科技快讯 · 10.05–10.11</title>" in page
    assert "<script>" not in page and "&lt;script&gt;" in page  # 外部文字一律转义
    assert "<a " not in page  # 公众号里链接点不了：来源写成网址
    assert "（来源：https://example.com/a%28b%29）" in page and "（来源：Example）" in page
    assert page.count("✨") == 4 and 'style="' in page
    assert "数据来自俱乐部开源仪表盘（https://osd.openatom.club/）。" in page


def test_latest_block_shows_the_kuaixun_and_the_daily(make_item, config):
    block = render.render_latest_block(DAY, payload_of(make_item()), config, kx_issue())
    assert block.index("## 每周快讯 · 10.05–10.11") < block.index("## 最新日报 · 2026-10-11（周日）")
    assert "[阅读全文](weekly/2026-W41.md) · [公众号排版版](weekly/2026-W41.html)" in block
    assert "✨ [阿里发布 Qwen4](https://example.com/a%28b%29)" in block
    only_daily = render.render_latest_block(DAY, payload_of(make_item()), config)
    assert "每周快讯 ·" not in only_daily and "[每周快讯](weekly/README.md)" in only_daily
    only_kx = render.render_latest_block(None, {}, config, kx_issue())
    assert "最新日报" not in only_kx and only_kx.endswith(render.LATEST_END)


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
    older = kx_issue(week="2026-W40", start="2026-09-28", end="2026-10-04", entries=[])
    weekly = render.render_weekly_index([older, kx_issue()])
    assert "- [2026 年第 41 周 · 10.05–10.11](2026-W41.md) · [公众号排版版](2026-W41.html) · 4 条" in weekly
    assert weekly.index("第 41 周") < weekly.index("第 40 周")
    assert "还没有快讯：每周一生成上一周的一期" in render.render_weekly_index([])


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
