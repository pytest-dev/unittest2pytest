# required-method: assertIsNot

class TestAssertIsNot(TestCase):
    def test_you(self):
        assert abc is not 'xxx'

    def test_me(self):
        assert 123 is not xxx+y

    def test_everybody(self):
        assert 'abc' is not 'def'

    def test_message(self):
        assert 123+z is not xxx+z, error_message
        assert 123 is not xxx+z, error_message
