# required-method: assertIsNot

class TestAssertIsNot(TestCase):
    def test_you(self):
        assert abc is not 'xxx'

    def test_me(self):
        assert 123 is not xxx+y
        assert 456 is not (aaa and bbb)
        assert 789 is not (ccc or ddd)
        assert 123 is not (True if You else False)

    def test_everybody(self):
        assert 'abc' is not 'def'

    def test_message(self):
        assert 123+z is not xxx+z, error_message
        assert 123 is not xxx+z, error_message
