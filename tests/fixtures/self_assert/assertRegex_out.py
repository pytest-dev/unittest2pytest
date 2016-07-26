# required-method: assertRegex

import re
class TestAssertEqual(TestCase):
    def test_you(self):
        assert re.search('xxx', abc)

    def test_me(self):
        assert re.search(xxx+y, 123)

    def test_everybody(self):
        assert re.search('def', 'abc')

    def test_message(self):
        assert re.search(xxx+y, 123+z), 'This is wrong!'
        assert re.search(xxx+y, 123), 'This is wrong!'
