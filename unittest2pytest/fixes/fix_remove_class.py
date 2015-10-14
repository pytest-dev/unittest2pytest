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
