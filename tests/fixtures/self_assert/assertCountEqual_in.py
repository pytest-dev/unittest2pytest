# required-method: assertCountEqual

class TestAssertCountEqual(TestCase):
    def test_simple(self):
        self.assertCountEqual([0, 0, 1], [0, 1, 0])
