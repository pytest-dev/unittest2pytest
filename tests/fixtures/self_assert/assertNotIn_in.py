# required-method: assertNotIn

class TestAssertNotIn(TestCase):
    def test_you(self):
        self.assertNotIn(abc, 'xxx')

    def test_me(self):
        self.assertNotIn(123, xxx+y)

    def test_everybody(self):
        self.assertNotIn(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertNotIn(123+z, xxx+z, msg=error_message)
        self.assertNotIn(123, xxx+z, error_message)
