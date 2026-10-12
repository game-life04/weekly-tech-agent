"""日期小工具：本地日期、ISO 周、时间格式转换。"""

from __future__ import annotations

from datetime import UTC, date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

_WEEKDAYS = "一二三四五六日"


def local_time(now: datetime, utc_offset_hours: float) -> datetime:
    """把时间换到配置的时区。中国没有夏令时，用固定偏移就够了，也省掉时区数据库这个依赖。"""
    return now.astimezone(timezone(timedelta(hours=utc_offset_hours)))


def local_date(now: datetime, utc_offset_hours: float) -> date:
    return local_time(now, utc_offset_hours).date()


def weekday_name(day: date) -> str:
    return "周" + _WEEKDAYS[day.weekday()]


def week_id(day: date) -> str:
    """ISO 周编号，例如 2026-W41。跨年的那一周按 ISO 规则归到对应年份。"""
    year, week, _ = day.isocalendar()
    return f"{year}-W{week:02d}"


def week_range(day: date) -> tuple[date, date]:
    """day 所在这一周的周一和周日。"""
    monday = day - timedelta(days=day.weekday())
    return monday, monday + timedelta(days=6)


def to_iso(value: object) -> str:
    """统一存成 UTC 的 ISO 8601 字符串，例如 2026-10-11T03:20:00Z。

    接受 parse_time 能认的任何写法（时间对象、时间戳、字符串）；认不出来返回空字符串。
    """
    moment = parse_time(value)
    return moment.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ") if moment else ""


def parse_time(value: object) -> datetime | None:
    """尽力把各种时间写法解析成带时区的时间；解析不了返回 None。

    支持 Unix 时间戳、ISO 8601（含结尾的 Z）和 RSS 常用的 RFC 2822。
    """
    if value is None or value == "":
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=UTC)
    try:
        if isinstance(value, (int, float)):
            return datetime.fromtimestamp(float(value), tz=UTC)
        text = str(value).strip()
        try:
            parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
        except ValueError:
            parsed = parsedate_to_datetime(text)
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)
    except (ValueError, TypeError, OverflowError, OSError):
        return None
