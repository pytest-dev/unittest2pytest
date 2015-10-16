# required-method: assertIs

class TestAssertIs(TestCase):
    def test_you(self):
        self.assertIs(abc, 'xxx')

    def test_me(self):
        self.assertIs(123, xxx+y)

    def test_everybody(self):
        self.assertIs(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertIs(123+z, xxx+z, msg='This is wrong!')
        self.assertIs(123, xxx+z, 'This is wrong!')
