# -*- coding: utf-8 -*-
"""
fix_self_assert - lib2to3 fix for replacing assertXXX() method calls
by their pytest equivalent.
"""
#
# Copyright 2015-1017 by Hartmut Goebel <h.goebel@crazy-compilers.com>
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
__copyright__ = "Copyright 2015-1017 by Hartmut Goebel"
__licence__ = "GNU General Public License version 3 or later (GPLv3+)"


from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import (
    Comma, Name, Call, Node, Leaf,
    Newline, KeywordArg, find_indentation,
    ArgList, String, Number, syms, token,
    does_tree_import, is_import, parenthesize)

from functools import partial
import re
import unittest

from .. import utils


TEMPLATE_PATTERN = re.compile('[\1\2]|[^\1\2]+')

def CompOp(op, left, right, kws):
    op = Name(op, prefix=" ")
    left = parenthesize_expression(left)
    right = parenthesize_expression(right)

    left.prefix = ""
    if '\n' not in right.prefix:
        right.prefix = " "
    return Node(syms.comparison, (left, op, right), prefix=" ")


def UnaryOp(prefix, postfix, value, kws):
    if prefix or postfix:
        value = parenthesize_expression(value)

    kids = []
    if prefix:
        kids.append(Name(prefix, prefix=" "))
    value.prefix = " "
    kids.append(value)
    if postfix:
        kids.append(Name(postfix, prefix=" "))
    return Node(syms.test, kids, prefix=" ")


def parenthesize_expression(value):
    if value.type in [syms.comparison, syms.not_test]:
        parenthesized = parenthesize(value.clone())
        parenthesized.prefix = parenthesized.children[1].prefix
        parenthesized.children[1].prefix = ''
        value = parenthesized
    return value


def fill_template(template, *args):
    parts = TEMPLATE_PATTERN.findall(template)
    kids = []
    for p in parts:
        if p == '':
            continue
        elif p in '\1\2\3\4\5':
            p = args[ord(p)-1]
            p.prefix = ''
        else:
            p = Name(p)
        kids.append(p.clone())
    return kids

def DualOp(template, first, second, kws):
    kids = fill_template(template, first, second)
    return Node(syms.test, kids, prefix=" ")


def SequenceEqual(left, right, kws):
    if 'seq_type' in kws:
        # :todo: implement `assert isinstance(xx, seq_type)`
        pass
    return CompOp('==', left, right, kws)


def AlmostOp(places_op, delta_op, first, second, kws):
    first.prefix =  ""
    second.prefix = ""
    abs_op = Call(Name('abs'),
                  [Node(syms.factor, [first, Name('-'), second])])
    if kws.get('delta', None) is not None:
        # delta
        return CompOp(delta_op, abs_op, kws['delta'], {})
    else:
        # `7` is the default in unittest.TestCase.asserAlmostEqual
        places = kws['places'] or Number(7)
        places.prefix = " "
        round_op = Call(Name('round'), (abs_op, Comma(), places))
        return CompOp(places_op, round_op, Number(0), {})


def RaisesOp(context, exceptionClass, indent, kws, arglist, node):
    exceptionClass.prefix = ""
    args = [exceptionClass]
    # Add match keyword arg to with statement if an expected regex was provided.
    # In py27 the keyword is `expected_regexp`, in py3 is `expected_regex`
    if 'expected_regex' in kws or 'expected_regexp' in kws:
        expected_regex = kws.get('expected_regex', kws.get('expected_regexp')).clone()
        expected_regex.prefix = ''
        args.append(String(', '))
        args.append(
            KeywordArg(Name('match'), expected_regex))
    with_item = Call(Name(context), args)
    with_item.prefix = " "
    args = []
    arglist = [a.clone() for a in arglist.children[4:]]
    if arglist:
        arglist[0].prefix=""

    func = None

    # :fixme: this uses hardcoded parameter names, which may change
    if 'callableObj' in kws:
        func = kws['callableObj']
    elif 'callable_obj' in kws:
        func = kws['callable_obj']
    elif kws['args']:  # any arguments assigned to `*args`
        func = kws['args'][0]
    else:
        func = None

    if func is None:
        # Context manager
        return Node(syms.with_stmt, [with_item])

    if func.type == syms.lambdef:
        suite = func.children[-1].clone()
    else:
        # TODO: Newlines within arguments are not handled yet.
        # If argment prefix contains a newline, all whitespace around this
        # ought to be replaced by indent plus 4+1+len(func) spaces.
        suite = Call(func, arglist)

    suite.prefix = indent + (4 * " ")
    return Node(syms.with_stmt,
                [Name('with'),
                 with_item,
                 Name(':'),
                 Newline(),
                 suite])

def RaisesRegexOp(context, designator, exceptionClass, expected_regex,
                  indent, kws, arglist, node):
    arglist = [a.clone() for a in arglist.children]
    pattern = arglist[2]
    del arglist[2:4] # remove pattern and comma
    arglist = Node(syms.arglist, arglist)
    with_stmt = RaisesOp(context, exceptionClass, indent, kws, arglist, node)

    # if this is already part of a with statement we need to insert re.search
    # after the last leaf with content
    if node.parent.type == syms.with_stmt:
        parent_with = node.parent
        for leaf in reversed(list(parent_with.leaves())):
            if leaf.value.strip():
                break
        i = leaf.parent.children.index(leaf)
        return with_stmt
    else:
        return Node(syms.suite, [with_stmt])


def add_import(import_name, node):
    suite = get_parent_of_type(node, syms.suite)
    test_case = suite
    while test_case.parent.type != syms.file_input:
        test_case = test_case.parent
    file_input = test_case.parent

    if not does_tree_import(None, import_name, node):
        import_stmt = Node(syms.simple_stmt,
                           [Node(syms.import_name, [Name('import'), Name(import_name, prefix=' ')]),
                            Newline(),
                            ])
        insert_import(import_stmt, test_case, file_input)


def get_parent_of_type(node, node_type):
    while node:
        if node.type == node_type:
            return node
        node = node.parent


def insert_import(import_stmt, test_case, file_input):
    """This inserts an import in a very similar way as
    lib2to3.fixer_util.touch_import, but try to maintain encoding and shebang
    prefixes on top of the file when there is no import"""
    import_nodes = get_import_nodes(file_input)
    if import_nodes:
        last_import_stmt = import_nodes[-1].parent
        i = file_input.children.index(last_import_stmt) + 1
    # no import found, so add right before the test case
    else:
        i = file_input.children.index(test_case)
        import_stmt.prefix = test_case.prefix
        test_case.prefix = ''
    file_input.insert_child(i, import_stmt)


def get_import_nodes(node):
    return [
        x for c in node.children
        for x in c.children
        if c.type == syms.simple_stmt
        and is_import(x)
    ]


_method_map = {
    # simple ones
    'assertEqual':         partial(CompOp, '=='),
    'assertNotEqual':      partial(CompOp, '!='),
    'assertFalse':         partial(UnaryOp, 'not', ''),
    'assertGreater':       partial(CompOp, '>'),
    'assertGreaterEqual':  partial(CompOp, '>='),
    'assertIn':            partial(CompOp, 'in'),
    'assertIs':            partial(CompOp, 'is'),
    'assertIsInstance':    partial(DualOp, 'isinstance(\1, \2)'),
    'assertIsNone':        partial(UnaryOp, '', 'is None'),
    'assertIsNot':         partial(CompOp, 'is not'),
    'assertIsNotNone':     partial(UnaryOp, '', 'is not None'),
    'assertLess':          partial(CompOp, '<'),
    'assertLessEqual':     partial(CompOp, '<='),
    'assertNotIn':         partial(CompOp, 'not in'),
    'assertNotIsInstance': partial(DualOp, 'not isinstance(\1, \2)'),
    'assertTrue':          partial(UnaryOp, '', ''),

    # types ones
    'assertDictEqual':      partial(CompOp, '=='),
    'assertListEqual':      partial(CompOp, '=='),
    'assertMultiLineEqual': partial(CompOp, '=='),
    'assertSetEqual':       partial(CompOp, '=='),
    'assertTupleEqual':     partial(CompOp, '=='),
    'assertSequenceEqual':  SequenceEqual,

    'assertDictContainsSubset': partial(DualOp, 'dict(\2, **\1) == \2'),
    # :todo:
    #'assertItemsEqual': '', # unordered sequence specific comparison.

    'assertAlmostEqual':    partial(AlmostOp, "==", "<"),
    'assertNotAlmostEqual': partial(AlmostOp, "!=", ">"),

    'assertRaises':         partial(RaisesOp, 'pytest.raises'),
    'assertWarns':          partial(RaisesOp, 'pytest.warns'), # new Py 3.2

    'assertRegex':          partial(DualOp, 're.search(\2, \1)'),
    'assertNotRegex':       partial(DualOp, 'not re.search(\2, \1)'), # new Py 3.2

    'assertRaisesRegex':    partial(RaisesRegexOp, 'pytest.raises', 'excinfo'),
    'assertWarnsRegex':     partial(RaisesRegexOp, 'pytest.warns', 'record'),

    #'assertLogs': -- not to be handled here, is an context handler only
}

for newname, oldname in (
        ('assertRaisesRegex', 'assertRaisesRegexp'),
        ('assertRegex', 'assertRegexpMatches'),
):
    if not hasattr(unittest.TestCase, newname):
        # use old name
        _method_map[oldname] = _method_map[newname]
        del _method_map[newname]

for m in list(_method_map.keys()):
    if not hasattr(unittest.TestCase, m):
        del _method_map[m]


# (Deprecated) Aliases
_method_aliases = {
    'assertEquals'         : 'assertEqual',
    'assertNotEquals'      : 'assertNotEqual',
    'assert_'              : 'assertTrue',
    'assertAlmostEquals'   : 'assertAlmostEqual',
    'assertNotAlmostEquals': 'assertNotAlmostEqual',
    'assertRegexpMatches'  : 'assertRegex',
    'assertRaisesRegexp'   : 'assertRaisesRegex',

    'failUnlessEqual'      : 'assertEqual',
    'failIfEqual'          : 'assertNotEqual',
    'failUnless'           : 'assertTrue',
    'failIf'               : 'assertFalse',
    'failUnlessRaises'     : 'assertRaises',
    'failUnlessAlmostEqual': 'assertAlmostEqual',
    'failIfAlmostEqual'    : 'assertNotAlmostEqual',
}

for a, o in list(_method_aliases.items()):
    if not o in _method_map:
        # if the original name is not a TestCase method, remove the alias
        del _method_aliases[a]


"""
Node(power,
     [Leaf(1, u'self'),
      Node(trailer,
           [Leaf(23, u'.'),
            Leaf(1, u'assertEqual')]),
      Node(trailer,
           [Leaf(7, u'('),
            Node(arglist,
                 [Leaf(1, u'abc'),
                  Leaf(12, u','),
                  Leaf(3, u"'xxx'")]),
            Leaf(8, u')')])])

Node(power,
     [Leaf(1, u'self'),
      Node(trailer,
           [Leaf(23, u'.'),
            Leaf(1, u'assertAlmostEqual')]),
      Node(trailer,
           [Leaf(7, u'('),
            Node(arglist,
                 [Leaf(2, u'100'),
                  Leaf(12, u','),
                  Leaf(1, u'klm'),
                  Leaf(12, u','),
                Node(argument,
                     [Leaf(1, u'msg'),
                      Leaf(22, u'='),
                      Leaf(3, u'"Message"')]),
                  Leaf(12, u','),
                  Node(argument,
                       [Leaf(1, u'places'),
                        Leaf(22, u'='),
                        Leaf(2, u'1')])]),
            Leaf(8, u')')])])
"""


class FixSelfAssert(BaseFix):

    PATTERN = """
    power< 'self'
      trailer< '.' method=( %s ) >
      trailer< '(' arglist=any ')' >
    >
    """ % ' | '.join(map(repr,
                         (set(_method_map.keys()) | set(_method_aliases.keys()))))

    def transform(self, node, results):

        def process_arg(arg):
            if isinstance(arg, Leaf) and arg.type == token.COMMA:
                return
            elif (isinstance(arg, Node) and arg.type == syms.argument and
                  arg.children[1].type == token.EQUAL):
                # keyword argument
                name, equal, value = arg.children
                assert name.type == token.NAME
                assert equal.type == token.EQUAL
                value = value.clone()
                kwargs[name.value] = value
                if '\n' in arg.prefix:
                    value.prefix = arg.prefix
                else:
                    value.prefix = arg.prefix.strip() + " "
            else:
                if (isinstance(arg, Node) and arg.type == syms.argument and
                    arg.children[0].type == 36 and arg.children[0].value == '**'):
                    return
                assert not kwargs, 'all positional args are assumed to come first'
                if (isinstance(arg, Node) and arg.type == syms.argument and
                    arg.children[1].type == syms.comp_for):
                    # argument is a generator expression w/o
                    # parenthesis, add parenthesis
                    value = arg.clone()
                    value.children.insert(0, Leaf(token.LPAR, '('))
                    value.children.append(Leaf(token.RPAR, ')'))
                    posargs.append(value)
                else:
                    posargs.append(arg.clone())

        method = results['method'][0].value
        # map (deprecated) aliases to original to avoid analysing
        # the decorator function
        method = _method_aliases.get(method, method)

        posargs = []
        kwargs = {}

        # This is either a "arglist" or a single argument
        if results['arglist'].type == syms.arglist:
            for arg in results['arglist'].children:
                process_arg(arg)
        else:
            process_arg(results['arglist'])

        try:
            test_func = getattr(unittest.TestCase, method)
        except AttributeError:
            raise RuntimeError("Your unittest package does not support '%s'. "
                               "consider updating the package" % method)

        required_args, argsdict = utils.resolve_func_args(test_func, posargs, kwargs)

        if method.startswith(('assertRaises', 'assertWarns')):
            n_stmt = _method_map[method](*required_args,
                                         indent=find_indentation(node),
                                         kws=argsdict,
                                         arglist=results['arglist'],
                                         node=node)
        else:
            n_stmt = Node(syms.assert_stmt,
                          [Name('assert'),
                           _method_map[method](*required_args, kws=argsdict)])
        if argsdict.get('msg', None) is not None:
            n_stmt.children.extend((Name(','), argsdict['msg']))

        def fix_line_wrapping(x):
            for c in x.children:
                # no need to worry about wrapping of "[", "{" and "("
                if c.type in [token.LSQB, token.LBRACE, token.LPAR]:
                    break
                if c.prefix.startswith('\n'):
                    c.prefix = c.prefix.replace('\n', ' \\\n')
                fix_line_wrapping(c)
        fix_line_wrapping(n_stmt)
        # the prefix should be set only after fixing line wrapping because it can contain a '\n'
        n_stmt.prefix = node.prefix

        # add necessary imports
        if 'Raises' in method or 'Warns' in method:
            add_import('pytest', node)
        if ('Regex' in method and not 'Raises' in method and
                not 'Warns' in method):
            add_import('re', node)

        return n_stmt
