# required-method: assertEqual

class TestAssertEqual(TestCase):
    def test_you(self):
        self.assertEqual(abc, 'xxx')
        self.assertEquals(abc, 'xxx')

    def test_me(self):
        self.assertEqual(123, xxx+y)

    def test_everybody(self):
        self.assertEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertEqual(123+z, xxx+y, msg='This is wrong!')
        self.assertEqual(123, xxx+y, 'This is wrong!')
