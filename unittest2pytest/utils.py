# -*- coding: utf-8 -*-
"""
Some utility functions for unittest2pytest.
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


import inspect
try:
    from inspect import Parameter
except ImportError:
    # Python 2
    pass
from collections import OrderedDict


class SelfMarker: pass

def __apply_defaults(boundargs):
    # Backport of Python 3.5 inspect.BoundArgs.apply_defaults()
    arguments = boundargs.arguments
    if not arguments:
        return
    new_arguments = []
    for name, param in boundargs.signature.parameters.items():
        try:
            new_arguments.append((name, arguments[name]))
        except KeyError:
            if param.default is not Parameter.empty:
                val = param.default
            elif param.kind is Parameter.VAR_POSITIONAL:
                val = ()
            elif param.kind is Parameter.VAR_KEYWORD:
                val = {}
            else:
                # This BoundArguments was likely produced by
                # Signature.bind_partial().
                continue
            new_arguments.append((name, val))
    boundargs.arguments = OrderedDict(new_arguments)


def resolve_func_args(test_func, posargs, kwargs):
    try:
        inspect.signature
    except AttributeError:
        # Python 2.7
        posargs.insert(0, SelfMarker)
        args = inspect.getcallargs(test_func, *posargs, **kwargs)

        assert args['self'] == SelfMarker
        argspec = inspect.getargspec(test_func)
        #if not 'Raises' in method:
        #    assert argspec.varargs is None  # unhandled case
        #    assert argspec.keywords is None  # unhandled case

        # get the required arguments
        if argspec.defaults:
            required_args = argspec.args[1:-len(argspec.defaults)]
        else:
            required_args = argspec.args[1:]
        required_args = [args[argname] for argname in required_args]

    else:
        sig = inspect.signature(test_func)
        assert (list(iter(sig.parameters))[0] == 'self')
        posargs.insert(0, SelfMarker)
        ba = sig.bind(*posargs, **kwargs)
        try:
            ba.apply_defaults
        except AttributeError:
            # Python < 3.5
            __apply_defaults(ba)
        else:
            ba.apply_defaults()
        args = ba.arguments
        required_args = [n for n,v in sig.parameters.items()
                         if (v.default is Parameter.empty and
                             v.kind not in (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD))]
        assert args['self'] == SelfMarker
        assert required_args[0] == 'self'
        del required_args[0], args['self']
        required_args = [args[n] for n in required_args]

    return required_args, args
