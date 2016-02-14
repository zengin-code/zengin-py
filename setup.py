#!/usr/bin/env python
# -*- conding:utf-8 -*-

try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    print("Please install setuptools.")

import sys

if sys.version_info < (3, 5, 0):
    sys.stderr.write("zengin-py is require Python 3.5.0 or newer.\n")
    sys.exit(-1)

from zengin import info

setup(
    name=info.__name__,
    version=info.__version__,
    description=info.__description__,
    long_description=info.__long_description__,
    author=info.__author__,
    author_email=info.__author_email__,
    license=info.__license__,
    url=info.__url__,
    packages=find_packages(exclude=['tests']),
    package_data={'source-data': ['data/banks.json']},
    include_package_data=True,
    classifiers=info.__classifiers__,
    scripts=["bin/zengin.py"]
)
