# required-method: assertRaises

class TestRaises(TestCase):
    def test_simple(self):
        self.assertRaises(RunTimeError, someFunc)

    def test_args(self):
        self.assertRaises(RunTimeError, someFunc, 1,2,3)

    def test_kwargs(self):
        self.assertRaises(RunTimeError, someFunc, foo=42, bar=43)

    def test_args_kwargs(self):
        self.assertRaises(RunTimeError, someFunc, 1,2,3, foo=42, bar=43)

    def test_context_manager(self):
        with self.assertRaises(RunTimeError):
            someFunc()

    def test_context_manager_var(self):
        with self.assertRaises(RunTimeError) as ctx:
            someFunc()
        assert ctx.exception

    def test_lambda(self):
        self.assertRaises(RunTimeError, lambda: error(1, 2))
        self.assertRaises(RunTimeError, lambda: error(1, 2) or error())
