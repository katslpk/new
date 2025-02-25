from datetime import date
from datetime import datetime
from typing import NamedTuple
from typing import Optional

import requests
from delorean import Delorean
from django.conf import settings

from project.utils.safeguards import safe


def utcnow() -> datetime:
    return Delorean().datetime


def now(timezone: Optional[str] = None) -> datetime:
    tz = timezone or settings.TIME_ZONE
    return Delorean().shift(tz).datetime


def near(dt1: datetime, dt2: datetime, interval=0):
    delta = abs(dt1 - dt2)
    return delta.total_seconds() <= interval


@safe
def retrieve_tz(ip: str):
    resp = requests.get(f"http://ip-api.com/json/{ip}")
    if resp.status_code != 200:
        return None

    payload = resp.json()
    tz_name = payload.get("timezone")
    return tz_name


class DateDelta(NamedTuple):
    years: int
    months: int

    def __str__(self):
        parts = []

        if self.years:
            suffix = "s" if (self.years % 10) != 1 else ""
            parts.append(f"{self.years} y{suffix}")

        if self.months:
            suffix = "s" if (self.months % 10) != 1 else ""
            parts.append(f"{self.months} mo{suffix}")

        if not any((self.years, self.months)):
            parts.append("<1 mo")

        return " ".join(parts)

    @classmethod
    def build(cls, start: date, finish: Optional[date] = None) -> "DateDelta":
        finish = finish or utcnow().date()
        delta = finish - start
        years, days = divmod(delta.days, 365)
        months = days // 30
        return DateDelta(years=years, months=months)
