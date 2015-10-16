# -*- coding: utf-8 -*-
"""
fix_remote_class - lib2to3 fix for replacing assertXXX() method calls
by their pytest equivalent.
"""
#
# Copyright 2015 by Hartmut Goebel <h.goebel@crazy-compilers.com>
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
__copyright__ = "Copyright 2015 by Hartmut Goebel"
__licence__ = "GNU General Public License version 3 ot later (GPLv3+)"


from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import (
    Comma, Name, Call, Node, Leaf,
    Newline, KeywordArg, find_indentation,
    ArgList, String, Number, syms, token)

from functools import partial
import unittest

from .. import utils


def CompOp(op, left, right, kws):
    op = Name(op, prefix=" ")
    left.prefix = ""
    right.prefix = " "
    return Node(syms.comparison, (left, op, right), prefix=" ")


def UnaryOp(prefix, postfix, value, kws):
    kids = []
    if prefix:
        kids.append(Name(prefix, prefix=" "))
    value.prefix = " "
    kids.append(value)
    if postfix:
        kids.append(Name(postfix, prefix=" "))
    return Node(syms.test, kids, prefix=" ")


def DualOp(template, first, second, kws):
    prefix, separator, postfix = template.split('\0')
    kids = []
    if prefix:
        kids.append(Name(prefix, prefix=" "))
    first.prefix = ''
    kids.append(first)
    if separator:
        kids.append(Name(separator))
    second.prefix = ''
    kids.append(second)
    if postfix:
        kids.append(Name(postfix))
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


def RaisesOp(context, exceptionClass, indent, kws, arglist):
    with_item = Call(Name(context), [exceptionClass])
    with_item.prefix = " "
    args = []
    arglist = [a.clone() for a in arglist.children[4:]]
    if arglist:
        arglist[0].prefix=""
    # :fixme: this uses hardcoded parameter names, which may change
    if 'callableObj' in kws:
        suite = Call(kws['callableObj'], arglist)
    elif 'callable_obj' in kws:
        suite = Call(kws['callable_obj'], arglist)
    elif kws['args']: # any arguments assigned to `*args`
        suite = Call(kws['args'][0], arglist)
    else:
        raise NotImplementedError('with %s is not implemented' % context)
    suite.prefix = indent + (4 * " ")
    return Node(syms.with_stmt,
                [Name('with'),
                 with_item,
                 Name(':'),
                 Newline(),
                 suite])


_method_map = {
    # simple ones
    'assertEqual':         partial(CompOp, '=='),
    'assertNotEqual':      partial(CompOp, '!='),
    'assertFalse':         partial(UnaryOp, 'not', ''),
    'assertGreater':       partial(CompOp, '>'),
    'assertGreaterEqual':  partial(CompOp, '>='),
    'assertIn':            partial(CompOp, 'in'),
    'assertIs':            partial(CompOp, 'is'),
    'assertIsInstance':    partial(DualOp, 'isinstance(\0, \0)'),
    'assertIsNone':        partial(UnaryOp, '', 'is None'),
    'assertIsNot':         partial(CompOp, 'is not'),
    'assertIsNotNone':     partial(UnaryOp, '', 'is not None'),
    'assertLess':          partial(CompOp, '<'),
    'assertLessEqual':     partial(CompOp, '<='),
    'assertNotIn':         partial(CompOp, 'not in'),
    'assertNotIsInstance': partial(DualOp, 'not isinstance(\0, \0)'),
    'assertTrue':          partial(UnaryOp, '', ''),

    # types ones
    'assertDictEqual':      partial(CompOp, '=='),
    'assertListEqual':      partial(CompOp, '=='),
    'assertMultiLineEqual': partial(CompOp, '=='),
    'assertSetEqual':       partial(CompOp, '=='),
    'assertTupleEqual':     partial(CompOp, '=='),
    'assertSequenceEqual':  SequenceEqual,

    # :todo:
    #'assertDictContainsSubset': '',
    #'assertItemsEqual': '', # unordered sequence specific comparison.

    'assertAlmostEqual':    partial(AlmostOp, "==", "<"),
    'assertNotAlmostEqual': partial(AlmostOp, "!=", ">"),

    'assertRaises':         partial(RaisesOp, 'pytest.raises'),

    # new in Python 3.2
    'assertWarns':          partial(RaisesOp, 'pytest.warns'),

    'assertRaisesRegex':   NotImplementedError,
    'assertRegex':   NotImplementedError,
    #'assertWarnsRegex':    're.match(\2, \1)' # new name, py >= 3.2
    #'assertLogs':
}


for newname, oldname in (
        ('assertRaisesRegex', 'assertRaisesRegexp'),
        ('assertRegex', 'assertRegexpMatches'),
):
    if not hasattr(unittest.TestCase, newname):
        # use old name
        _method_map[oldname] = _method_map[newname]
        del _method_map[oldname]


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
            elif isinstance(arg, Node) and arg.type == syms.argument:
                # keyword argument
                name, equal, value = arg.children
                assert name.type == token.NAME # what is the symbol for 1?
                assert equal.type == token.EQUAL # what is the symbol for 1?
                value = value.clone()
                value.prefix = " "
                kwargs[name.value] = value
            else:
                assert not kwargs, 'all positional args are assumed to come first'
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

        if method in ('assertRaises', 'assertWarns'):
            n_stmt = _method_map[method](*required_args,
                                         indent=find_indentation(node),
                                         kws=argsdict,
                                         arglist=results['arglist'])
        else:
            n_stmt = Node(syms.assert_stmt,
                          [Name('assert'),
                           _method_map[method](*required_args, kws=argsdict)])
        if argsdict.get('msg', None) is not None:
            n_stmt.children.extend((Name(','), argsdict['msg']))
        n_stmt.prefix = node.prefix
        return n_stmt
