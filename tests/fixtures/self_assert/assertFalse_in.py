# required-method: assertFalse

class TestAssertFalse(TestCase):
    def test_you(self):
        self.assertFalse(abc)

    def test_me(self):
        self.assertFalse(xxx+y)

    def test_everybody(self):
        self.assertFalse(    'def'   )

    def test_message(self):
        self.assertFalse(123+z, msg=error_message)
        self.assertFalse(xxx+z, 'This is wrong!')
