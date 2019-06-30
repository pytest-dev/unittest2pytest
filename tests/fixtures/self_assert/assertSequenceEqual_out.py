# required-method: assertSequenceEqual

class TestSequenceEqual(TestCase):
    def test_simple(self):
        assert 100 == klm
        assert 456 == (aaa and bbb)
        assert 789 == (ccc or ddd)
        assert 123 == (True if You else False)

    def test_simple_msg(self):
        assert klm == 100, "This is wrong!"

    def test_simple_msg2(self):
        assert klm == 100, "This is wrong!"

    def test_type(self):
        # TODO: assert isinstance(100, list)
        # TODO: assert isinstance(klm, list)
        assert 100 == klm

    def test_type_msg(self):
        # TODO: assert isinstance(klm, tuple)
        # TODO: assert isinstance(100, tuple)
        assert klm == 100, "This is wrong!"

    def test_type_msg2(self):
        # TODO: assert isinstance(klm, list)
        # TODO: assert isinstance(100, list)
        assert klm == 100, "This is wrong!"

    def test_line_wrapping(self):
        assert [
                'a',
                'b'
            ] == \
            ['b'], \
            "This is wrong!"

        assert 100 == klm
