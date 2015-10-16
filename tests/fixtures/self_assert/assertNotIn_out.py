# required-method: assertNotIn

class TestAssertNotIn(TestCase):
    def test_you(self):
        assert abc not in 'xxx'

    def test_me(self):
        assert 123 not in xxx+y

    def test_everybody(self):
        assert 'abc' not in 'def'

    def test_message(self):
        assert 123+z not in xxx+z, error_message
        assert 123 not in xxx+z, error_message
