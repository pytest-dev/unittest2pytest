# required-method: assertRaisesRegex

class TestRaises(TestCase):
    def test_simple(self):
        self.assertRaisesRegex(RunTimeError, "text .* match", someFunc)

    def test_args(self):
        self.assertRaisesRegex(RunTimeError, "text .* match", someFunc, 1,2,3)

    def test_kwargs(self):
        self.assertRaisesRegex(RunTimeError, "text .* match", someFunc, foo=42, bar=43)

    def test_context_manager(self):
        with self.assertRaisesRegex(RunTimeError, "text .* match"):
            someFunc('foo', None)

    def test_args_kwargs(self):
        self.assertRaisesRegex(RunTimeError, "text .* match", someFunc, 1,2,3, foo=42, bar=43)

    def test_lambda(self):
        self.assertRaises(RunTimeError, lambda: error(1, 2))
        self.assertRaises(RunTimeError, lambda: error(1, 2) or error())
