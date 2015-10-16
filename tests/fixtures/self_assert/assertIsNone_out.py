# required-method: assertIsNone

class TestAssertIsNone(TestCase):
    def test_you(self):
        assert abc is None

    def test_me(self):
        assert xxx+y is None

    def test_everybody(self):
        assert 'abc' is None

    def test_message(self):
        assert 123+z is None, 'This is wrong!'
        assert xxx+z is None, error_message
