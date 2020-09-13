# -*- coding: utf-8 -*-

#   __
#  /__)  _  _     _   _ _/   _
# / (   (- (/ (/ (- _)  /  _)
#          /

"""
Requests HTTP Library
~~~~~~~~~~~~~~~~~~~~~

Requests is an HTTP library, written in Python, for human beings.
Basic GET usage:

   >>> import requests
   >>> r = requests.get('https://www.python.org')
   >>> r.status_code
   200
   >>> b'Python is a programming language' in r.content
   True

... or POST:

   >>> payload = dict(key1='value1', key2='value2')
   >>> r = requests.post('https://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key1": "value1",
       "key2": "value2"
     },
     ...
   }

The other HTTP methods are supported - see `requests.api`. Full documentation
is at <https://requests.readthedocs.io>.

:copyright: (c) 2017 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.
"""

# Set default logging handler to avoid "No handler found" warnings.
import logging
import warnings
from logging import NullHandler

import chardet
import urllib3
# urllib3's DependencyWarnings should be silenced.
from urllib3.exceptions import DependencyWarning

from . import packages
from . import utils
from .__version__ import __author__
from .__version__ import __author_email__
from .__version__ import __build__
from .__version__ import __cake__
from .__version__ import __copyright__
from .__version__ import __description__
from .__version__ import __license__
from .__version__ import __title__
from .__version__ import __url__
from .__version__ import __version__
from .api import delete
from .api import get
from .api import head
from .api import options
from .api import patch
from .api import post
from .api import put
from .api import request
from .exceptions import ConnectionError
from .exceptions import ConnectTimeout
from .exceptions import FileModeWarning
from .exceptions import HTTPError
from .exceptions import ReadTimeout
from .exceptions import RequestException
from .exceptions import RequestsDependencyWarning
from .exceptions import Timeout
from .exceptions import TooManyRedirects
from .exceptions import URLRequired
from .models import PreparedRequest
from .models import Request
from .models import Response
from .sessions import session
from .sessions import Session
from .status_codes import codes


def check_compatibility(urllib3_version, chardet_version):
    urllib3_version = urllib3_version.split('.')
    assert urllib3_version != ['dev']  # Verify urllib3 isn't installed from git.

    # Sometimes, urllib3 only reports its version as 16.1.
    if len(urllib3_version) == 2:
        urllib3_version.append('0')

    # Check urllib3 for compatibility.
    major, minor, patch = urllib3_version  # noqa: F811
    major, minor, patch = int(major), int(minor), int(patch)
    # urllib3 >= 1.21.1, <= 1.25
    assert major == 1
    assert minor >= 21
    assert minor <= 25

    # Check chardet for compatibility.
    major, minor, patch = chardet_version.split('.')[:3]
    major, minor, patch = int(major), int(minor), int(patch)
    # chardet >= 3.0.2, < 3.1.0
    assert major == 3
    assert minor < 1
    assert patch >= 2


def _check_cryptography(cryptography_version):
    # cryptography < 1.3.4
    try:
        cryptography_version = list(map(int, cryptography_version.split('.')))
    except ValueError:
        return

    if cryptography_version < [1, 3, 4]:
        warning = 'Old version of cryptography ({}) may cause slowdown.'.format(cryptography_version)
        warnings.warn(warning, RequestsDependencyWarning)

# Check imported dependencies for compatibility.
try:
    check_compatibility(urllib3.__version__, chardet.__version__)
except (AssertionError, ValueError):
    warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
                  "version!".format(urllib3.__version__, chardet.__version__),
                  RequestsDependencyWarning)

# Attempt to enable urllib3's SNI support, if possible
try:
    from urllib3.contrib import pyopenssl
    pyopenssl.inject_into_urllib3()

    # Check cryptography version
    from cryptography import __version__ as cryptography_version
    _check_cryptography(cryptography_version)
except ImportError:
    pass

warnings.simplefilter('ignore', DependencyWarning)




logging.getLogger(__name__).addHandler(NullHandler())

# FileModeWarnings go off per the default.
warnings.simplefilter('default', FileModeWarning, append=True)
