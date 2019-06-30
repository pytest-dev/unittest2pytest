# required-method: assertRaises
import os
from os import listdir, path
import subprocess as sb
import pytest

class Dummy():
    pass

class TestRaises(TestCase):
    def test_simple(self):
        import io
        from io import StringIO, BytesIO
        import numpy as np
        with pytest.raises(RunTimeError):
            someFunc()

    def test_simple_with_newlines(self):
        with pytest.raises(RunTimeError):
            someFunc()

    def test_args(self):
        with pytest.raises(RunTimeError):
            someFunc(1,2,3)

    def test_kwargs(self):
        with pytest.raises(RunTimeError):
            someFunc(foo=42, bar=43)

    def test_args_kwargs(self):
        with pytest.raises(RunTimeError):
            someFunc(1,2,3, foo=42, bar=43)

    def test_args_kwargs_with_newlines(self):
        # TODO: Newlines within arguments are not handled yet.
        with pytest.raises(RunTimeError):
            someFunc(1,2,
                          3,
                          foo=42,
                          bar=43)

    def test_context_manager(self):
        with pytest.raises(RunTimeError):
            someFunc()

    def test_context_manager_var(self):
        with pytest.raises(RunTimeError) as ctx:
            someFunc()
        assert ctx.exception

    def test_lambda(self):
        with pytest.raises(RunTimeError):
            error(1, 2)
        with pytest.raises(RunTimeError):
            error(1, 2) or error()

    def test_kwargs(self):
        kwargs = {}
        with pytest.raises(RunTimeError):
            someFunc(**kwargs)
