import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "persian_silver_2",
    version = "0.0.1",
    author = "Martin Hanekom",
    author_email = "martin.b.hanekom@gmail.com",
    description = ("Persian Silver 2 is a turn-based fast-action strategy board game"),
    license = "BSD",
    keywords = "strategy board-game city-building",
    url = "http://packages.python.org/persian_silver_2",
    packages = ["src", "test"],
    long_description = read("README.md"),
    classifiers = [
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
