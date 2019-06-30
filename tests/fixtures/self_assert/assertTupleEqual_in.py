# required-method: assertTupleEqual

class TestTupleEqual(TestCase):
    def test_simple(self):
        self.assertTupleEqual(100, klm)
        self.assertTupleEqual(456, aaa and bbb)
        self.assertTupleEqual(789, ccc or ddd)
        self.assertTupleEqual(123, True if You else False)

    def test_simple_msg(self):
        self.assertTupleEqual(klm, 100, msg="This is wrong!")

    def test_simple_msg2(self):
        self.assertTupleEqual(klm, 100, "This is wrong!")

    def test_line_wrapping(self):
        self.assertTupleEqual(
            (
                'a',
                'b'
            ),
            ('b',),
            "This is wrong!",
        )

        self.assertTupleEqual(100, klm)
