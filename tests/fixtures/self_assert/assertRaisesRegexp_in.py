# required-method: assertRaisesRegexp

class TestRaises(TestCase):
    def test_simple(self):
        self.assertRaisesRegexp(RunTimeError, pattern, someFunc)

    def test_args(self):
        self.assertRaisesRegexp(RunTimeError, pattern, someFunc, 1,2,3)

    def test_kwargs(self):
        self.assertRaisesRegexp(RunTimeError, pattern, someFunc, foo=42, bar=43)

    def test_context_manager(self):
        with self.assertRaisesRegexp(RunTimeError, pattern):
            someFunc('foo', None)

    def test_args_kwargs(self):
        self.assertRaisesRegexp(RunTimeError, pattern, someFunc, 1,2,3, foo=42, bar=43)

    def test_lambda(self):
        self.assertRaises(RunTimeError, lambda: error(1, 2))
        self.assertRaises(RunTimeError, lambda: error(1, 2) or error())
