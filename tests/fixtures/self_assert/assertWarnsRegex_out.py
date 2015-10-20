# required-method: assertWarnsRegex

class TestWarns(TestCase):
    def test_simple(self):
        with pytest.warns(RunTimeError) as record:
            someFunc()
        assert re.search(pattern, record.value)

    def test_args(self):
        with pytest.warns(RunTimeError) as record:
            someFunc(1,2,3)
        assert re.search(pattern, record.value)

    def test_kwargs(self):
        with pytest.warns(RunTimeError) as record:
            someFunc(foo=42, bar=43)
        assert re.search(pattern, record.value)

    def test_args_kwargs(self):
        with pytest.warns(RunTimeError) as record:
            someFunc(1,2,3, foo=42, bar=43)
        assert re.search(pattern, record.value)
