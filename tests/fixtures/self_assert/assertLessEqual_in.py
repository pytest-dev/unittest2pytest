# required-method: assertLessEqual

class TestAssertLessEqual(TestCase):
    def test_you(self):
        self.assertLessEqual(abc, 'xxx')

    def test_me(self):
        self.assertLessEqual(123, xxx+y)
        self.assertLessEqual(456, aaa and bbb)
        self.assertLessEqual(789, ccc or ddd)
        self.assertLessEqual(123, True if You else False)

    def test_everybody(self):
        self.assertLessEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertLessEqual(123+z, xxx+z, msg=error_message)
        self.assertLessEqual(123, xxx+z, error_message)
