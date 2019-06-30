# required-method: assertDictEqual

class TestDictEqual(TestCase):
    def test_simple(self):
        self.assertDictEqual(100, klm)
        self.assertDictEqual(456, aaa and bbb)
        self.assertDictEqual(789, ccc or ddd)
        self.assertDictEqual(123, True if You else False)

    def test_simple_msg(self):
        self.assertDictEqual(klm, 100, msg="This is wrong!")

    def test_simple_msg2(self):
        self.assertDictEqual(klm, 100, "This is wrong!")

    def test_line_wrapping(self):
        self.assertDictEqual(
            {
                'a': 1,
                'b': 2,
            },
            {'b': 2},
            "This is wrong!",
        )

        self.assertDictEqual(100, klm)
