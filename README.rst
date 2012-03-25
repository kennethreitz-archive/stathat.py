stathat.py
==========

A minimalistic API wrapper for StatHat.com, powered by Requests.

Usage::

    >>> from stathat import StatHat
    >>> stats = StatHat('me@kennethreitz.com')
    >>> stats.count('wtfs/minute', 10)
    True
    >>> stats.count('connections.active', 85092)
    True

Enjoy.


Installation
------------

Installation is simple::

    $ pip install stathat