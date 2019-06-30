# required-method: assertTrue

class TestAssertTrue(TestCase):
    def test_you(self):
        assert abc

    def test_me(self):
        assert xxx+y
        assert aaa and bbb
        assert ccc or ddd
        assert True if You else False

    def test_everybody(self):
        assert 'abc'

    def test_message(self):
        assert 123+z, 'This is wrong!'
        assert xxx+z, error_message

    def test_expression_as_argument(self):
        assert abc not in self.data
        assert abc in self.data
        assert not contains

    def test_generator(self):
        assert (x for x in range(1))
        assert (x for x in range(1))
        assert (x for x in range(1)), "This is wrong"
