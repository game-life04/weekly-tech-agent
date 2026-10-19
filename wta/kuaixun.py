"""每周快讯：参照《CCF开源快讯》的体例，把上一周的内容整理成一期“5 分钟速读”。

每周一生成上周一到周日的一期，栏目和顺序见 models.KX_SECTIONS：
- 俱乐部动态：俱乐部 GitHub 组织的周统计、最活跃的仓库、新仓库和新版本，由程序根据接口数据写成（club.py）；
- 政策动向：中国政府网上和人工智能、开源、软件有关的条目（policy.py）；
- 国内动态、海外动态、开源项目、学术前沿、产业纵横：从这一周每天的日报里挑。大模型负责分栏，
  按“主体+动作+对象”写标题，写一两句正文，并指出讲同一件事的重复条目；
- 活动预告：接下来几周截稿的 CCF 推荐会议（deadlines.py）。

和日报一样，大模型只写栏目、标题和正文，日期、链接、来源和统计数字都由程序填写；
写出了资料里没有的英文名称或数字、或者没写成中文的，就不用，退回日报里已经核对过的中文标题和摘要。
结果存进 data/weekly/<周>.json，页面只凭这份数据生成，重新排版不需要网络和大模型。
"""

from __future__ import annotations

import hashlib
import logging
import re
import unicodedata
from collections.abc import Mapping
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

from . import club, deadlines, excerpt, policy, store
from .dates import local_date, local_time, parse_time, to_iso, week_id, week_range
from .editor import CJK, DATA_NOTE, BatchRun, batches, evidence_of, plain, ungrounded
from .http import Http
from .llm import LLMClient
from .models import KX_SECTIONS, Item
from .publish import load_week_note, week_payloads
from .sources.base import Context
from .textutil import KeywordMatcher, clean_text

log = logging.getLogger(__name__)

BATCH = 12
HEADLINE_LIMIT, BODY_LIMIT = 36, 130  # 提示词里要的是 28 字和 90 字，留一点余地；超出的不用
EVIDENCE_CHARS = 600
MAX_TRIES = 3  # 大模型没写完的那几条，最多再补几次
WRITABLE = ("domestic", "overseas", "opensource", "papers", "industry")  # 大模型可以把日报的 AI 动态放进这些栏目
# 其余条目只能留在对应的栏目或不登：热门仓库多是早就有的项目，被写成“某公司发布”会误导人（第一期出现过）
_ALLOWED = {policy.NAME: ("policy",), "opensource": ("opensource",), "papers": ("papers",)}
_DATE_PREFIX = re.compile(r"^(?:\d{4}年)?\d{1,2}月\d{1,2}日(?:[至到—–-]\d{1,2}日)?(?:消息)?[，,、。.\s]*")
_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9.+-]*")
_GENERIC = frozenset(["ai", "llm", "api"])  # 比较两条是不是同一件事时不算数的通用词

PROMPT = f"""你是《每周科技快讯》的编辑，参照《CCF开源快讯》的体例，为关注人工智能和开源的中国大学生整理上周要闻。
{DATA_NOTE}

每一条有 title（原标题）、title_zh（中文标题，可能没有）、text（资料）、source（来源）和 section（日报里的栏目）。
对每一条：
1. cat：放进哪个栏目。
   section 是 news 的，只能是下面之一：
     domestic 国内动态：中国的公司、高校和机构的发布与动作，包括它们开源的模型和项目；
     overseas 海外动态：海外的公司、高校和机构的发布与动作，包括它们开源的模型和项目；
     opensource 开源项目：社区开源项目的新闻，不是某家公司或机构的动作；
     papers 学术前沿：研究成果和技术文章；
     industry 产业纵横：行业会议、标准、投融资、市场和产业数据；
     skip：和人工智能、开源关系不大，或者资料太少、说不清是什么。
     OpenAI、Google、Meta、Anthropic、英伟达、微软是海外公司；DeepSeek、阿里、腾讯、百度、字节跳动、华为、智谱是中国公司。
   section 是 opensource 的（GitHub 热门仓库、新仓库、版本发布、热门模型），只能是 opensource 或 skip；
   section 是 papers 的，只能是 papers 或 skip；source 是“中国政府网”的，只能是 policy 或 skip。
2. headline：中文标题，不超过 28 个字，写成“主体+动作+对象”，
   例如“腾讯混元开源记忆框架Hy Memory 2.0”“英伟达发布Nemotron 3.5 Super VL模型”。
   主体必须是资料里写明的公司、机构或团队；谁发布、谁使用要和资料一致：“A 用了 B 的模型”不能写成“A 发布 B”。
   资料没写清是谁做的，就用项目或产品的名字开头。
   section 是 opensource 的条目多数是早就有的项目，不要写成“某公司发布某项目”：
   仓库和模型写成“项目名：做什么的”，例如“rea：用智能体做逆向工程”；版本发布写成“项目名 发布 1.2.0 版本”，保留版本号。
3. body：一到两句中文，不超过 90 个字，用主体开头写成完整的句子，说清楚做了什么、有什么特点，
   例如“阶跃星辰宣布开放Step 5 Preview模型权重，包含BF16与FP8两个版本。”。不要写日期，程序会在前面加上日期。
   只能依据 title、title_zh 和 text；资料里没有的数字、结论、评价、公司名和模型名一律不要写；
   名称、数字和单位照抄原文的写法。
4. same：如果这一条和前面某一条（i 更小）讲的是同一件事，填那一条的 i；不是就不写这个字段。

只输出一个 JSON 对象，格式为
{{"items": [{{"i": 0, "cat": "domestic", "headline": "...", "body": "..."}}]}}。
每条输入都要有对应的输出，i 与输入一致。不要输出其他任何文字。"""
# 提示词的指纹：提示词改了以后，当周这一期由大模型按新提示词重写一遍（旧的写法不再沿用）
PROMPT_VERSION = hashlib.sha256(PROMPT.encode("utf-8")).hexdigest()[:8]


def last_week(today: date) -> date:
    """today 所在这一周的上一周的周一。"""
    return week_range(today)[0] - timedelta(days=7)


def due(root: Path, today: date, llm_ready: bool) -> date | None:
    """上一周的快讯需不需要生成（或重新生成），需要就返回那一周的周一。

    - 还没有：这一周有日报就生成；
    - 大模型有几条没写成（服务过载、额度用完）：有大模型可用时再补，最多补 MAX_TRIES 次；
    - 提示词改过了：有大模型可用时按新提示词重写；
    - 周一当天，俱乐部的统计还没覆盖到周日（仪表盘每天更新一次，凌晨时还停在前一天）：重新取一次。
    重新生成时，大模型已经写好的条目直接沿用，不会重写（提示词改过的除外）。
    """
    monday = last_week(today)
    note = load_week_note(root, week_id(monday)).get("kuaixun")
    if not isinstance(note, dict):
        return monday if week_payloads(root, monday) else None
    if llm_ready and note.get("pending") and note.get("tries", 0) < MAX_TRIES:
        return monday
    if llm_ready and note.get("prompt") != PROMPT_VERSION:
        return monday
    sunday = monday + timedelta(days=6)
    covered = str((note.get("club_period") or {}).get("end", ""))
    if today == sunday + timedelta(days=1) and covered < sunday.isoformat():
        return monday
    return None


def pool_of(payloads: dict[date, dict[str, Any]]) -> list[Item]:
    """这一周每天入选的内容。同一条只留第一次出现的那天（记在 extra["kx_day"]）。"""
    seen: set[str] = set()
    pool: list[Item] = []
    for day in sorted(payloads):
        for item in store.items_of(payloads[day]):
            if item.id in seen:
                continue
            seen.add(item.id)
            item.extra["kx_day"] = day.isoformat()
            pool.append(item)
    return pool


def shortlist(pool: list[Item], limits: Mapping[str, int], chinese: int = 0) -> list[Item]:
    """每个日报栏目按综合分取前几条，交给大模型分栏和改写。

    中文标题的 AI 动态（国内媒体的报道）另外再取 chinese 条：只按综合分取的话，前几十条几乎全是
    热度高的 Hacker News 帖子，国内公司的新闻排不进来，“国内动态”会是空的（第一期就是这样）。
    """
    ranked = sorted(pool, key=lambda item: item.score, reverse=True)
    picked: list[Item] = []
    for section, count in limits.items():
        picked += [item for item in ranked if item.section == section][: int(count)]
    taken = {id(item) for item in picked}
    extra = [item for item in ranked if item.section == "news" and CJK.search(item.title) and id(item) not in taken]
    return picked + extra[:chinese]


def guess(item: Item) -> str:
    """没有大模型时的分栏：政策、论文、开源项目照来源分；其余看原标题是不是中文。"""
    if item.source == policy.NAME:
        return "policy"
    if item.section in ("papers", "opensource"):
        return item.section
    return "domestic" if CJK.search(item.title) else "overseas"


def _allowed(item: Item) -> tuple[str, ...]:
    """大模型可以把这一条放进哪些栏目（skip 表示不登）。"""
    return (*_ALLOWED.get(item.source, _ALLOWED.get(item.section, WRITABLE)), "skip")


def _facts(item: Item) -> str:
    return f"{item.title} {item.title_zh} {item.summary_zh} {item.via} {evidence_of(item)}"


def _checked(name: str, value: object, limit: int, item: Item) -> str:
    text = plain(value, 0)
    if name == "正文":
        text = _DATE_PREFIX.sub("", text).strip()
    if not text:
        return ""
    problem = ""
    if len(text) > limit:
        problem = "太长"
    elif not CJK.search(text):
        problem = "没有写成中文"
    elif invented := ungrounded(text, _facts(item)):
        problem = "出现了资料里没有的 " + "、".join(invented)
    if problem:
        log.info("快讯不采用模型写的%s（%s）：%s", name, problem, item.title[:60])
        return ""
    return text


class _Writer:
    """交给 BatchRun 的两个函数：生成每一批的输入，核对并记下模型的输出。

    一批里的条目按顺序编号；same 指向同一批里更靠前的那一条，所以要记住当前这一批。
    """

    def __init__(self) -> None:
        self.batch: list[Item] = []

    def row(self, index: int, item: Item) -> dict[str, Any]:
        if index == 0:
            self.batch = []
        self.batch.append(item)
        row: dict[str, Any] = {"i": index, "section": item.section, "source": item.via, "title": item.title[:200]}
        if item.title_zh:
            row["title_zh"] = item.title_zh
        text = clean_text(f"{item.summary_zh} {evidence_of(item)}", EVIDENCE_CHARS)
        if text:
            row["text"] = text
        return row

    def apply(self, item: Item, row: dict[str, Any]) -> bool:
        cat = row.get("cat")
        allowed = _allowed(item)
        written = {
            "cat": cat if cat in allowed else "",
            "headline": _checked("标题", row.get("headline"), HEADLINE_LIMIT, item),
            "body": _checked("正文", row.get("body"), BODY_LIMIT, item),
        }
        position = next((i for i, other in enumerate(self.batch) if other is item), -1)
        same = row.get("same")
        if isinstance(same, int) and not isinstance(same, bool) and 0 <= same < position:
            written["same"] = self.batch[same].id
        item.extra["kx"] = written
        return bool(written["headline"] or written["body"])


def write(items: list[Item], client: LLMClient) -> int:
    """让大模型给这些条目分栏、写标题和正文，结果记在 extra["kx"]；返回写成的条数。"""
    todo = [item for item in items if "kx" not in item.extra and not item.extra.get("filtered")]
    if not todo:
        return 0
    writer = _Writer()
    run = BatchRun(client, PROMPT, writer.row, writer.apply, 260, reserve=0, depth=8)
    run.process(batches(todo, BATCH))
    log.info("大模型写快讯：%d/%d 条", run.done, len(todo))
    return run.done


def _when(item: Item, monday: date, sunday: date, offset: float) -> tuple[str, str]:
    """（日期，正文开头的日期写法）。发布日期在这一周里就写发布日期，否则写日报登出那天的“某日消息”。"""
    moment = parse_time(item.published)
    day = local_date(moment, offset) if moment else None
    if day and monday <= day <= sunday:
        return day.isoformat(), f"{day.month}月{day.day}日"
    seen = date.fromisoformat(item.extra.get("kx_day") or monday.isoformat())
    return seen.isoformat(), f"{seen.month}月{seen.day}日消息"


def entry_of(item: Item, cat: str, monday: date, sunday: date, offset: float) -> dict[str, Any] | None:
    """一条快讯。大模型没写成的部分用日报里的中文标题和摘要；连正文都没有的不登。"""
    written = item.extra.get("kx") or {}
    headline = written.get("headline") or item.title_zh or clean_text(item.title, 80)
    body = written.get("body") or item.summary_zh or clean_text(item.summary, 120)
    if not body and item.source == policy.NAME:
        body = f"据{policy.VIA}消息：{clean_text(item.title, 100)}"
    if not body:
        return None
    if body[-1] not in "。！？.!?…”）)":
        body += "。"
    day, when = _when(item, monday, sunday, offset)
    return {
        "cat": cat,
        "headline": headline,
        "when": when,
        "date": day,
        "body": body,
        "url": item.url,
        "via": item.via or item.source,
        "id": item.id,
        "ai": bool(written.get("headline") or written.get("body") or item.title_zh or item.summary_zh),
    }


def names(headline: str) -> frozenset[str]:
    """标题里的英文名称和数字（不分大小写），例如“DeepSeek 发布 V4.1 Flash”→ deepseek、v4.1、flash。"""
    words = (word.rstrip(".+-").casefold() for word in _NAME.findall(unicodedata.normalize("NFKC", headline)))
    return frozenset(word for word in words if word and word not in _GENERIC)


def same_story(a: frozenset[str], b: frozenset[str]) -> bool:
    """两条标题是不是讲同一件事：一条里的名称和数字（至少三个）全都出现在另一条里。

    大模型给的 same 字段靠不住（glm-4.7-flash 第一期一条都没标），同一件事又常常从几个来源进来，
    例如 Hacker News 和 Google 博客各有一条 Gemini 4 Argon。至少三个才算，免得“OpenAI 发布 GPT-6”
    和“OpenAI 发布 GPT-6 mini”这种只差一个词的被当成一件事。
    """
    small, large = sorted((a, b), key=len)
    return len(small) >= 3 and small <= large


def _subject(headline: str, companies: Mapping[str, list[str]]) -> str:
    """标题以名单里的公司开头时，返回它是 domestic 还是 overseas；否则返回空字符串。"""
    text = headline.strip().casefold()
    found = [
        (len(name), side) for side, rows in companies.items() for name in rows or [] if text.startswith(name.casefold())
    ]
    return max(found)[1] if found else ""


def assemble(
    candidates: list[Item],
    caps: Mapping[str, int],
    monday: date,
    sunday: date,
    offset: float,
    companies: Mapping[str, list[str]] | None = None,
) -> dict[str, list[dict[str, Any]]]:
    """按栏目挑出要登的条目：栏目内按综合分取前几条，再按日期排。

    - 讲同一件事的只登综合分最高的那条（大模型标的 same，加上程序按名称判断的）；
    - AI 动态里标题以名单里的公司开头的，按名单分到国内或海外动态：大模型会把 OpenAI 放进国内、
      把 DeepSeek 发布的模型放进开源项目（第一期实际出现过）。开源圈的条目不动，它们多是早就有的项目。
    """
    chosen: dict[str, list[dict[str, Any]]] = {name: [] for name, _ in KX_SECTIONS}
    taken: list[frozenset[str]] = []
    for item in sorted(candidates, key=lambda item: item.score, reverse=True):
        written = item.extra.get("kx") or {}
        cat = written.get("cat") if written.get("cat") in _allowed(item) else guess(item)  # 旧数据也按现在的规则
        if cat == "skip" or written.get("same"):
            continue
        entry = entry_of(item, cat, monday, sunday, offset)
        if not entry:
            continue
        if cat in ("domestic", "overseas") or (cat == "opensource" and item.section == "news"):
            cat = entry["cat"] = _subject(entry["headline"], companies or {}) or cat
        key = names(entry["headline"])
        if len(chosen[cat]) >= int(caps.get(cat, 0)) or any(same_story(key, other) for other in taken):
            continue
        taken.append(key)
        chosen[cat].append(entry)
    for rows in chosen.values():
        rows.sort(key=lambda entry: entry["date"])
    return chosen


def _attempt(report: list[dict[str, Any]], name: str, title: str, job) -> Any:
    """跑一个外部数据源，成败记进报告；失败返回 None。"""
    try:
        result = job()
    except Exception as exc:  # 任何一个数据源出问题都不能让快讯出不来
        log.warning("快讯的%s取不到：%s", title, exc)
        report.append({"name": name, "title": title, "ok": False, "error": clean_text(str(exc), 200)})
        return None
    report.append({"name": name, "title": title, "ok": True, "error": ""})
    return result


def build(
    root: Path,
    config: dict[str, Any],
    monday: date,
    *,
    client: LLMClient | None,
    http: Http,
    env: Mapping[str, str],
    now: datetime,
    reuse: bool = True,
) -> dict[str, Any]:
    """生成 monday 这一周的快讯（返回要存进周记录的数据，不写文件）。

    reuse 为真时，上一次大模型已经写好的条目直接沿用，只补没写成的；提示词改过、而且这次有大模型可用时全部重写。
    """
    settings, offset = config["kuaixun"], config["utc_offset_hours"]
    sunday = monday + timedelta(days=6)
    week = week_id(monday)
    previous = load_week_note(root, week).get("kuaixun") or {}
    kept = [entry for entry in previous.get("entries") or [] if isinstance(entry, dict)]
    report: list[dict[str, Any]] = []
    ctx = Context(http=http, now=now, keywords=KeywordMatcher(config["keywords"]), env=env)

    fetched = _attempt(report, "club", club.VIA, lambda: club.fetch(ctx, settings["club"], monday, sunday, offset))
    club_entries, club_period = fetched or ([e for e in kept if e.get("cat") == "club"], previous.get("club_period"))
    policies = _attempt(report, "policy", policy.VIA, lambda: policy.fetch(http, monday, sunday, settings["policy"]))
    beijing = local_time(now, offset).replace(tzinfo=None)
    events = _attempt(report, "events", deadlines.VIA, lambda: deadlines.fetch(http, beijing, settings["events"]))
    if events is None:
        events = [entry for entry in kept if entry.get("cat") == "events"]

    payloads = week_payloads(root, monday)
    candidates = shortlist(pool_of(payloads), settings["candidates"], int(settings.get("chinese_news", 0)))
    candidates += policies or []
    fresh = previous.get("prompt") == PROMPT_VERSION
    rewrite = not reuse or (client is not None and not fresh)  # 没有大模型时宁可沿用旧写法，也不退回日报的文字
    cache = {} if rewrite else previous.get("written") or {}
    for item in candidates:  # 上次已经写好的直接沿用
        if isinstance(cache.get(item.id), dict):
            item.extra["kx"] = cache[item.id]
    waiting = [item for item in candidates if "kx" not in item.extra]
    attempted = client is not None and not client.exhausted and bool(waiting)  # 真的要请求时才算补了一次
    if client is not None and attempted:
        try:
            excerpt.enrich([item for item in candidates if item.source == policy.NAME], http)
            write(candidates, client)
        except Exception:
            log.exception("大模型写快讯出错，用日报里的中文标题和摘要")

    caps = settings["caps"]
    chosen = assemble(candidates, caps, monday, sunday, offset, settings.get("companies"))
    if policies is None:  # 政策列表这次取不到：沿用上次的
        chosen["policy"] = [entry for entry in kept if entry.get("cat") == "policy"]
    chosen["club"] = club_entries[: int(caps.get("club", 0))]
    chosen["events"] = events[: int(caps.get("events", 0))]
    entries = [entry for name, _ in KX_SECTIONS for entry in chosen[name]]

    models = [*previous.get("models", [])]
    models += [str((payload.get("llm") or {}).get("model") or "") for payload in payloads.values()]
    models += [provider.model for provider in client.answered] if client else []
    return {
        "week": week,
        "start": monday.isoformat(),
        "end": sunday.isoformat(),
        "generated_at": to_iso(now),
        "models": list(dict.fromkeys(name for name in models if name)),
        "prompt": PROMPT_VERSION if fresh or rewrite else previous.get("prompt", ""),
        "tries": (0 if rewrite else int(previous.get("tries", 0))) + attempted,
        "pending": sum("kx" not in item.extra and not item.extra.get("filtered") for item in candidates),
        "club_period": club_period,
        "sources": report,
        "entries": entries,
        "written": {item.id: item.extra["kx"] for item in candidates if "kx" in item.extra},
    }
