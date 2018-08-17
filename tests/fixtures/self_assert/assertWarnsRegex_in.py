# required-method: assertWarnsRegex

class TestWarns(TestCase):
    def test_simple(self):
        self.assertWarnsRegex(RunTimeError, pattern, someFunc)

    def test_args(self):
        self.assertWarnsRegex(RunTimeError, pattern, someFunc, 1,2,3)

    def test_kwargs(self):
        self.assertWarnsRegex(RunTimeError, pattern, someFunc, foo=42, bar=43)

    def test_args_kwargs(self):
        self.assertWarnsRegex(RunTimeError, pattern, someFunc, 1,2,3, foo=42, bar=43)

    def test_context_manager(self):
        with self.assertWarnsRegex(RunTimeError, pattern):
            someFunc(1, 2, 3)
