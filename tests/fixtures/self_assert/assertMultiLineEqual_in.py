# required-method: assertMultiLineEqual

class TestMultiLineEqual(TestCase):
    def test_simple(self):
        self.assertMultiLineEqual(100, klm)
        self.assertMultiLineEqual(456, aaa and bbb)
        self.assertMultiLineEqual(789, ccc or ddd)
        self.assertMultiLineEqual(123, True if You else False)

    def test_simple_msg(self):
        self.assertMultiLineEqual(klm, 100, msg="This is wrong!")

    def test_simple_msg2(self):
        self.assertMultiLineEqual(klm, 100, "This is wrong!")
