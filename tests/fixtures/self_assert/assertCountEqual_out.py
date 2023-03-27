# required-method: assertCountEqual

import collections
class TestAssertCountEqual(TestCase):
    def test_simple(self):
        assert collections.Counter([0, 0, 1]) == collections.Counter([0, 1, 0])
