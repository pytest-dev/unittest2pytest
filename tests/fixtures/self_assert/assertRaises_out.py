# required-method: assertRaises

class TestRaises(TestCase):
    def test_simple(self):
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
