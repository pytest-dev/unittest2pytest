# required-method: assertRaisesRegex

class TestRaises(TestCase):
    def test_simple(self):
        self.assertRaisesRegex(RunTimeError, "text .* match", someFunc)

    def test_simple_with_newlines(self):
        self.assertRaisesRegex(
            RunTimeError,
            "text .* match",
            someFunc)

    def test_args(self):
        self.assertRaisesRegex(RunTimeError, "text .* match", someFunc, 1,2,3)

    def test_kwargs(self):
        self.assertRaisesRegex(RunTimeError, "text .* match", someFunc, foo=42, bar=43)

    def test_context_manager(self):
        with self.assertRaisesRegex(RunTimeError, "text .* match"):
            someFunc('foo', None)

    def test_args_kwargs(self):
        self.assertRaisesRegex(RunTimeError, "text .* match", someFunc, 1,2,3, foo=42, bar=43)

    def test_args_kwargs_with_newlines(self):
        # TODO: Newlines within arguments are not handled yet.
        self.assertRaisesRegex(
            RunTimeError,
            "text .* match",
            someFunc, 1,
            2,3,
            foo=42,
            bar=43)

    def test_lambda(self):
        self.assertRaises(RunTimeError, lambda: error(1, 2))
        self.assertRaises(RunTimeError, lambda: error(1, 2) or error())

    def test_atom(self):
        self.assertRaisesRegex(RunTimeError, ("foo" "bar"), someFunc, 1,2,3)

    def test_expr(self):
        self.assertRaisesRegex(RunTimeError, "foo" + "bar", someFunc, 1,2,3)
