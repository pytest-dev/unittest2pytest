# required-method: assertIsNotNone

class TestAssertIsNotNone(TestCase):
    def test_you(self):
        assert abc is not None

    def test_me(self):
        assert xxx+y is not None

    def test_everybody(self):
        assert 'def' is not None

    def test_message(self):
        assert 123+z is not None, error_message
        assert xxx+z is not None, 'This is wrong!'
