# required-method: assertIs

class TestAssertIs(TestCase):
    def test_you(self):
        self.assertIs(abc, 'xxx')

    def test_me(self):
        self.assertIs(123, xxx+y)
        self.assertIs(456, aaa and bbb)
        self.assertIs(789, ccc or ddd)
        self.assertIs(123, True if You else False)

    def test_everybody(self):
        self.assertIs(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertIs(123+z, xxx+z, msg='This is wrong!')
        self.assertIs(123, xxx+z, 'This is wrong!')
