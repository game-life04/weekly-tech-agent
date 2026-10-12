from __future__ import annotations

from datetime import UTC, datetime

import pytest

from wta.feeds import FeedError, parse_date, parse_feed

NOW = datetime(2026, 10, 11, 12, 0, tzinfo=UTC)

RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:dc="http://purl.org/dc/elements/1.1/">
<channel>
  <title>Example Blog</title>
  <link>https://example.com/</link>
  <item>
    <title>Older &amp; wiser</title>
    <link>https://example.com/older</link>
    <pubDate>Fri, 09 Oct 2026 08:00:00 GMT</pubDate>
    <description>&lt;p&gt;Hello &lt;b&gt;world&lt;/b&gt;&amp;nbsp;again&lt;/p&gt;</description>
    <category>AI</category><category>AI</category><category>Tools</category>
  </item>
  <item>
    <title>Newest</title>
    <link>/relative/newest</link>
    <dc:date>2026-10-11T03:20:00Z</dc:date>
    <content:encoded><![CDATA[<div>Full <i>text</i> only</div>]]></content:encoded>
  </item>
  <item>
    <title>No date at all</title>
    <guid isPermaLink="true">https://example.com/undated</guid>
  </item>
  <item><title>No link, skipped</title></item>
</channel>
</rss>"""

ATOM = """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Example Atom</title>
  <link rel="self" href="https://atom.example/feed.xml"/>
  <link rel="alternate" type="text/html" href="https://atom.example/"/>
  <entry>
    <title type="html">An &lt;em&gt;Atom&lt;/em&gt; post</title>
    <link rel="replies" href="https://atom.example/comments"/>
    <link rel="alternate" type="text/html" href="https://atom.example/post"/>
    <published>2026-10-10T10:00:00+08:00</published>
    <updated>2026-10-11T10:00:00+08:00</updated>
    <summary>Short summary</summary>
    <category term="llm"/>
  </entry>
</feed>"""


def test_rss_entries_are_cleaned_and_sorted_newest_first():
    entries = parse_feed(RSS.encode(), "https://example.com/feed", now=NOW)
    assert [e["title"] for e in entries] == ["Newest", "Older & wiser", "No date at all"]
    newest, older, undated = entries
    assert newest["url"] == "https://example.com/relative/newest"  # 相对链接按频道地址补全
    assert newest["published"] == datetime(2026, 10, 11, 3, 20, tzinfo=UTC)
    assert newest["summary"] == "Full text only"  # 没有 description 时用正文
    assert older["summary"] == "Hello world again"
    assert older["tags"] == ["AI", "Tools"]
    assert undated["published"] is None and undated["url"] == "https://example.com/undated"


def test_atom_entry_uses_alternate_link_and_published_date():
    (entry,) = parse_feed(ATOM.encode(), "https://atom.example/feed.xml", now=NOW)
    assert entry == {
        "title": "An Atom post",
        "url": "https://atom.example/post",
        "published": datetime(2026, 10, 10, 2, 0, tzinfo=UTC),
        "summary": "Short summary",
        "tags": ["llm"],
    }


def test_sloppy_xml_is_repaired():
    broken = RSS.replace("Older &amp; wiser", "Older & wiser &nbsp; \x07").encode()
    assert parse_feed(broken, now=NOW)[1]["title"] == "Older & wiser"


@pytest.mark.parametrize(
    ("body", "message"),
    [
        (b"", "为空"),
        (b"<!DOCTYPE html><html><body>Just a moment...</body></html>", "网页"),
        (b'<?xml version="1.0"?><!DOCTYPE r [<!ENTITY a "aaaa">]><rss><channel/></rss>', "DOCTYPE"),
        (b"<opml><body/></opml>", "既不是 RSS 也不是 Atom"),
        (b"<rss><channel><item>", "XML 格式错误"),
    ],
)
def test_unusable_documents_raise_feed_error(body, message):
    with pytest.raises(FeedError, match=message):
        parse_feed(body, now=NOW)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Sun, 11 Oct 2026 03:20:00 GMT", "2026-10-11T03:20:00"),
        ("2026-10-11T11:20:00+08:00", "2026-10-11T03:20:00"),
        ("2026-10-11 11:20:00  +0800", "2026-10-11T03:20:00"),  # 36氪的写法
        ("2026/10/11 03:20", "2026-10-11T03:20:00"),
        ("2026-10-11T03:20:00.123456789Z", "2026-10-11T03:20:00.123456"),
        ("October 11, 2026", "2026-10-11T00:00:00"),
    ],
)
def test_parse_date_formats(text, expected):
    assert parse_date(text, NOW).replace(tzinfo=None).isoformat() == expected


def test_parse_date_offsets_and_garbage():
    assert parse_date("2026-10-11 11:20:00", NOW, naive_offset=8).hour == 3  # 没写时区：按北京时间
    assert parse_date("Sun, 11 Oct 2026 11:20:00 GMT", NOW, force_offset=8).hour == 3  # 标成 GMT 的北京时间
    assert parse_date("Mon, 01 Jan 0001 00:00:00 +0000", NOW) is None  # 零值日期
    assert parse_date("2030-01-01T00:00:00Z", NOW) is None  # 太远的未来
    assert parse_date("1990-01-01", NOW) is None
    assert parse_date("not a date", NOW) is None and parse_date("", NOW) is None and parse_date(None, NOW) is None
