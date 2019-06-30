# required-method: assertNotIsInstance

class TestAssertNotIsInstance(TestCase):
    def test_you(self):
        assert not isinstance(abc, 'xxx')

    def test_me(self):
        assert not isinstance(123, xxx+y)
        assert not isinstance(456, aaa and bbb)
        assert not isinstance(789, ccc or ddd)
        assert not isinstance(123, True if You else False)

    def test_everybody(self):
        assert not isinstance('abc', 'def')

    def test_message(self):
        assert not isinstance(123+z, xxx+z), error_message
        assert not isinstance(123, xxx+z), error_message
