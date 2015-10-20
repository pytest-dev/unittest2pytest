# required-method: assertRaisesRegex

class TestRaises(TestCase):
    def test_simple(self):
        self.assertRaisesRegex(RunTimeError, pattern, someFunc)

    def test_args(self):
        self.assertRaisesRegex(RunTimeError, pattern, someFunc, 1,2,3)

    def test_kwargs(self):
        self.assertRaisesRegex(RunTimeError, pattern, someFunc, foo=42, bar=43)

    def test_args_kwargs(self):
        self.assertRaisesRegex(RunTimeError, pattern, someFunc, 1,2,3, foo=42, bar=43)
