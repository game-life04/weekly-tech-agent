from __future__ import annotations

import pytest
from fakes import FakeClient

from wta import editor
from wta.llm import Filtered, LLMError

LONG_TEXT = (
    "OpenAI released X, a new open-weight model with a 1M-token context window, available today under Apache 2.0."
)


def test_parse_json_tolerates_wrapping():
    assert editor.parse_json('```json\n{"items": []}\n```') == {"items": []}
    assert editor.parse_json('好的，结果如下：{"a": 1} 希望有帮助') == {"a": 1}
    with pytest.raises(ValueError, match="共 7 字，开头：没有 JSON"):  # 日志里能看出模型回了什么
        editor.parse_json("没有 JSON")
    with pytest.raises(ValueError, match="没有完整的 JSON 对象"):
        editor.parse_json('{"a": ')
    with pytest.raises(ValueError, match="不是合法的 JSON"):
        editor.parse_json('{"a": 1,, }')
    cut_off = '{"items": [{"i": 0, "score": 7}, {"i": 1, "score": 3}, {"i": 2, "sc'
    assert editor.parse_json(cut_off) == {"items": [{"i": 0, "score": 7}, {"i": 1, "score": 3}]}  # 被截断：救回完整的行


def test_plain_strips_links_markup_and_non_strings():
    assert editor.plain("看这里 [点我](https://evil.example/x) **重要** `rm -rf`", 100) == "看这里 点我 重要 rm -rf"
    assert editor.plain("图 ![alt](https://evil.example/a.png) 和 (https://evil.example/b)", 100) == "图 alt 和 ()"
    assert editor.plain("访问 www.evil.example 领取", 100) == "访问 领取"
    assert editor.plain(None, 10) == "" and editor.plain(123, 10) == ""
    assert len(editor.plain("字" * 500, 80)) == 80
    kept = "llama_index 新增 max_tokens，支持 C# 与 F#，延迟 >2 倍 ~50ms"
    assert editor.plain(kept, 100) == kept  # 下划线、#、> 是名称和正文的一部分，不能删


def test_ungrounded_flags_names_and_figures_missing_from_the_source():
    source = "Qwen3-8B reaches 71.5% on the benchmark, says Alibaba"
    assert editor.ungrounded("阿里发布 Qwen3-8B，准确率 71.5%", source) == []
    assert editor.ungrounded("阿里发布 Qwen3-8B，超过 GPT-5，准确率 93.2%", source) == ["93.2%", "GPT-5"]
    assert editor.ungrounded("一个新的 AI Agent 框架，支持 Python 和 API 调用", "a new framework") == []  # 通用词不算
    assert editor.ungrounded("发布了 3 个模型，共 12 项改进", "nothing") == []  # 一两位的小数字不查
    assert (
        editor.ungrounded("GPT-6 支持 3500 行", "with GPT" + chr(0x2011) + "6, a 3,500-Line demo") == []
    )  # 连字符、千分位
    assert editor.ungrounded("open-webui v0.12.0 发布", "open-webui/open-webui v0.12.0 Minor release") == []  # 版本号
    assert editor.ungrounded("升级到 0.13.1", "v0.12.0") == ["0.13.1"]
    assert editor.ungrounded("基于 GPT-5，共 100 项", "GPT-5.6 has 1000 items") == [
        "100",
        "GPT-5",
    ]  # 不能是更长数字的前缀


def test_score_applies_valid_rows_and_ignores_bad_ones(make_item):
    items = [make_item(title=f"t{i}", url=f"https://a.com/{i}", summary="about a model") for i in range(4)]
    client = FakeClient(
        [{"items": [{"i": 0, "score": 9}, {"i": 1, "score": 99}, {"i": 2, "score": "8"}, {"i": 7, "score": 5}, "x"]}]
    )
    assert editor.score(items, client) == 1
    assert items[0].extra["llm_score"] == 9.0
    assert all("llm_score" not in item.extra for item in items[1:])
    sent = client.calls[0]["items"][0]
    assert sent == {"i": 0, "section": "news", "source": "Fake", "title": "t0", "text": "about a model"}


def test_score_batches_and_skips_items_already_scored(make_item):
    items = [make_item(title=f"t{i}", url=f"https://a.com/{i}") for i in range(editor.SCORE_BATCH + 3)]
    items[0].extra["llm_score"] = 8.0
    client = FakeClient([lambda sent: {"items": [{"i": row["i"], "score": 5} for row in sent["items"]]}])
    assert editor.score(items, client) == editor.SCORE_BATCH + 2
    assert [len(call["items"]) for call in client.calls] == [editor.SCORE_BATCH, 2]


def blocked_reply(sent):
    if any(row["title"] == "BLOCKED" for row in sent["items"]):
        return Filtered("sensitive")
    return {"items": [{"i": r["i"], "score": 6, "title_zh": "标题", "summary_zh": ""} for r in sent["items"]]}


def test_scoring_splits_a_blocked_batch_only_once(make_item):
    items = [make_item(title=f"t{i}", url=f"https://a.com/{i}") for i in range(8)]
    items[6].title = "BLOCKED"
    client = FakeClient([blocked_reply])
    assert editor.score(items, client) == 4  # 没被拦的那一半照常打分
    assert len(client.calls) == 3  # 整批一次，对半各一次；不再往下细分，省下请求留给写摘要
    assert not any(item.extra.get("filtered") for item in items)
    assert ["llm_score" in item.extra for item in items] == [True] * 4 + [False] * 4


def test_summarising_finds_the_one_item_blocked_by_content_filter(make_item):
    items = [make_item(title=f"t{i}", url=f"https://a.com/{i}") for i in range(6)]
    items[4].title = "BLOCKED"
    assert editor.summarize(items, FakeClient([blocked_reply])) == 5
    assert [bool(item.extra.get("filtered")) for item in items] == [False, False, False, False, True, False]
    assert all(item.title_zh == "标题" for item in items if item.title != "BLOCKED")


def test_scoring_leaves_requests_for_the_summaries(make_item):
    items = [make_item(title=f"t{i}", url=f"https://a.com/{i}") for i in range(editor.SCORE_BATCH * 12)]
    client = FakeClient([lambda sent: {"items": [{"i": r["i"], "score": 5} for r in sent["items"]]}], max_requests=10)
    editor.score(items, client)
    assert len(client.calls) == 10 - min(editor.SCORE_RESERVE, 5)


def test_open_submission_sources_never_share_a_batch_with_publishers(make_item):
    items = [make_item(title="feed", url="https://a.com/1", source="rss")]
    items += [make_item(title="post", url="https://a.com/2", source="hackernews")]
    client = FakeClient([lambda sent: {"items": [{"i": r["i"], "score": 5} for r in sent["items"]]}])
    assert editor.score(items, client) == 2
    assert [[row["title"] for row in call["items"]] for call in client.calls] == [["feed"], ["post"]]


def test_score_stops_after_repeated_failures_and_when_budget_runs_out(make_item):
    items = [make_item(title=f"t{i}", url=f"https://a.com/{i}") for i in range(editor.SCORE_BATCH * 4)]
    client = FakeClient([LLMError("HTTP 500"), "这不是 JSON", LLMError("HTTP 500"), {"items": []}])
    assert editor.score(items, client) == 0
    assert len(client.calls) == 3  # 接连失败两批就停；最后补做时再失败一批，彻底收工

    tight = FakeClient([lambda sent: {"items": []}], max_requests=1)
    editor.score(items, tight)
    assert len(tight.calls) == 1  # 请求次数用完也停


def test_batches_that_failed_are_retried_in_halves_at_the_end(make_item):
    items = [make_item(title=f"t{i}", url=f"https://a.com/{i}") for i in range(editor.SUMMARY_BATCH * 2 + 3)]
    good = lambda sent: {"items": [{"i": r["i"], "title_zh": "标题", "summary_zh": ""} for r in sent["items"]]}  # noqa: E731
    client = FakeClient([LLMError("HTTP 429：当前API请求过多"), good])
    assert editor.summarize(items, client) == len(items)  # 第一批一时失败，最后补上了
    half = editor.SUMMARY_BATCH // 2
    assert [len(call["items"]) for call in client.calls] == [editor.SUMMARY_BATCH, editor.SUMMARY_BATCH, 3, half, half]

    # 接连失败两批之后，没轮到的批次也留到最后补做（整批，不用拆）
    items = [make_item(title=f"n{i}", url=f"https://b.com/{i}") for i in range(editor.SUMMARY_BATCH * 3)]
    client = FakeClient([LLMError("HTTP 500"), "不是 JSON", good])
    assert editor.summarize(items, client) == len(items)
    assert [len(call["items"]) for call in client.calls] == [10, 10, half, half, half, half, 10]


def test_summarize_writes_chinese_and_guards_against_invention(make_item):
    news = make_item(title="OpenAI releases X", url="https://a.com/1", summary=LONG_TEXT)
    repo = make_item(title="owner/repo", url="https://github.com/owner/repo", section="opensource", summary=LONG_TEXT)
    thin = make_item(title="Anthropic ships something", url="https://a.com/3", summary="short")
    liar = make_item(title="A paper about agents", url="https://a.com/4", summary=LONG_TEXT)
    client = FakeClient(
        [
            {
                "items": [
                    {
                        "i": 0,
                        "title_zh": "OpenAI 发布 X",
                        "summary_zh": "开放权重的新模型，上下文窗口 1M。详见 https://evil.example",
                        "tags": ["模型发布", "x" * 50, 7, "多余", "更多"],
                    },
                    {"i": 1, "title_zh": "不该出现的标题", "summary_zh": "一个开放权重模型的仓库", "tags": "不是列表"},
                    {"i": 2, "title_zh": "Anthropic 发布新功能", "summary_zh": "资料不够也硬写的摘要"},
                    {
                        "i": 3,
                        "title_zh": "关于智能体的论文",
                        "summary_zh": "该方法在 SWE-bench 上达到 87.4%，超过 Claude 9",
                    },
                ]
            }
        ]
    )
    assert editor.summarize([news, repo, thin, liar], client) == 4

    assert (news.title_zh, news.summary_zh) == ("OpenAI 发布 X", "开放权重的新模型，上下文窗口 1M。详见")
    assert news.tags == ["模型发布", "x" * 11 + "…"]
    assert (repo.title_zh, repo.summary_zh) == ("", "一个开放权重模型的仓库")  # 仓库名不翻译
    assert (thin.title_zh, thin.summary_zh) == ("Anthropic 发布新功能", "")  # 资料太少：只译标题，不写摘要
    assert (liar.title_zh, liar.summary_zh) == ("关于智能体的论文", "")  # 摘要里编了资料中没有的名称和数字
    sent = client.calls[0]["items"]
    assert "text" in sent[0] and "text" not in sent[2]
    assert all(item.extra["llm_done"] for item in (news, repo, thin, liar))

    again = FakeClient([])
    assert editor.summarize([news, repo, thin, liar], again) == 0 and again.calls == []  # 处理过的不再重复请求


def test_summarize_uses_extra_evidence_when_present(make_item):
    release = make_item(
        title="org/tool v2.0.0",
        url="https://github.com/org/tool/releases/tag/v2.0.0",
        section="opensource",
        summary="主版本更新",
        extra={"evidence": "v2.0.0 adds a streaming API and drops Python 3.9 support. " * 3},
    )
    client = FakeClient([{"items": [{"i": 0, "title_zh": "", "summary_zh": "新增流式 API，不再支持 Python 3.9"}]}])
    assert editor.summarize([release], client) == 1
    assert release.summary_zh == "新增流式 API，不再支持 Python 3.9"
    assert client.calls[0]["items"][0]["text"].startswith("v2.0.0 adds a streaming API")


HIGGSFIELD = {  # 真实出过的错：原题只说 Higgsfield 把视频做长了，简介里说它用了 OpenAI 的 GPT-6 Astra
    "title": "Higgsfield takes AI video from 1 minute to over 10",
    "via": "OpenAI",
    "summary": "Higgsfield brings creators longer videos with GPT-6 Astra, precise visuals with GPT-Image-2.5.",
}


def test_a_title_may_not_borrow_names_from_the_summary(make_item):
    story = make_item(**HIGGSFIELD)
    reply = {
        "i": 0,
        "title_zh": "Higgsfield 推出 GPT-6 等模型，支持超长视频生成",  # 把使用者写成了发布者
        "summary_zh": "Higgsfield 利用 GPT-6 Astra 和 GPT-Image-2.5，把 AI 视频从 1 分钟延长到 10 分钟以上。",
    }
    assert editor.summarize([story], FakeClient([{"items": [reply]}])) == 1
    assert story.title_zh == ""  # 页面上改为显示原标题
    assert story.summary_zh.startswith("Higgsfield 利用 GPT-6 Astra")  # 摘要可以依据简介来写


def test_recheck_applies_newer_rules_to_text_written_earlier(make_item):
    old = make_item(
        **HIGGSFIELD,
        title_zh="Higgsfield 推出 GPT-6",
        summary_zh="Higgsfield 利用 GPT-6 Astra 做长视频",
        extra={"llm_done": True},
    )
    fine = make_item(
        title="OpenAI releases X", url="https://a.com/2", title_zh="OpenAI 发布 X", extra={"llm_done": True}
    )
    assert editor.recheck([old, fine]) == 1
    assert (old.title_zh, old.summary_zh) == ("", "Higgsfield 利用 GPT-6 Astra 做长视频")  # 只撤不合格的标题
    assert old.extra["llm_done"]  # 不重写：重写可能把原本正确的摘要也写错
    assert fine.title_zh == "OpenAI 发布 X" and fine.extra["llm_done"]
    assert editor.recheck([old, fine]) == 0


def test_weekly_overview(make_item):
    items = [make_item(title="Qwen3 released", title_zh="Qwen3 发布", summary_zh="阿里发布新模型", score=8.0)]
    assert (
        editor.weekly_overview(items, FakeClient([{"overview": "本周 **重点** 是 Qwen3 发布。"}]))
        == "本周 重点 是 Qwen3 发布。"
    )
    assert editor.weekly_overview(items, FakeClient([{"overview": "本周 GPT-9 横空出世。"}])) == ""  # 编出了没有的名称
    assert editor.weekly_overview(items, FakeClient([LLMError("boom")])) == ""
    assert editor.weekly_overview(items, FakeClient([{"overview": ["不是字符串"]}])) == ""
    assert editor.weekly_overview([], FakeClient([])) == ""

    # 模型没按要求输出 JSON，直接回了一段话（智谱实际出现过）：去掉它自己加的小标题后照用
    paragraph = "本周最值得关注的是 Qwen3 发布，阿里发布新模型，开源社区反应热烈，相关工具和评测也在陆续跟进。"
    assert editor.weekly_overview(items, FakeClient(["本周看点：" + paragraph])) == paragraph
    assert editor.weekly_overview(items, FakeClient(["抱歉，我无法完成。"])) == ""  # 太短，不像一段看点
    assert editor.weekly_overview(items, FakeClient(['{"overview": "半截'])) == ""  # 坏掉的 JSON 不猜
