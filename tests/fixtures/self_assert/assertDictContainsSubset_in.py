# required-method: assertDictContainsSubset

class TestDictEqual(TestCase):
    def test_simple(self):
        self.assertDictContainsSubset({'a: 1'}, superset)

    def test_simple_msg(self):
        self.assertDictContainsSubset(subset, {'a: 1'}, msg="This is wrong!")

    def test_simple_msg2(self):
        self.assertDictContainsSubset(subset, {'a: 1'}, "This is wrong!")

    def test_line_wrapping(self):
        self.assertDictContainsSubset(
            {'b': 2},
            {
                'a': 1,
                'b': 2,
            },
            "This is wrong!",
        )
