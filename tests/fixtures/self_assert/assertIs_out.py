# required-method: assertIs

class TestAssertIs(TestCase):
    def test_you(self):
        assert abc is 'xxx'

    def test_me(self):
        assert 123 is xxx+y

    def test_everybody(self):
        assert 'abc' is 'def'

    def test_message(self):
        assert 123+z is xxx+z, 'This is wrong!'
        assert 123 is xxx+z, 'This is wrong!'
