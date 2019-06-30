# required-method: assertIsNot

class TestAssertIsNot(TestCase):
    def test_you(self):
        self.assertIsNot(abc, 'xxx')

    def test_me(self):
        self.assertIsNot(123, xxx+y)
        self.assertIsNot(456, aaa and bbb)
        self.assertIsNot(789, ccc or ddd)
        self.assertIsNot(123, True if You else False)

    def test_everybody(self):
        self.assertIsNot(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertIsNot(123+z, xxx+z, msg=error_message)
        self.assertIsNot(123, xxx+z, error_message)
