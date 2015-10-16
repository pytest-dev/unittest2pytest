# required-method: assertNotEqual

class TestAssertNotEqual(TestCase):
    def test_you(self):
        self.assertNotEqual(abc, 'xxx')
        self.assertNotEquals(abc, 'xxx')

    def test_me(self):
        self.assertNotEqual(123, xxx+y)

    def test_everybody(self):
        self.assertNotEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertNotEqual(123+z, xxx+z, msg=error_message)
        self.assertNotEqual(123, xxx+z, error_message)
