# required-method: assertDictContainsSubset

class TestDictEqual(TestCase):
    def test_simple(self):
        assert dict({'a: 1'}, **superset) == superset

    def test_simple_msg(self):
        assert dict(subset, **{'a: 1'}) == {'a: 1'}, "This is wrong!"

    def test_simple_msg2(self):
        assert dict(subset, **{'a: 1'}) == {'a: 1'}, "This is wrong!"

    def test_line_wrapping(self):
        assert dict({'b': 2}, **{
                'a': 1,
                'b': 2,
            }) == {
                'a': 1,
                'b': 2,
            }, \
            "This is wrong!"
