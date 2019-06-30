# required-method: assertIsNotNone

class TestAssertIsNotNone(TestCase):
    def test_you(self):
        assert abc is not None

    def test_me(self):
        assert xxx+y is not None
        assert (aaa and bbb) is not None
        assert (ccc or ddd) is not None
        assert (True if You else False) is not None

    def test_everybody(self):
        assert 'def' is not None

    def test_message(self):
        assert 123+z is not None, error_message
        assert xxx+z is not None, 'This is wrong!'

    def test_generator(self):
        assert (x for x in range(1)) is not None
        assert (x for x in range(1)) is not None
        assert (x for x in range(1)) is not None, "This is wrong"
