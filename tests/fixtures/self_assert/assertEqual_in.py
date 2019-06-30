# required-method: assertEqual

class TestAssertEqual(TestCase):
    def test_you(self):
        self.assertEqual(abc, 'xxx')
        self.assertEquals(abc, 'xxx')

    def test_me(self):
        self.assertEqual(123, xxx+y)
        self.assertEqual(456, aaa and bbb)
        self.assertEqual(789, ccc or ddd)
        self.assertEqual(123, True if You else False)

    def test_everybody(self):
        self.assertEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertEqual(123+z, xxx+y, msg='This is wrong!')
        self.assertEqual(123, xxx+y, 'This is wrong!')

    def test_line_wrapping(self):
        self.assertEqual(True, False, 'This will fail %s' %
                'always')

        self.assertEqual(

                         'abc'
                         .replace(
                                  'abc'
                                  , 'def'),
                         'def',
                         msg='Wrap %s' %
                         'everything')

    def test_expression_as_argument(self):
        self.assertEqual(abc not in self.data, True)
        self.assertEqual(abc in self.data, not contains)
        self.assertEqual(contains, not contains)
