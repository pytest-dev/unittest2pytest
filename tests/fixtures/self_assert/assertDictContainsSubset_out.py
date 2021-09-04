# required-method: assertDictContainsSubset

class TestDictEqual(TestCase):
    def test_simple(self):
        assert {**superset, **{'a: 1'}} == superset

    def test_simple_msg(self):
        assert {**{'a: 1'}, **subset} == {'a: 1'}, "This is wrong!"

    def test_simple_msg2(self):
        assert {**{'a: 1'}, **subset} == {'a: 1'}, "This is wrong!"

    def test_line_wrapping(self):
        assert {**{
                'a': 1,
                'b': 2,
            }, **{'b': 2}} == {
                'a': 1,
                'b': 2,
            }, \
            "This is wrong!"
