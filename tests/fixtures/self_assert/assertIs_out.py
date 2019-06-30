# required-method: assertIs

class TestAssertIs(TestCase):
    def test_you(self):
        assert abc is 'xxx'

    def test_me(self):
        assert 123 is xxx+y
        assert 456 is (aaa and bbb)
        assert 789 is (ccc or ddd)
        assert 123 is (True if You else False)

    def test_everybody(self):
        assert 'abc' is 'def'

    def test_message(self):
        assert 123+z is xxx+z, 'This is wrong!'
        assert 123 is xxx+z, 'This is wrong!'
