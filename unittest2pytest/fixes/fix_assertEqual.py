from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import (
    Comma, Name, Call, LParen, RParen, Dot, Node, Leaf,
    ArgList, String, Number, syms, is_tuple, token)

from lib2to3.pygram import python_symbols as symbols

from functools import partial
import inspect
import unittest


def CompOp(op, left, right, kws):
    op = Name(op, prefix=" ")
    #import pdb ; pdb.set_trace()
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
        # :todo: implement `assert isinstance(xx, seq_type`
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

}

"""
    'assertNotRegexpMatches': '',
    'assertRaises': '',
    'assertRaisesRegexp': '',
    'assertRegexpMatches': '',
    }
"""

# Aliases
_method_map['assertEquals'] = _method_map['assertEqual']
_method_map['assertNotEquals'] = _method_map['assertNotEqual']
_method_map['failIf'] = _method_map['assertFalse']
#_method_map['failIfAlmostEqual'] = _method_map['assertNotAlmostEqual']
_method_map['failIfEqual'] = _method_map['assertNotEqual']
_method_map['failUnless'] = _method_map['assertTrue']
#_method_map['failUnlessAlmostEqual'] = _method_map['assertAlmostEqual']
_method_map['failUnlessEqual'] = _method_map['assertEqual']
#_method_map['failUnlessRaises'] = _method_map['assertRaises']



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


class FixAssertequal(BaseFix):

    PATTERN = """
    power< 'self'
      trailer< '.' method=( %s ) >
      trailer< '(' arglist=arglist< any+ > ')' >
    >
    """ % ' | '.join(map(repr, _method_map.keys()))

    PATTERN = """
    power< 'self'
      trailer< '.' method=( %s ) >
      trailer< '(' arglist=any ')' >
    >
    """ % ' | '.join(map(repr, _method_map.keys()))

    class SelfMarker: pass

    def transform(self, node, results):

        def process_arg(arg):
            if isinstance(arg, Leaf) and arg.type == token.COMMA:
                return
            elif isinstance(arg, Node) and arg.type == syms.argument:
                # keyword argument
                #import pdb ; pdb.set_trace()
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

        posargs = [self.SelfMarker]
        kwargs = {}

        # This is either a "arglist" or a single argument
        if method == 'assertTrue':
            #print results.keys()
            pass
        #import pdb ; pdb.set_trace()
        
        
        if results['arglist'].type == syms.arglist:
            for arg in results['arglist'].children:
                process_arg(arg)
        else:
            process_arg(results['arglist'])
        #print posargs
        
        test_func = getattr(unittest.TestCase, method)
        
        args = inspect.getcallargs(test_func, *posargs, **kwargs)
        assert args['self'] == self.SelfMarker
        argspec = inspect.getargspec(test_func)
        assert argspec.varargs is None  # unhandled case
        assert argspec.keywords is None  # unhandled case

        # get the required arguments
        if argspec.defaults:
            required_args = argspec.args[1:-len(argspec.defaults)]
        else:
            required_args = argspec.args[1:]
        required_args = [args[argname] for argname in required_args]
        
        n_stmt = Node(syms.assert_stmt,
                      [Name('assert'),
                       _method_map[method](*required_args, kws=args)])
        #if method == 'assertTrue':
        #    import pdb ; pdb.set_trace()
        if args.get('msg', None) is not None:
            #import pdb ; pdb.set_trace()
            n_stmt.children.extend((Name(','), args['msg']))
        n_stmt.prefix = node.prefix
        return n_stmt
