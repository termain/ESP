#taken almost directly from http://packages.python.org/an_example_pypi_project/setuptools.html#setting-up-setup-py

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ESP",
    version = "0.1.0",
    author = "Nathan Alday",
    author_email = "n.c.alday@gmail.com",
    description = ("A Modeling and simulation package."),
    license = "GPL3",
    keywords = "modeling simulation education engineering",
    url = "http://github.com/termain/esp",
    packages=['esp'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Simulation",
        "License :: OSI Approved :: GPL3 License",
    ],
)
