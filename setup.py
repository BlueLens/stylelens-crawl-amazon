# coding: utf-8

"""
    stylelens-crawl-amazon

    Contact: master@bluehack.net
"""


import sys
from setuptools import setup, find_packages

NAME = "stylelens-crawl-amazon"
VERSION = "0.0.36"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["pymongo","bottlenose","bs4"]

setup(
    name=NAME,
    version=VERSION,
    description="stylelens-crawl-amazon",
    author_email="master@bluehack.net",
    url="",
    keywords=["BlueLens", "stylelens-crawl-amazon"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)
