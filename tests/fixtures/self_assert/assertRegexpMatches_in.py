# required-method: assertRegexpMatches

class TestAssertEqual(TestCase):
    def test_you(self):
        self.assertRegexpMatches(abc, 'xxx')

    def test_me(self):
        self.assertRegexpMatches(123, xxx+y)

    def test_everybody(self):
        self.assertRegexpMatches(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertRegexpMatches(123+z, xxx+y, msg='This is wrong!')
        self.assertRegexpMatches(123, xxx+y, 'This is wrong!')
