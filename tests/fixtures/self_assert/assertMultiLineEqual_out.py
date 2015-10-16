# required-method: assertMultiLineEqual

class TestMultiLineEqual(TestCase):
    def test_simple(self):
        assert 100 == klm

    def test_simple_msg(self):
        assert klm == 100, "This is wrong!"

    def test_simple_msg2(self):
        assert klm == 100, "This is wrong!"
