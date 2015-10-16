# required-method: assertTupleEqual

class TestTupleEqual(TestCase):
    def test_simple(self):
        self.assertTupleEqual(100, klm)

    def test_simple_msg(self):
        self.assertTupleEqual(klm, 100, msg="This is wrong!")

    def test_simple_msg2(self):
        self.assertTupleEqual(klm, 100, "This is wrong!")
