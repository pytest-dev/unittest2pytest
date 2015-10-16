# required-method: assertIsInstance

class TestAssertIsInstance(TestCase):
    def test_you(self):
        self.assertIsInstance(abc, 'xxx')

    def test_me(self):
        self.assertIsInstance(123, xxx+y)

    def test_everybody(self):
        self.assertIsInstance(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertIsInstance(123+z, xxx+z, msg='This is wrong!')
        self.assertIsInstance(123, xxx+z, 'This is wrong!')
