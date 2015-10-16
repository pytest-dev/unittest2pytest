# required-method: assertDictEqual

class TestDictEqual(TestCase):
    def test_simple(self):
        self.assertDictEqual(100, klm)

    def test_simple_msg(self):
        self.assertDictEqual(klm, 100, msg="This is wrong!")

    def test_simple_msg2(self):
        self.assertDictEqual(klm, 100, "This is wrong!")
