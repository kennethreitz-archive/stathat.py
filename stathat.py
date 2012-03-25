# -*- coding: utf-8 -*-

"""
stathat.py
~~~~~~~~~~

A minimalistic API wrapper for StatHat.com, powered by Requests.

Usage::

    >>> from stathat import StatHat
    >>> stats = StatHat('me@kennethreitz.com')
    >>> stats.count('wtfs/minute', 10)
    True
    >>> stats.count('connections.active', 85000)
    True

Enjoy.

"""

import sys

try:
    # Lazy setup.py __doc__ hack.
    import requests
except ImportError:
    print >> sys.sterr, 'warning: requests module is required.'

DEFAULT_STATHAT_URL = 'http://api.stathat.com'


class StatHat(object):
    """The StatHat API wrapper."""

    STATHAT_URL = DEFAULT_STATHAT_URL

    def __init__(self, email=None):
        self.email = email

        # Enable keep-alive and connection-pooling.
        self.session = requests.session()

    def _http_post(self, path, data):
        url = self.STATHAT_URL + path
        r = self.session.post(url, data=data, prefetch=True)
        return r

    def value(self, key, value):
        r = self._http_post('/ez', {'email': self.email, 'stat': key, 'value': value})
        return r.okay

    def count(self, key, count):
        r = self._http_post('/ez', {'email': self.email, 'stat': key, 'count': count})
        return r.ok