# required-method: assertIsInstance

class TestAssertIsInstance(TestCase):
    def test_you(self):
        self.assertIsInstance(abc, 'xxx')

    def test_me(self):
        self.assertIsInstance(123, xxx+y)
        self.assertIsInstance(456, aaa and bbb)
        self.assertIsInstance(789, ccc or ddd)
        self.assertIsInstance(123, True if You else False)

    def test_everybody(self):
        self.assertIsInstance(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertIsInstance(123+z, xxx+z, msg='This is wrong!')
        self.assertIsInstance(123, xxx+z, 'This is wrong!')
