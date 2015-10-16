# required-method: assertGreaterEqual

class TestAssertGreaterEqual(TestCase):
    def test_you(self):
        self.assertGreaterEqual(abc, 'xxx')

    def test_me(self):
        self.assertGreaterEqual(123, xxx+y)

    def test_everybody(self):
        self.assertGreaterEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertGreaterEqual(123+z, xxx+z, msg=error_message)
        self.assertGreaterEqual(123, xxx+z, error_message)
