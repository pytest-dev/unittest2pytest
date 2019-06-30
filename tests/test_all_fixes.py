#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file is part of test-suite for unittest2pytest.
"""
#
# Copyright 2015-2019 by Hartmut Goebel <h.goebel@crazy-compilers.com>
#
# This program is part of unittest2pytest.
#
# unittest2pytest free software: you can redistribute it and/or modify
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

from __future__ import unicode_literals

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2015-2019 by Hartmut Goebel"
__licence__ = "GNU General Public License version 3 or later (GPLv3+)"


import pytest


import os
from os.path import join, abspath
import re
import glob
import shutil
from difflib import unified_diff
import unittest
import logging

from lib2to3.main import main

# make logging less verbose
logging.getLogger('lib2to3.main').setLevel(logging.WARN)
logging.getLogger('RefactoringTool').setLevel(logging.WARN)

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')

def requiredTestMethod(name):
    # skip if TestCase does not have this method
    is_missing = getattr(unittest.TestCase, name, None) is None
    return pytest.mark.skipif(is_missing,
                              reason="unittest does not have TestCase.%s " % name)


def _collect_in_files_from_directory(directory):
    fixture_files = glob.glob(abspath(join(directory, '*_in.py')))
    for fixture_file in fixture_files:
        with open(fixture_file) as fh:
            text = fh.read(200)
        l = re.findall(r'^# required-method: (\S+)', text)
        method = l[0] if l else None
        yield fixture_file, method


def collect_all_test_fixtures():
    for root, dirs, files in os.walk(FIXTURE_PATH):
        # Loop recursively through all files. If the files is in a
        # subdirectory, only run the fixer of the subdirectory name, else run
        # all fixers.
        for in_file, method in _collect_in_files_from_directory(root):
            fixer_to_run = root[len(FIXTURE_PATH)+1:] or None
            marks = []
            if method:
                marks.append(requiredTestMethod(method))
            yield pytest.param(fixer_to_run, in_file, marks=marks)


def _get_id(argvalue):
    if argvalue is not None and argvalue.startswith(FIXTURE_PATH):
        return os.path.basename(argvalue).replace("_in.py", "")


@pytest.mark.parametrize("fixer, in_file",
                         collect_all_test_fixtures(), ids=_get_id)
def test_check_fixture(in_file, fixer, tmpdir):
    if fixer:
        main("unittest2pytest.fixes",
             args=['--no-diffs', '--fix', fixer, '-w', in_file,
                   '--nobackups', '--output-dir', str(tmpdir)])
    else:
        main("unittest2pytest.fixes",
             args=['--no-diffs', '--fix', 'all', '-w', in_file,
                   '--nobackups', '--output-dir', str(tmpdir)])

    result_file_name = tmpdir.join(os.path.basename(in_file))
    assert result_file_name.exists(), '%s is missing' % result_file_name
    result_file_contents = result_file_name.readlines()

    expected_file = in_file.replace("_in.py", "_out.py")
    with open(expected_file) as fh:
        expected_contents = fh.readlines()

    # ensure the expected code is actually correct and compiles
    try:
        compile(''.join(expected_contents), expected_file, 'exec')
    except Exception as e:
        pytest.fail("FATAL: %s does not compile: %s" % (expected_file, e),
                    False)

    if result_file_contents != expected_contents:
        text = "Refactured code doesn't match expected outcome\n"
        text += ''.join(unified_diff(expected_contents, result_file_contents,
                                     'expected', 'refactured result'))
        pytest.fail(text, False)
