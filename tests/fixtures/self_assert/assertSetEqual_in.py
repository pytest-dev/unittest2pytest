# required-method: assertSetEqual

class TestSetEqual(TestCase):
    def test_simple(self):
        self.assertSetEqual(100, klm)

    def test_simple_msg(self):
        self.assertSetEqual(klm, 100, msg="This is wrong!")

    def test_simple_msg2(self):
        self.assertSetEqual(klm, 100, "This is wrong!")
