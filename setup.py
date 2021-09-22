#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2015-2019 by Hartmut Goebel <h.goebel@crazy-compilers.com>
#
# This file is part of unittest2pytest.
#
# unittest2pytest is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import setup
import re


def get_version(filename):
    """
    Return package version as listed in `__version__` in `filename`.
    """
    init_py = open(filename).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('unittest2pytest/__init__.py')


def read(filename):
    return open(filename, 'r', encoding='utf-8').read()


long_description = '\n\n'.join([read('README.rst'),
                                read('CHANGES.rst')])


setup(
    name="unittest2pytest",
    license='GPLv3+',
    version=version,
    description="Convert unittest test-cases to pytest",
    long_description=long_description,
    author="Hartmut Goebel",
    author_email="h.goebel@crazy-compilers.com",
    url="https://github.com/pytest-dev/unittest2pytest",
    packages=["unittest2pytest", "unittest2pytest.fixes"],
    entry_points={
        'console_scripts': [
            'unittest2pytest = unittest2pytest.__main__:main',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    zip_safe=False
)
