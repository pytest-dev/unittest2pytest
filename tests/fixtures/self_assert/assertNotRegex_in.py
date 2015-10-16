# required-method: assertNotRegex

class TestAssertEqual(TestCase):
    def test_you(self):
        self.assertNotRegex(abc, 'xxx')

    def test_me(self):
        self.assertNotRegex(123, xxx+y)

    def test_everybody(self):
        self.assertNotRegex(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertNotRegex(123+z, xxx+y, msg='This is wrong!')
        self.assertNotRegex(123, xxx+y, 'This is wrong!')
