#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import stathat

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

required = ['requests']

setup(
    name='stathat',
    version='0.0.1',
    description='StatHat.com API Wrapper.',
    long_description=stathat.__doc__,
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/stathat.py',
    py_modules= ['stathat'],
    install_requires=required,
    license='MIT',
    use_2to3 = True,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
    ),
)
