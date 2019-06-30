# required-method: assertLess

class TestAssertLess(TestCase):
    def test_you(self):
        self.assertLess(abc, 'xxx')

    def test_me(self):
        self.assertLess(123, xxx+y)
        self.assertLess(456, aaa and bbb)
        self.assertLess(789, ccc or ddd)
        self.assertLess(123, True if You else False)

    def test_everybody(self):
        self.assertLess(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertLess(123+z, xxx+z, msg='This is wrong!')
        self.assertLess(123, xxx+z, 'This is wrong!')
