# -*- coding: utf-8 -*-
"""
Some utility functions for unittest2pytest.
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


import inspect
from inspect import Parameter


class SelfMarker: pass


def resolve_func_args(test_func, posargs, kwargs):
    sig = inspect.signature(test_func)
    assert (list(iter(sig.parameters))[0] == 'self')
    posargs.insert(0, SelfMarker)
    ba = sig.bind(*posargs, **kwargs)
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
