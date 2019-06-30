# required-method: assertIsNone

class TestAssertIsNone(TestCase):
    def test_you(self):
        assert abc is None

    def test_me(self):
        assert xxx+y is None
        assert (aaa and bbb) is None
        assert (ccc or ddd) is None
        assert (True if You else False) is None

    def test_everybody(self):
        assert 'abc' is None

    def test_message(self):
        assert 123+z is None, 'This is wrong!'
        assert xxx+z is None, error_message

    def test_generator(self):
        assert (x for x in range(1)) is None
        assert (x for x in range(1)) is None
        assert (x for x in range(1)) is None, "This is wrong"
