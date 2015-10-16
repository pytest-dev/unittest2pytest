# required-method: assertLessEqual

class TestAssertLessEqual(TestCase):
    def test_you(self):
        self.assertLessEqual(abc, 'xxx')

    def test_me(self):
        self.assertLessEqual(123, xxx+y)

    def test_everybody(self):
        self.assertLessEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertLessEqual(123+z, xxx+z, msg=error_message)
        self.assertLessEqual(123, xxx+z, error_message)
