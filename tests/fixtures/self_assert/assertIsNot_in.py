# required-method: assertIsNot

class TestAssertIsNot(TestCase):
    def test_you(self):
        self.assertIsNot(abc, 'xxx')

    def test_me(self):
        self.assertIsNot(123, xxx+y)

    def test_everybody(self):
        self.assertIsNot(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertIsNot(123+z, xxx+z, msg=error_message)
        self.assertIsNot(123, xxx+z, error_message)
