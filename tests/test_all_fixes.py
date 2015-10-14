#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest


import os
from os.path import join, abspath
import shutil
from difflib import unified_diff

from lib2to3.main import main

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


def _collect_in_files_from_directory(directory):
    fixture_files = os.listdir(directory)
    return (abspath(join(directory, fixture_file))
            for fixture_file in fixture_files
            if fixture_file.endswith("_in.py"))


def collect_all_test_fixtures():
    for root, dirs, files in os.walk(FIXTURE_PATH):
        # Loop recursively through all files. If the files is in a
        # subdirectory, only run the fixer of the subdirectory name, else run
        # all fixers.
        for in_file in _collect_in_files_from_directory(root):
            fixer_to_run = root[len(FIXTURE_PATH)+1:] or None
            yield (in_file, fixer_to_run)

def _get_id(argvalue):
    return os.path.basename(argvalue).replace("_in.py", "")


@pytest.mark.parametrize("in_file, fixer",
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

    if result_file_contents != expected_contents:
        text = "in_file doesn't match out_file\n"
        text += ''.join(unified_diff(expected_contents, result_file_contents,
                                     'expected', 'refactured result'))
        raise AssertionError(text)
