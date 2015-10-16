# required-method: assertSequenceEqual

class TestSequenceEqual(TestCase):
    def test_simple(self):
        self.assertSequenceEqual(100, klm)

    def test_simple_msg(self):
        self.assertSequenceEqual(klm, 100, msg="This is wrong!")

    def test_simple_msg2(self):
        self.assertSequenceEqual(klm, 100, "This is wrong!")

    def test_type(self):
        # TODO: assert isinstance(100, list)
        # TODO: assert isinstance(klm, list)
        self.assertSequenceEqual(100, klm, seq_type=list)

    def test_type_msg(self):
        # TODO: assert isinstance(klm, tuple)
        # TODO: assert isinstance(100, tuple)
        self.assertSequenceEqual(klm, 100, seq_type=tuple, msg="This is wrong!")

    def test_type_msg2(self):
        # TODO: assert isinstance(klm, list)
        # TODO: assert isinstance(100, list)
        self.assertSequenceEqual(klm, 100, "This is wrong!", list)
