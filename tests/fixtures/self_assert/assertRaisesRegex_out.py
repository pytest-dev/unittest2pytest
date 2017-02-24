# required-method: assertRaisesRegex

import pytest
import re
class TestRaises(TestCase):
    def test_simple(self):
        with pytest.raises(RunTimeError) as excinfo:
            someFunc()
        assert re.search("text .* match", excinfo.value)

    def test_args(self):
        with pytest.raises(RunTimeError) as excinfo:
            someFunc(1,2,3)
        assert re.search("text .* match", excinfo.value)

    def test_kwargs(self):
        with pytest.raises(RunTimeError) as excinfo:
            someFunc(foo=42, bar=43)
        assert re.search("text .* match", excinfo.value)

    def test_context_manager(self):
        with pytest.raises(RunTimeError) as excinfo:
            someFunc('foo', None)
        assert re.search("text .* match", excinfo.value)

    def test_args_kwargs(self):
        with pytest.raises(RunTimeError) as excinfo:
            someFunc(1,2,3, foo=42, bar=43)
        assert re.search("text .* match", excinfo.value)

    def test_lambda(self):
        with pytest.raises(RunTimeError):
            error(1, 2)
        with pytest.raises(RunTimeError):
            error(1, 2) or error()
