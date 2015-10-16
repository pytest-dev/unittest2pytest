# required-method: assertIn

class TestAssertIn(TestCase):
    def test_you(self):
        self.assertIn(abc, 'xxx')

    def test_me(self):
        self.assertIn(123, xxx+y)

    def test_everybody(self):
        self.assertIn(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertIn(123, xxx+z, 'This is wrong!')
        self.assertIn(123+z, xxx+z, msg='This is wrong!')
