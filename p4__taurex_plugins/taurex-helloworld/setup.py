#!/usr/bin/env python
import setuptools
from setuptools import find_packages
from distutils.core import setup
from distutils.core import Extension
from distutils import log
import re, os

packages = find_packages(exclude=("tests", "doc"))
provides = [
    "taurex_helloworld",
]

requires = []

install_requires = [
    "taurex",
]

entry_points = {"taurex.plugins": "helloworld = taurex_helloworld"}

with open("README.md", "r") as fh:
    long_description = fh.read()

version = "0.0.1-alpha"

setup(
    name="taurex_helloworld",
    author="author name",
    author_email="author@email",
    license="BSD",
    description="Helloworld plugin for TauREx-3 ",
    packages=packages,
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points=entry_points,
    version=version,
    keywords=[
        "exoplanet",
        "helloworld",
        "taurex",
        "chemistry" "taurex",
        "plugin",
        "taurex3",
        "atmosphere",
        "atmospheric",
    ],
    provides=provides,
    requires=requires,
    install_requires=install_requires,
)
