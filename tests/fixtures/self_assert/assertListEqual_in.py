# required-method: assertListEqual

class TestListEqual(TestCase):
    def test_simple(self):
        self.assertListEqual(100, klm)

    def test_simple_msg(self):
        self.assertListEqual(klm, 100, msg="This is wrong!")

    def test_simple_msg2(self):
        self.assertListEqual(klm, 100, "This is wrong!")
