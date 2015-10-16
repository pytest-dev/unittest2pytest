# required-method: assertIn

class TestAssertIn(TestCase):
    def test_you(self):
        assert abc in 'xxx'

    def test_me(self):
        assert 123 in xxx+y

    def test_everybody(self):
        assert 'abc' in 'def'

    def test_message(self):
        assert 123 in xxx+z, 'This is wrong!'
        assert 123+z in xxx+z, 'This is wrong!'
