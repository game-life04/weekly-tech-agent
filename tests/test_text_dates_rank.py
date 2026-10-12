from __future__ import annotations

from datetime import UTC, date, datetime, timedelta

import pytest

from wta.dates import local_date, parse_time, to_iso, week_id, week_range, weekday_name
from wta.rank import apply_scores, freshness, select
from wta.textutil import KeywordMatcher, clean_text, log_scale

NOW = datetime(2026, 10, 11, 0, 0, tzinfo=UTC)


def test_clean_text_strips_markup_and_control_chars():
    assert clean_text("<p>Hello&nbsp;<b>world</b>\n\n &amp; more</p>") == "Hello world & more"
    hidden = "".join(
        chr(code) for code in (0x200B, 0x00, 0x202E, 0xE0041, 0xD83D)
    )  # 零宽、控制符、方向符、标签字符、孤立代理
    assert clean_text("a" + hidden + "bc") == "abc"
    assert clean_text(None) == ""
    assert clean_text("x" * 50, limit=10) == "x" * 9 + "…"


KEYWORDS = {
    "exact": ["AI", "LLMs?", "RAG", "LoRA", r"GPT-?\d[\w.\-]*"],
    "any_case": ["fine-?tun(?:e|ed|es|ing)", "claude", "agents?", "大模型"],
    "exclude": ["claude shannon", "(?:fbi|travel) agents?"],
    "domains": ["openai.com"],
}


def test_keyword_matcher_whole_words_case_and_excludes():
    matcher = KeywordMatcher(KEYWORDS)
    assert matcher.match("New AI model released")
    assert matcher.match("Why LLMs hallucinate")
    assert matcher.match("国产大模型发布") and matcher.match("用AI写代码")
    assert matcher.match("A guide to Fine-Tuning")
    assert matcher.hits("GPT‑6 leaked") == ["gpt-6"]  # 标题里的不换行连字符也认
    assert not matcher.match("He said he would maintain the garage")  # said / maintain / garage 里都有 ai、rag
    assert not matcher.match("Show HN: a LoRa mesh radio") and matcher.match("A new LoRA trick")  # 缩写区分大小写
    assert not matcher.match("Claude Shannon and information theory")
    assert matcher.hits("Claude Shannon would love Claude") == ["claude"]  # 只屏蔽被排除的那几个字
    assert not matcher.match("FBI agents raid office") and matcher.match("Coding agents are here")
    assert matcher.hits("AI and AI and LLMs") == ["ai", "llms"]
    assert not matcher.match("")


def test_keyword_matcher_falls_back_to_known_domains():
    matcher = KeywordMatcher(KEYWORDS)
    assert matcher.hits("Decisions API is in public beta", "https://platform.openai.com/docs") == [
        "platform.openai.com"
    ]
    assert not matcher.match("Decisions API is in public beta", "https://notopenai.com/docs")
    assert not matcher.match("Decisions API is in public beta")


def test_keyword_matcher_without_keywords_matches_nothing():
    assert not KeywordMatcher({}).match("AI")
    assert not KeywordMatcher(None).match("AI", "https://openai.com")


def test_keyword_matcher_reports_which_pattern_is_broken():
    with pytest.raises(ValueError, match=r"keywords\.any_case.*\(unclosed"):
        KeywordMatcher({"any_case": ["fine", "(unclosed"]})


def test_log_scale():
    assert log_scale(0, 1000) == 0
    assert log_scale(1000, 1000) == 1
    assert log_scale(10**9, 1000) == 1
    assert 0 < log_scale(30, 1000) < log_scale(300, 1000) < 1


def test_local_date_uses_configured_offset():
    late_utc = datetime(2026, 10, 10, 23, 30, tzinfo=UTC)
    assert local_date(late_utc, 8) == date(2026, 10, 11)
    assert local_date(late_utc, 0) == date(2026, 10, 10)


@pytest.mark.parametrize(
    ("day", "week"),
    [
        (date(2026, 10, 11), "2026-W41"),
        (date(2026, 12, 31), "2026-W53"),
        (date(2027, 1, 3), "2026-W53"),  # 跨年的那一周归到上一年
        (date(2027, 1, 4), "2027-W01"),
    ],
)
def test_week_id(day, week):
    assert week_id(day) == week


def test_week_range_and_weekday_name():
    monday, sunday = week_range(date(2026, 10, 11))
    assert (monday, sunday) == (date(2026, 10, 5), date(2026, 10, 11))
    assert weekday_name(monday) == "周一"
    assert weekday_name(sunday) == "周日"


@pytest.mark.parametrize(
    "value",
    [
        "2026-10-11T03:20:00Z",
        "2026-10-11T11:20:00+08:00",
        "Sun, 11 Oct 2026 03:20:00 GMT",
        datetime(2026, 10, 11, 3, 20, tzinfo=UTC).timestamp(),
    ],
)
def test_parse_time_accepts_common_formats(value):
    assert to_iso(parse_time(value)) == "2026-10-11T03:20:00Z"


def test_parse_time_rejects_garbage():
    assert parse_time("not a date") is None
    assert parse_time("") is None
    assert to_iso(None) == "" and to_iso("garbage") == ""
    assert parse_time("2026-10-11T03:20:00").tzinfo is not None  # 没带时区的按 UTC


def test_freshness_decays():
    assert freshness(to_iso(NOW), NOW) == pytest.approx(1.0)
    assert freshness(to_iso(NOW - timedelta(hours=48)), NOW) == pytest.approx(0.5)
    assert freshness("", NOW) == 0.5
    assert freshness(to_iso(NOW + timedelta(hours=5)), NOW) == pytest.approx(1.0)  # 来源时钟超前不加分


def test_apply_scores_blends_llm_score(make_item):
    plain = make_item(heat=1.0, weight=1.0, published=to_iso(NOW))
    judged = make_item(heat=1.0, weight=1.0, published=to_iso(NOW), extra={"llm_score": 4})
    wrong_type = make_item(heat=1.0, weight=1.0, published=to_iso(NOW), extra={"llm_score": "9"})
    apply_scores([plain, judged, wrong_type], NOW)
    assert plain.score == 10
    assert judged.score == 6.4  # 规则分 10 占四成，大模型给的 4 分占六成
    assert wrong_type.score == 10


def test_select_respects_quota_cap_and_order(make_item):
    items = [make_item(title=f"n{i}", url=f"https://x.com/{i}", via="A", score=10 - i) for i in range(5)]
    items += [make_item(title="other", url="https://y.com/1", via="B", score=1.0)]
    items += [make_item(title="repo", url="https://github.com/a/b", section="opensource", score=3.0)]
    chosen = select(items, {"news": 4, "opensource": 2, "papers": 2}, per_source_cap=2)
    assert [i.title for i in chosen] == ["n0", "n1", "other", "repo"]  # A 最多 2 条，名额不够时不硬凑
