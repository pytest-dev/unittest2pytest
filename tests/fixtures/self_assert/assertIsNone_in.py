# required-method: assertIsNone

class TestAssertIsNone(TestCase):
    def test_you(self):
        self.assertIsNone(abc)

    def test_me(self):
        self.assertIsNone(xxx+y)

    def test_everybody(self):
        self.assertIsNone(   'abc'   )

    def test_message(self):
        self.assertIsNone(123+z, msg='This is wrong!')
        self.assertIsNone(xxx+z, error_message)
