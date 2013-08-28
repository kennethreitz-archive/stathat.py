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
    >>> stats.count('connections.active', 85092)
    True

Enjoy.

"""

import requests

DEFAULT_STATHAT_URL = 'https://api.stathat.com'


class StatHat(object):
    """The StatHat API wrapper."""

    STATHAT_URL = DEFAULT_STATHAT_URL

    def __init__(self, email=None):
        self.email = email

        # Enable keep-alive and connection-pooling.
        self.session = requests.session()

    def _http_post(self, path, data):
        url = self.STATHAT_URL + path
        r = self.session.post(url, data=data)
        return r

    def value(self, key, value, timestamp=None):
        data = {'email': self.email, 'stat': key, 'value': value}
        if timestamp:
            data['t'] = timestamp
        r = self._http_post('/ez', data)
        return r.ok

    def count(self, key, count, timestamp=None):
        data = {'email': self.email, 'stat': key, 'count': count}
        if timestamp:
            data['t'] = timestamp
        r = self._http_post('/ez', data)
        return r.ok
