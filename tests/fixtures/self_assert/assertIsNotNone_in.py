# required-method: assertIsNotNone

class TestAssertIsNotNone(TestCase):
    def test_you(self):
        self.assertIsNotNone(abc)

    def test_me(self):
        self.assertIsNotNone(xxx+y)

    def test_everybody(self):
        self.assertIsNotNone(    'def'   )

    def test_message(self):
        self.assertIsNotNone(123+z, msg=error_message)
        self.assertIsNotNone(xxx+z, 'This is wrong!')
