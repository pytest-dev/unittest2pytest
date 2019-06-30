# required-method: assertNotAlmostEqual

class TestAssertNotAlmostEqual(TestCase):
    def test_simple(self):
        self.assertNotAlmostEqual(100, klm)
        self.assertNotAlmostEqual(456, aaa and bbb)
        self.assertNotAlmostEqual(789, ccc or ddd)
        self.assertNotAlmostEqual(123, True if You else False)

    def test_simple_msg(self):
        self.assertNotAlmostEqual(klm, 50+x, msg="This is wrong!")

    def test_places(self):
        self.assertNotAlmostEqual(100, klm, 1)

    def test_places_msg(self):
        self.assertNotAlmostEqual(klm, 100, 1, msg=error_message)

    def test_places_kw(self):
        self.assertNotAlmostEqual(50+x, klm, places=1)

    def test_places_kw_msg(self):
        self.assertNotAlmostEqual(klm, 100, places=1, msg="This is wrong!")

    def test_places_kw_msg2(self):
        self.assertNotAlmostEqual(100, klm, msg=error_message, places=1)


    def test_delta_kw(self):
        self.assertNotAlmostEqual(klm, 50+x, delta=1)

    def test_delta_kw_msg(self):
        self.assertNotAlmostEqual(100, klm, delta=1, msg="This is wrong!")

    def test_delta_kw_msg2(self):
        self.assertNotAlmostEqual(klm, 100, msg=error_message, delta=1)
