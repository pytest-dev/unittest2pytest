
class TestAssertEqual(TestCase):
    def test_you(self):
        assert abc == 'xxx'
        assert abc == 'xxx'

    def test_me(self):
        assert 123 == xxx+y

    def test_everybody(self):
        assert 'abc' == 'def'

    def test_message(self):
        assert 123+z == xxx+y, 'This is wrong!'
        assert 123 == xxx+y, 'This is wrong!'


class TestAssertNotEqual(TestCase):
    def test_you(self):
        assert abc != 'xxx'
        assert abc != 'xxx'

    def test_me(self):
        assert 123 != xxx+y

    def test_everybody(self):
        assert 'abc' != 'def'

    def test_message(self):
        assert 123+z != xxx+z, error_message
        assert 123 != xxx+z, error_message


class TestAssertGreater(TestCase):
    def test_you(self):
        assert abc > 'xxx'

    def test_me(self):
        assert 123 > xxx+y

    def test_everybody(self):
        assert 'abc' > 'def'

    def test_message(self):
        assert 123+z > xxx+z, 'This is wrong!'
        assert 123 > xxx+z, 'This is wrong!'


class TestAssertGreaterEqual(TestCase):
    def test_you(self):
        assert abc >= 'xxx'

    def test_me(self):
        assert 123 >= xxx+y

    def test_everybody(self):
        assert 'abc' >= 'def'

    def test_message(self):
        assert 123+z >= xxx+z, error_message
        assert 123 >= xxx+z, error_message


class TestAssertIs(TestCase):
    def test_you(self):
        assert abc is 'xxx'

    def test_me(self):
        assert 123 is xxx+y

    def test_everybody(self):
        assert 'abc' is 'def'

    def test_message(self):
        assert 123+z is xxx+z, 'This is wrong!'
        assert 123 is xxx+z, 'This is wrong!'


class TestAssertIsNot(TestCase):
    def test_you(self):
        assert abc is not 'xxx'

    def test_me(self):
        assert 123 is not xxx+y

    def test_everybody(self):
        assert 'abc' is not 'def'

    def test_message(self):
        assert 123+z is not xxx+z, error_message
        assert 123 is not xxx+z, error_message


class TestAssertIn(TestCase):
    def test_you(self):
        assert abc in 'xxx'

    def test_me(self):
        assert 123 in xxx+y

    def test_everybody(self):
        assert 'abc' in 'def'

    def test_message(self):
        assert 123 in xxx+z, 'This is wrong!'
        assert 123+z in xxx+z, 'This is wrong!'


class TestAssertNotIn(TestCase):
    def test_you(self):
        assert abc not in 'xxx'

    def test_me(self):
        assert 123 not in xxx+y

    def test_everybody(self):
        assert 'abc' not in 'def'

    def test_message(self):
        assert 123+z not in xxx+z, error_message
        assert 123 not in xxx+z, error_message


class TestAssertLess(TestCase):
    def test_you(self):
        assert abc < 'xxx'

    def test_me(self):
        assert 123 < xxx+y

    def test_everybody(self):
        assert 'abc' < 'def'

    def test_message(self):
        assert 123+z < xxx+z, 'This is wrong!'
        assert 123 < xxx+z, 'This is wrong!'


class TestAssertLessEqual(TestCase):
    def test_you(self):
        assert abc <= 'xxx'

    def test_me(self):
        assert 123 <= xxx+y

    def test_everybody(self):
        assert 'abc' <= 'def'

    def test_message(self):
        assert 123+z <= xxx+z, error_message
        assert 123 <= xxx+z, error_message



class TestAssertTrue(TestCase):
    def test_you(self):
        assert abc

    def test_me(self):
        assert xxx+y

    def test_everybody(self):
        assert 'abc'

    def test_message(self):
        assert 123+z, 'This is wrong!'
        assert xxx+z, error_message


class TestAssertFalse(TestCase):
    def test_you(self):
        assert not abc

    def test_me(self):
        assert not xxx+y

    def test_everybody(self):
        assert not 'def'

    def test_message(self):
        assert not 123+z, error_message
        assert not xxx+z, 'This is wrong!'



class TestAssertIsNone(TestCase):
    def test_you(self):
        assert abc is None

    def test_me(self):
        assert xxx+y is None

    def test_everybody(self):
        assert 'abc' is None

    def test_message(self):
        assert 123+z is None, 'This is wrong!'
        assert xxx+z is None, error_message


class TestAssertIsNotNone(TestCase):
    def test_you(self):
        assert abc is not None

    def test_me(self):
        assert xxx+y is not None

    def test_everybody(self):
        assert 'def' is not None

    def test_message(self):
        assert 123+z is not None, error_message
        assert xxx+z is not None, 'This is wrong!'



class TestAssertIsInstance(TestCase):
    def test_you(self):
        assert isinstance(abc, 'xxx')

    def test_me(self):
        assert isinstance(123, xxx+y)

    def test_everybody(self):
        assert isinstance('abc', 'def')

    def test_message(self):
        assert isinstance(123+z, xxx+z), 'This is wrong!'
        assert isinstance(123, xxx+z), 'This is wrong!'


class TestAssertNotIsInstance(TestCase):
    def test_you(self):
        assert not isinstance(abc, 'xxx')

    def test_me(self):
        assert not isinstance(123, xxx+y)

    def test_everybody(self):
        assert not isinstance('abc', 'def')

    def test_message(self):
        assert not isinstance(123+z, xxx+z), error_message
        assert not isinstance(123, xxx+z), error_message
