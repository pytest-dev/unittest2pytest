# required-method: assertRaisesRegexp

import pytest
class TestRaises(TestCase):
    def test_simple(self):
        with pytest.raises(RunTimeError, match="text .* match"):
            someFunc()

    def test_simple_with_newlines(self):
        with pytest.raises(RunTimeError, match="text .* match"):
            someFunc()

    def test_args(self):
        with pytest.raises(RunTimeError, match="text .* match"):
            someFunc(1,2,3)

    def test_kwargs(self):
        with pytest.raises(RunTimeError, match="text .* match"):
            someFunc(foo=42, bar=43)

    def test_context_manager(self):
        with pytest.raises(RunTimeError, match="text .* match"):
            someFunc('foo', None)

    def test_args_kwargs(self):
        with pytest.raises(RunTimeError, match="text .* match"):
            someFunc(1,2,3, foo=42, bar=43)

    def test_args_kwargs_with_newlines(self):
        # TODO: Newlines within arguments are not handled yet.
        with pytest.raises(RunTimeError, match="text .* match"):
            someFunc(1,
            2,3,
            foo=42,
            bar=43)

    def test_lambda(self):
        with pytest.raises(RunTimeError):
            error(1, 2)
        with pytest.raises(RunTimeError):
            error(1, 2) or error()

    def test_atom(self):
        with pytest.raises(RunTimeError, match=("foo" "bar")):
            someFunc(1,2,3)

    def test_expr(self):
        with pytest.raises(RunTimeError, match="foo" + "bar"):
            someFunc(1,2,3)
