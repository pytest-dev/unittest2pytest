# required-method: assertNotAlmostEqual

class TestAssertNotAlmostEqual(TestCase):
    def test_simple(self):
        assert round(abs(100-klm), 7) != 0
        assert round(abs(456-(aaa and bbb)), 7) != 0
        assert round(abs(789-(ccc or ddd)), 7) != 0
        assert round(abs(123-(True if You else False)), 7) != 0

    def test_simple_msg(self):
        assert round(abs(klm-50+x), 7) != 0, "This is wrong!"

    def test_places(self):
        assert round(abs(100-klm), 1) != 0

    def test_places_msg(self):
        assert round(abs(klm-100), 1) != 0, error_message

    def test_places_kw(self):
        assert round(abs(50+x-klm), 1) != 0

    def test_places_kw_msg(self):
        assert round(abs(klm-100), 1) != 0, "This is wrong!"

    def test_places_kw_msg2(self):
        assert round(abs(100-klm), 1) != 0, error_message


    def test_delta_kw(self):
        assert abs(klm-50+x) > 1

    def test_delta_kw_msg(self):
        assert abs(100-klm) > 1, "This is wrong!"

    def test_delta_kw_msg2(self):
        assert abs(klm-100) > 1, error_message
