# required-method: assertGreater

class TestAssertGreater(TestCase):
    def test_you(self):
        assert abc > 'xxx'

    def test_me(self):
        assert 123 > xxx+y
        assert 456 > (aaa and bbb)
        assert 789 > (ccc or ddd)
        assert 123 > (True if You else False)

    def test_everybody(self):
        assert 'abc' > 'def'

    def test_message(self):
        assert 123+z > xxx+z, 'This is wrong!'
        assert 123 > xxx+z, 'This is wrong!'
