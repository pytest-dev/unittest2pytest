# required-method: assertNotEqual

class TestAssertNotEqual(TestCase):
    def test_you(self):
        self.assertNotEqual(abc, 'xxx')
        self.assertNotEquals(abc, 'xxx')

    def test_me(self):
        self.assertNotEqual(123, xxx+y)
        self.assertNotEqual(456, aaa and bbb)
        self.assertNotEqual(789, ccc or ddd)
        self.assertNotEqual(123, True if You else False)

    def test_everybody(self):
        self.assertNotEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertNotEqual(123+z, xxx+z, msg=error_message)
        self.assertNotEqual(123, xxx+z, error_message)
