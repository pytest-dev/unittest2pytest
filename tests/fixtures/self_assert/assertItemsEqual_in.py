# required-method: assertItemsEqual

class TestItemsEqual(TestCase):
    def test_simple(self):
        self.assertItemsEqual(a, b)

    def test_simple_msg(self):
        self.assertItemsEqual(a, b, msg="This is wrong!")

    def test_simple_msg2(self):
        self.assertItemsEqual(a, b, "This is wrong!")
