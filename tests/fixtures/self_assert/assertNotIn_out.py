# required-method: assertNotIn

class TestAssertNotIn(TestCase):
    def test_you(self):
        assert abc not in 'xxx'

    def test_me(self):
        assert 123 not in xxx+y
        assert 456 not in (aaa and bbb)
        assert 789 not in (ccc or ddd)
        assert 123 not in (True if You else False)

    def test_everybody(self):
        assert 'abc' not in 'def'

    def test_message(self):
        assert 123+z not in xxx+z, error_message
        assert 123 not in xxx+z, error_message
