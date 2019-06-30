# -*- coding: utf-8 -*-
"""
fix_remove_class - lib2to3 fix for removing "class Testxxx(TestCase):"
headers and dedenting the contained code.
"""
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

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2015-2019 by Hartmut Goebel"
__licence__ = "GNU General Public License version 3 or later (GPLv3+)"


from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import token, find_indentation

"""
Node(classdef, 
     [Leaf(1, 'class'), 
      Leaf(1, 'TestAssertEqual'), 
      Leaf(7, '('), 
      Leaf(1, 'TestCase'), 
      Leaf(8, ')'), 
      Leaf(11, ':'), 
      Node(suite, [
          Leaf(4, '\n'), 
          Leaf(5, '    '), 
          Node(funcdef, [
              Leaf(1, 'def'), 
              Leaf(1, 'test_you'), ...
          ]), 
          Leaf(6, '')])])
"""

class FixRemoveClass(BaseFix):

    PATTERN = """
      classdef< 'class' name=any '(' 'TestCase' ')' ':'
         suite=suite
      >
    """

    def dedent(self, suite, dedent):
        self.line_num = suite.get_lineno()
        for kid in suite.leaves():
            if kid.type in (token.INDENT, token.DEDENT):
                self.line_num = kid.get_lineno()
                # todo: handle tabs
                kid.value = kid.value[dedent:]
                self.current_indent = kid.value
            elif kid.get_lineno() != self.line_num:
                # todo: handle tabs
                if len(kid.prefix) > len(self.current_indent):
                    kid.prefix = self.current_indent
            

    def transform(self, node, results):
        suite = results['suite'].clone()
        # todo: handle tabs
        dedent = len(find_indentation(suite)) - len(find_indentation(node))
        self.dedent(suite, dedent)

        # remove the first newline behind the classdef header
        first = suite.children[0]
        if first.type == token.NEWLINE:
            if len(first.value) == 1:
                del suite.children[0]
            else:
                first.value == first.value[1:]

        return suite
