# required-method: assertAlmostEqual

class TestAlmostAssertEqual(TestCase):
    def test_simple(self):
        self.assertAlmostEqual(100, klm)
        self.assertAlmostEqual(456, aaa and bbb)
        self.assertAlmostEqual(789, ccc or ddd)
        self.assertAlmostEqual(123, True if You else False)

    def test_simple_msg(self):
        self.assertAlmostEqual(klm, 100, msg="This is wrong!")

    def test_places(self):
        self.assertAlmostEqual(50+x, klm, 1)

    def test_places_msg(self):
        self.assertAlmostEqual(klm, 100, 1, msg=error_message)

    def test_places_kw(self):
        self.assertAlmostEqual(100, klm, places=1)

    def test_places_kw_msg(self):
        self.assertAlmostEqual(klm, 50+x, places=1, msg="This is wrong!")

    def test_places_kw_msg2(self):
        self.assertAlmostEqual(100, klm, msg=error_message, places=1)


    def test_delta_kw(self):
        self.assertAlmostEqual(klm, 100.01, delta=1)

    def test_delta_kw_msg(self):
        self.assertAlmostEqual(50+x, klm, delta=1, msg="This is wrong!")

    def test_delta_kw_msg2(self):
        self.assertAlmostEqual(klm, 100, msg=error_message, delta=1)
