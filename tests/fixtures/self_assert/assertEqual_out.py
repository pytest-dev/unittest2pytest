# required-method: assertEqual

class TestAssertEqual(TestCase):
    def test_you(self):
        assert abc == 'xxx'
        assert abc == 'xxx'

    def test_me(self):
        assert 123 == xxx+y
        assert 456 == (aaa and bbb)
        assert 789 == (ccc or ddd)
        assert 123 == (True if You else False)

    def test_everybody(self):
        assert 'abc' == 'def'

    def test_message(self):
        assert 123+z == xxx+y, 'This is wrong!'
        assert 123 == xxx+y, 'This is wrong!'

    def test_line_wrapping(self):
        assert True == False, 'This will fail %s' % \
                'always'

        assert 'abc' \
                         .replace(
                                  'abc'
                                  , 'def') == \
                         'def', \
                         'Wrap %s' % \
                         'everything'

    def test_expression_as_argument(self):
        assert (abc not in self.data) == True
        assert (abc in self.data) == (not contains)
        assert contains == (not contains)
