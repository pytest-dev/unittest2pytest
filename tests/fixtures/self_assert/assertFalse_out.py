# required-method: assertFalse

class TestAssertFalse(TestCase):
    def test_you(self):
        assert not abc

    def test_me(self):
        assert not xxx+y
        assert not (aaa and bbb)
        assert not (ccc or ddd)
        assert not (True if You else False)

    def test_everybody(self):
        assert not 'def'

    def test_message(self):
        assert not 123+z, error_message
        assert not xxx+z, 'This is wrong!'

    def test_expression_as_argument(self):
        assert not (abc not in self.data)
        assert not (abc in self.data)
        assert not (not contains)

    def test_generator(self):
        assert not (x for x in range(1))
        assert not (x for x in range(1))
        assert not (x for x in range(1)), "This is wrong"
