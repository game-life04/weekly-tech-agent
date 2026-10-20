"""每周快讯和每日快讯：参照《CCF开源快讯》的体例，把一周（或一天）的内容整理成一期速读。

每周一生成上周一到周日的一期；每天的日报出完以后，再用当天的内容生成一期每日快讯。栏目和顺序见 models.KX_SECTIONS：
- 俱乐部动态：俱乐部 GitHub 组织的周统计、最活跃的仓库、新仓库和新版本，由程序根据接口数据写成（club.py）；
- 政策动向：中国政府网上和人工智能、开源、软件有关的条目（policy.py）；
- 国内动态、海外动态、开源项目、学术前沿、产业纵横：从这一周每天的日报里挑。大模型负责分栏，
  按“主体+动作+对象”写标题，写一两句正文，并指出讲同一件事的重复条目；
- 活动预告：接下来几周截稿的 CCF 推荐会议（deadlines.py）。

和日报一样，大模型只写栏目、标题和正文，日期、链接、来源和统计数字都由程序填写；
写出了资料里没有的英文名称或数字、或者没写成中文的，就不用，退回日报里已经核对过的中文标题和摘要。
每周快讯存进 data/weekly/<周>.json，每日快讯存进当天数据的 kuaixun 字段；页面只凭这些数据生成，
重新排版不需要网络和大模型。
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
from urllib.parse import urlsplit

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
WRITABLE = ("domestic", "overseas", "opensource", "papers", "industry", "events")  # 日报的 AI 动态可以放进这些栏目
# 其余条目只能留在对应的栏目或不登：热门仓库多是早就有的项目，被写成“某公司发布”会误导人（第一期出现过）
_ALLOWED = {policy.NAME: ("policy",), "opensource": ("opensource",), "papers": ("papers",)}
_DATE_PREFIX = re.compile(r"^(?:\d{4}年)?\d{1,2}月\d{1,2}日(?:[至到—–-]\d{1,2}日)?(?:消息)?[，,、。.\s]*")
_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9.+-]*")
_GENERIC = frozenset(["ai", "llm", "api"])  # 比较两条是不是同一件事时不算数的通用词
# 活动日期的写法：10月22日、10月22-24日、10月30日至11月1日
_EVENT_WHEN = re.compile(r"(\d{1,2})月(\d{1,2})(?:日|日?[-–—~至到](?:(\d{1,2})月)?(\d{1,2})日)")
_MONTHS = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")

PROMPT = f"""你是《每周科技快讯》的编辑，参照《CCF开源快讯》的体例，为关注人工智能和开源的中国大学生整理上周要闻。
{DATA_NOTE}

每一条有 title（原标题）、title_zh（中文标题，可能没有）、text（资料）、source（来源）、site（原文所在的网站）
和 section（日报里的栏目）。
对每一条：
1. cat：放进哪个栏目。
   section 是 news 的，只能是下面之一：
     domestic 国内动态：中国的公司、高校和机构的发布与动作，包括它们开源的模型和项目；
     overseas 海外动态：海外的公司、高校和机构的发布与动作，包括它们开源的模型和项目；
     opensource 开源项目：社区开源项目的新闻，不是某家公司或机构的动作；
     papers 学术前沿：研究成果和技术文章；
     industry 产业纵横：已经举办的产业大会和论坛、行业标准、大额融资和并购、市场和产业数据；
     events 活动预告：还没举办的会议、论坛、比赛和开源活动，资料里写明了举办日期；
     skip：和人工智能、开源关系不大；个人观点、评论、调查报告和安全事件；资料太少、说不清是什么。
     OpenAI、Google、Meta、Anthropic、英伟达、微软是海外公司；DeepSeek、阿里、腾讯、百度、字节跳动、华为、智谱是中国公司。
     官方博客上的文章，发布方就是网站的主人，例如 site 是 research.meta.ai 的是 Meta，openai.com 的是 OpenAI。
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
4. when：只有 cat 是 events 时才写：活动举办的日期，照资料写成“10月22日”或“10月22-24日”。
5. same：如果这一条和前面某一条（i 更小）讲的是同一件事，填那一条的 i；不是就不写这个字段。

只输出一个 JSON 对象，格式为
{{"items": [{{"i": 0, "cat": "domestic", "headline": "...", "body": "..."}},
{{"i": 1, "cat": "events", "headline": "...", "body": "...", "when": "10月22-24日"}}]}}。
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


def _event_when(value: object, item: Item) -> str:
    """模型写的活动日期：格式要对，月和日的数字（或英文月份）都要在资料里出现过；不合格返回空字符串。"""
    text = plain(value, 30).replace(" ", "")
    match = _EVENT_WHEN.fullmatch(text)
    if not match:
        return ""
    facts = _facts(item).casefold()
    months = [int(n) for n in (match.group(1), match.group(3)) if n]
    days = [int(n) for n in (match.group(2), match.group(4)) if n]

    def seen(number: int) -> bool:
        return re.search(rf"(?<!\d)0?{number}(?!\d)", facts) is not None

    if all(seen(m) or _MONTHS[m - 1] in facts for m in months if 1 <= m <= 12) and all(seen(d) for d in days):
        return text
    log.info("快讯不采用模型写的活动日期 %s（资料里找不到）：%s", text, item.title[:60])
    return ""


def event_day(when: str, monday: date) -> date | None:
    """活动日期的第一天。年份按这一期所在的年份算，跨年的（一月的活动在十二月预告）算到下一年。"""
    match = _EVENT_WHEN.fullmatch(when or "")
    if not match:
        return None
    try:
        day = date(monday.year, int(match.group(1)), int(match.group(2)))
    except ValueError:
        return None
    return day if day >= monday - timedelta(days=120) else day.replace(year=monday.year + 1)


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
        row["site"] = (urlsplit(item.url).hostname or "").removeprefix("www.")
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
        if written["cat"] == "events":  # 活动要有资料里写明的日期，没有就不登
            written["when"] = _event_when(row.get("when"), item)
            written["cat"] = "events" if written["when"] else "skip"
        position = next((i for i, other in enumerate(self.batch) if other is item), -1)
        same = row.get("same")
        if isinstance(same, int) and not isinstance(same, bool) and 0 <= same < position:
            written["same"] = self.batch[same].id
        written["v"] = PROMPT_VERSION  # 按哪一版提示词写的
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


def _when(item: Item, start: date, end: date, offset: float) -> tuple[str, str]:
    """（日期，正文开头的日期写法）。发布日期在这一期的范围里就写发布日期，否则写日报登出那天的“某日消息”。"""
    moment = parse_time(item.published)
    day = local_date(moment, offset) if moment else None
    if day and start <= day <= end:
        return day.isoformat(), f"{day.month}月{day.day}日"
    seen = date.fromisoformat(item.extra.get("kx_day") or start.isoformat())
    return seen.isoformat(), f"{seen.month}月{seen.day}日消息"


def entry_of(item: Item, cat: str, start: date, end: date, offset: float) -> dict[str, Any] | None:
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
    day, when = _when(item, start, end, offset)
    if cat == "events":  # 活动写举办日期；这一期范围之内已经开始的不预告
        opening = event_day(written.get("when", ""), start)
        if opening is None or opening <= end:
            return None
        day, when = opening.isoformat(), written["when"]
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


def _words(headline: str) -> list[str]:
    """标题里的英文名称和数字（不分大小写），例如“DeepSeek 发布 V4.1 Flash”→ deepseek、v4.1、flash。"""
    words = (word.rstrip(".+-").casefold() for word in _NAME.findall(unicodedata.normalize("NFKC", headline)))
    return [word for word in words if word and word not in _GENERIC]


def same_story(a: str, b: str) -> bool:
    """两条标题是不是讲同一件事。大模型给的 same 字段靠不住（glm-4.7-flash 第一期一条都没标），
    同一件事又常常从几个来源进来。满足下面任意一条就算：

    - 一条里的名称和数字（至少三个）全都出现在另一条里：Hacker News 和 Google 博客各有一条 Gemini 4 Argon；
    - 去掉空格和连字符以后，一条的英文部分（至少 12 个字符）整个出现在另一条里：
      “DeepSeek 更新 V4.1 Flash”和“DeepSeek 开放 V4.1-Flash-1017”（第一期实际出现过）。
    门槛定得高一些，免得“OpenAI 发布 GPT-6”和“OpenAI 发布 GPT-6 mini”这种只差一个词的被当成一件事。
    """
    words_a, words_b = _words(a), _words(b)
    small, large = sorted((set(words_a), set(words_b)), key=len)
    if len(small) >= 3 and small <= large:
        return True
    short, long = sorted(("".join(words_a).replace("-", ""), "".join(words_b).replace("-", "")), key=len)
    return len(short) >= 12 and short in long


def _site(url: str, sites: Mapping[str, list[str]]) -> str:
    """原文在名单里的官方网站上时，返回 domestic 或 overseas；否则返回空字符串。"""
    host = (urlsplit(url).hostname or "").casefold()
    for side, rows in sites.items():
        if any(host == site.casefold() or host.endswith("." + site.casefold()) for site in rows or []):
            return side
    return ""


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
    start: date,
    end: date,
    offset: float,
    companies: Mapping[str, list[str]] | None = None,
    sites: Mapping[str, list[str]] | None = None,
) -> dict[str, list[dict[str, Any]]]:
    """按栏目挑出要登的条目：栏目内按综合分取前几条，再按日期排。

    - 讲同一件事的只登综合分最高的那条（大模型标的 same，加上程序按名称判断的）；
    - AI 动态里标题以名单里的公司开头的，按名单分到国内或海外动态：大模型会把 OpenAI 放进国内、
      把 DeepSeek 发布的模型放进开源项目（第一期实际出现过）。开源圈的条目不动，它们多是早就有的项目。
    """
    chosen: dict[str, list[dict[str, Any]]] = {name: [] for name, _ in KX_SECTIONS}
    taken: list[str] = []  # 已经登的标题
    for item in sorted(candidates, key=lambda item: item.score, reverse=True):
        written = item.extra.get("kx") or {}
        cat = written.get("cat") if written.get("cat") in _allowed(item) else guess(item)  # 旧数据也按现在的规则
        if cat == "skip" or written.get("same"):
            continue
        entry = entry_of(item, cat, start, end, offset)
        if not entry:
            continue
        if cat in ("domestic", "overseas") or (cat == "opensource" and item.section == "news"):
            side = _subject(entry["headline"], companies or {}) or _site(item.url, sites or {})
            cat = entry["cat"] = side or cat
        if len(chosen[cat]) >= int(caps.get(cat, 0)) or any(same_story(entry["headline"], h) for h in taken):
            continue
        taken.append(entry["headline"])
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


def _compose(
    config: dict[str, Any],
    previous: dict[str, Any],
    payloads: list[dict[str, Any]],
    candidates: list[Item],
    *,
    window: tuple[date, date],
    policy_window: tuple[date, date],
    club_days: int,
    club_window: tuple[date, date] | None,
    event_days: int,
    caps: Mapping[str, int],
    client: LLMClient | None,
    http: Http,
    env: Mapping[str, str],
    now: datetime,
    reuse: bool,
) -> dict[str, Any]:
    """每周快讯和每日快讯共用的部分：取俱乐部、政策和会议截稿，让大模型改写候选，按栏目挑出要登的条目。

    window 是这一期的日期范围（发布日期在范围里的写发布日期，活动要在范围之后才算预告）。
    reuse 为真时，上一次大模型已经写好的条目直接沿用，只补没写成的；提示词改过、而且这次有大模型可用时全部重写，
    重写没成功的条目先用旧的写法顶着，记作待补。
    """
    settings, offset = config["kuaixun"], config["utc_offset_hours"]
    start, end = window
    kept = [entry for entry in previous.get("entries") or [] if isinstance(entry, dict)]
    report: list[dict[str, Any]] = []
    ctx = Context(http=http, now=now, keywords=KeywordMatcher(config["keywords"]), env=env)

    fetched = _attempt(
        report,
        "club",
        club.VIA,
        lambda: club.fetch(ctx, settings["club"], offset, days=club_days, window=club_window),
    )
    covered = (fetched or ([], {}))[1].get("end", "")
    if fetched and club_window and previous.get("club_period") and covered > club_window[1].isoformat():
        # 仪表盘只能查“最近 N 天”：过了这一期再重新生成时（例如周二补写上周的快讯），新取到的统计已经
        # 不是这一期了，沿用上一次取到的（10-20 重写 W42 时实际出现过）
        log.info("俱乐部仪表盘的统计已经到了 %s，超出这一期，沿用上一次的俱乐部动态", covered)
        fetched = None
    club_entries, club_period = fetched or ([e for e in kept if e.get("cat") == "club"], previous.get("club_period"))
    policies = _attempt(report, "policy", policy.VIA, lambda: policy.fetch(http, *policy_window, settings["policy"]))
    beijing = local_time(now, offset).replace(tzinfo=None)
    event_settings = {**settings["events"], "days": event_days}
    events = _attempt(report, "events", deadlines.VIA, lambda: deadlines.fetch(http, beijing, event_settings))
    if events is None:
        events = [entry for entry in kept if entry.get("cat") == "events"]

    candidates = candidates + (policies or [])
    old, old_version = previous.get("written") or {}, previous.get("prompt", "")
    fresh = old_version == PROMPT_VERSION
    for item in candidates:  # 上次已经写好的直接沿用；没有大模型时，旧提示词写的也照用
        cached = old.get(item.id)
        if isinstance(cached, dict) and reuse and (client is None or cached.get("v", old_version) == PROMPT_VERSION):
            item.extra["kx"] = cached
    waiting = [item for item in candidates if "kx" not in item.extra]
    attempted = client is not None and not client.exhausted and bool(waiting)  # 真的要请求时才算补了一次
    if client is not None and attempted:
        try:
            excerpt.enrich([item for item in candidates if item.source == policy.NAME], http)
            write(candidates, client)
        except Exception:
            log.exception("大模型写快讯出错，用日报里的中文标题和摘要")
    # 按新提示词没写成的，先用旧的写法顶着、记作待补，不退回日报的文字（10-19 晚高峰重写时 68 条全部失败）
    for item in candidates:
        if "kx" not in item.extra and isinstance(old.get(item.id), dict):
            item.extra["kx"], item.extra["kx_stale"] = old[item.id], True

    chosen = assemble(candidates, caps, start, end, offset, settings.get("companies"), settings.get("sites"))
    if policies is None:  # 政策列表这次取不到：沿用上次的
        chosen["policy"] = [entry for entry in kept if entry.get("cat") == "policy"]
    chosen["club"] = club_entries[: int(caps.get("club", 0))]
    # 活动预告：新闻里预告的活动和会议截稿放在一起，按日期排
    upcoming = sorted(chosen["events"] + events, key=lambda entry: entry["date"])
    chosen["events"] = upcoming[: int(caps.get("events", 0))]
    entries = [entry for name, _ in KX_SECTIONS for entry in chosen[name]]

    models = [*previous.get("models", [])]
    models += [str((payload.get("llm") or {}).get("model") or "") for payload in payloads]
    models += [provider.model for provider in client.answered] if client else []
    return {
        "start": start.isoformat(),
        "end": end.isoformat(),
        "generated_at": to_iso(now),
        "models": list(dict.fromkeys(name for name in models if name)),
        "prompt": PROMPT_VERSION if fresh or attempted else old_version,
        "tries": (int(previous.get("tries", 0)) if fresh else 0) + attempted,
        "pending": sum(
            ("kx" not in item.extra or bool(item.extra.get("kx_stale"))) and not item.extra.get("filtered")
            for item in candidates
        ),
        "club_period": club_period,
        "sources": report,
        "entries": entries,
        # 每条记下是按哪一版提示词写的（早期的数据没有这一项，就是上一期整体的版本）
        "written": {item.id: {"v": old_version, **item.extra["kx"]} for item in candidates if "kx" in item.extra},
    }


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
    """生成 monday 这一周的快讯（返回要存进周记录的数据，不写文件）。"""
    settings = config["kuaixun"]
    sunday = monday + timedelta(days=6)
    week = week_id(monday)
    payloads = week_payloads(root, monday)
    issue = _compose(
        config,
        load_week_note(root, week).get("kuaixun") or {},
        list(payloads.values()),
        shortlist(pool_of(payloads), settings["candidates"], int(settings.get("chinese_news", 0))),
        window=(monday, sunday),
        policy_window=(monday, sunday),
        club_days=7,
        club_window=(monday, sunday),
        event_days=int(settings["events"].get("days", 45)),
        caps=settings["caps"],
        client=client,
        http=http,
        env=env,
        now=now,
        reuse=reuse,
    )
    return {"kind": "weekly", "week": week, **issue}


def build_day(
    root: Path,
    config: dict[str, Any],
    day: date,
    *,
    client: LLMClient | None,
    http: Http,
    env: Mapping[str, str],
    now: datetime,
    reuse: bool = True,
) -> dict[str, Any]:
    """生成 day 这一天的每日快讯（返回要存进当天数据的 kuaixun 字段，不写文件）。

    候选就是当天日报入选的全部内容；政策看前一天和当天；俱乐部看仪表盘最近一天的统计；
    会议截稿看接下来 event_days 天。发布日期在前两天以内的写发布日期，更早的写“某日消息”。
    """
    daily = config["kuaixun"]["daily"]
    payload = store.load_day(root, day) or {}
    items = store.items_of(payload)
    for item in items:
        item.extra["kx_day"] = day.isoformat()
    issue = _compose(
        config,
        payload.get("kuaixun") or {},
        [payload],
        items,
        window=(day - timedelta(days=2), day),
        policy_window=(day - timedelta(days=1), day),
        club_days=1,
        club_window=None,
        event_days=int(daily.get("event_days", 14)),
        caps=daily["caps"],
        client=client,
        http=http,
        env=env,
        now=now,
        reuse=reuse,
    )
    return {"kind": "daily", "day": day.isoformat(), **issue, "start": day.isoformat()}


def daily_due(payload: dict[str, Any] | None, llm_ready: bool) -> bool:
    """当天的每日快讯要不要生成（或补全）：还没有；或者有大模型可用，而且有没写成的、或提示词改过了。"""
    issue = (payload or {}).get("kuaixun")
    if not (payload or {}).get("items"):
        return False
    if not isinstance(issue, dict):
        return True
    if not llm_ready:
        return False
    return bool(issue.get("pending") and issue.get("tries", 0) < MAX_TRIES) or issue.get("prompt") != PROMPT_VERSION
