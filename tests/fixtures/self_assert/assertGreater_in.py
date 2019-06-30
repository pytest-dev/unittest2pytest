# required-method: assertGreater

class TestAssertGreater(TestCase):
    def test_you(self):
        self.assertGreater(abc, 'xxx')

    def test_me(self):
        self.assertGreater(123, xxx+y)
        self.assertGreater(456, aaa and bbb)
        self.assertGreater(789, ccc or ddd)
        self.assertGreater(123, True if You else False)

    def test_everybody(self):
        self.assertGreater(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertGreater(123+z, xxx+z, msg='This is wrong!')
        self.assertGreater(123, xxx+z, 'This is wrong!')
