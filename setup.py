#!/usr/bin/python3
from setuptools import setup, find_packages

setup(
    name="nicer-tests",
    version="0.1.0",
    description="A bunch of routines I wrote to make testing a nicer experience",
    author="Pradyun S. Gedam",
    author_email="pradyunsg@gmail.com",
    install_requires=["nose", "PyYAML"],
    packages=find_packages(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
    ]
)
