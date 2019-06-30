# required-method: assertIn

class TestAssertIn(TestCase):
    def test_you(self):
        assert abc in 'xxx'

    def test_me(self):
        assert 123 in xxx+y
        assert 456 in (aaa and bbb)
        assert 789 in (ccc or ddd)
        assert 123 in (True if You else False)

    def test_everybody(self):
        assert 'abc' in 'def'

    def test_message(self):
        assert 123 in xxx+z, 'This is wrong!'
        assert 123+z in xxx+z, 'This is wrong!'
