# required-method: assertRegex

class TestAssertEqual(TestCase):
    def test_you(self):
        self.assertRegex(abc, 'xxx')

    def test_me(self):
        self.assertRegex(123, xxx+y)

    def test_everybody(self):
        self.assertRegex(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertRegex(123+z, xxx+y, msg='This is wrong!')
        self.assertRegex(123, xxx+y, 'This is wrong!')
