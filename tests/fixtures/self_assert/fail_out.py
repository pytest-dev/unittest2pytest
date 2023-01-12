# required-method: fail

import pytest
class TestAssertTrue(TestCase):
    def test_me(self):
        pytest.fail(xxx+y)
        pytest.fail(aaa % bbb)
        pytest.fail(ccc or ddd)

    def test_everybody(self):
        pytest.fail(   'abc'   )

    def test_message(self):
        pytest.fail(msg='This is wrong!')
        pytest.fail(error_message)

    def test_nothing(self):
        pytest.fail()
        pytest.fail(pytest.fail())
