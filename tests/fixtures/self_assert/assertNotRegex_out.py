# required-method: assertNotRegex

import re
class TestAssertEqual(TestCase):
    def test_you(self):
        assert not re.search('xxx', abc)

    def test_me(self):
        assert not re.search(xxx+y, 123)

    def test_everybody(self):
        assert not re.search('def', 'abc')

    def test_message(self):
        assert not re.search(xxx+y, 123+z), 'This is wrong!'
        assert not re.search(xxx+y, 123), 'This is wrong!'
