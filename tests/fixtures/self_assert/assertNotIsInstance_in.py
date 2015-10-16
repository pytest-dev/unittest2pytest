# required-method: assertNotIsInstance

class TestAssertNotIsInstance(TestCase):
    def test_you(self):
        self.assertNotIsInstance(abc, 'xxx')

    def test_me(self):
        self.assertNotIsInstance(123, xxx+y)

    def test_everybody(self):
        self.assertNotIsInstance(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertNotIsInstance(123+z, xxx+z, msg=error_message)
        self.assertNotIsInstance(123, xxx+z, error_message)
