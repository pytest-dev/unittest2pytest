# required-method: assertSetEqual

class TestSetEqual(TestCase):
    def test_simple(self):
        self.assertSetEqual(100, klm)
        self.assertSetEqual(456, aaa and bbb)
        self.assertSetEqual(789, ccc or ddd)
        self.assertSetEqual(123, True if You else False)

    def test_simple_msg(self):
        self.assertSetEqual(klm, 100, msg="This is wrong!")

    def test_simple_msg2(self):
        self.assertSetEqual(klm, 100, "This is wrong!")

    def test_line_wrapping(self):
        self.assertSetEqual(set(
            [
                'a',
                'b'
            ]),
            set(['b']),
            "This is wrong!",
        )

        self.assertSetEqual(100, klm)
