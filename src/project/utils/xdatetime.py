from datetime import date
from datetime import datetime
from typing import NamedTuple
from typing import Optional
from typing import Union

import pytz
import requests
from delorean import Delorean
from django.conf import settings
from django.http import HttpRequest


def utcnow() -> datetime:
    return Delorean().datetime
