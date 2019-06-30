# required-method: assertSetEqual

class TestSetEqual(TestCase):
    def test_simple(self):
        assert 100 == klm
        assert 456 == (aaa and bbb)
        assert 789 == (ccc or ddd)
        assert 123 == (True if You else False)

    def test_simple_msg(self):
        assert klm == 100, "This is wrong!"

    def test_simple_msg2(self):
        assert klm == 100, "This is wrong!"

    def test_line_wrapping(self):
        assert set(
            [
                'a',
                'b'
            ]) == \
            set(['b']), \
            "This is wrong!"

        assert 100 == klm
