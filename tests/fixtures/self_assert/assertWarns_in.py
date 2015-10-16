# required-method: assertWarns

class TestWarns(TestCase):
    def test_simple(self):
        self.assertWarns(RunTimeError, someFunc)

    def test_args(self):
        self.assertWarns(RunTimeError, someFunc, 1,2,3)

    def test_kwargs(self):
        self.assertWarns(RunTimeError, someFunc, foo=42, bar=43)

    def test_args_kwargs(self):
        self.assertWarns(RunTimeError, someFunc, 1,2,3, foo=42, bar=43)
