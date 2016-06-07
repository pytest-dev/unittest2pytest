# required-method: assertWarns

import pytest
class TestWarns(TestCase):
    def test_simple(self):
        with pytest.warns(RunTimeError):
            someFunc()

    def test_args(self):
        with pytest.warns(RunTimeError):
            someFunc(1,2,3)

    def test_kwargs(self):
        with pytest.warns(RunTimeError):
            someFunc(foo=42, bar=43)

    def test_args_kwargs(self):
        with pytest.warns(RunTimeError):
            someFunc(1,2,3, foo=42, bar=43)
