# required-method: assertGreaterEqual

class TestAssertGreaterEqual(TestCase):
    def test_you(self):
        self.assertGreaterEqual(abc, 'xxx')

    def test_me(self):
        self.assertGreaterEqual(123, xxx+y)
        self.assertGreaterEqual(456, aaa and bbb)
        self.assertGreaterEqual(789, ccc or ddd)
        self.assertGreaterEqual(123, True if You else False)

    def test_everybody(self):
        self.assertGreaterEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertGreaterEqual(123+z, xxx+z, msg=error_message)
        self.assertGreaterEqual(123, xxx+z, error_message)
