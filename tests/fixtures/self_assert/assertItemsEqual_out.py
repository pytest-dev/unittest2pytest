# required-method: assertItemsEqual

class TestItemsEqual(TestCase):
    def test_simple(self):
        assert sorted(a) == sorted(b)

    def test_simple_msg(self):
        assert sorted(a) == sorted(b), "This is wrong!"

    def test_simple_msg2(self):
        assert sorted(a) == sorted(b), "This is wrong!"
