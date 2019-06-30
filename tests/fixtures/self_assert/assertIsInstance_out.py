# required-method: assertIsInstance

class TestAssertIsInstance(TestCase):
    def test_you(self):
        assert isinstance(abc, 'xxx')

    def test_me(self):
        assert isinstance(123, xxx+y)
        assert isinstance(456, aaa and bbb)
        assert isinstance(789, ccc or ddd)
        assert isinstance(123, True if You else False)

    def test_everybody(self):
        assert isinstance('abc', 'def')

    def test_message(self):
        assert isinstance(123+z, xxx+z), 'This is wrong!'
        assert isinstance(123, xxx+z), 'This is wrong!'
