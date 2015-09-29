
class TestAssertEqual(TestCase):
    def test_you(self):
        self.assertEqual(abc, 'xxx')
        self.assertEquals(abc, 'xxx')

    def test_me(self):
        self.assertEqual(123, xxx+y)

    def test_everybody(self):
        self.assertEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertEqual(123+z, xxx+y, msg='This is wrong!')
        self.assertEqual(123, xxx+y, 'This is wrong!')


class TestAssertNotEqual(TestCase):
    def test_you(self):
        self.assertNotEqual(abc, 'xxx')
        self.assertNotEquals(abc, 'xxx')

    def test_me(self):
        self.assertNotEqual(123, xxx+y)

    def test_everybody(self):
        self.assertNotEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertNotEqual(123+z, xxx+z, msg=error_message)
        self.assertNotEqual(123, xxx+z, error_message)


class TestAssertGreater(TestCase):
    def test_you(self):
        self.assertGreater(abc, 'xxx')

    def test_me(self):
        self.assertGreater(123, xxx+y)

    def test_everybody(self):
        self.assertGreater(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertGreater(123+z, xxx+z, msg='This is wrong!')
        self.assertGreater(123, xxx+z, 'This is wrong!')


class TestAssertGreaterEqual(TestCase):
    def test_you(self):
        self.assertGreaterEqual(abc, 'xxx')

    def test_me(self):
        self.assertGreaterEqual(123, xxx+y)

    def test_everybody(self):
        self.assertGreaterEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertGreaterEqual(123+z, xxx+z, msg=error_message)
        self.assertGreaterEqual(123, xxx+z, error_message)


class TestAssertIs(TestCase):
    def test_you(self):
        self.assertIs(abc, 'xxx')

    def test_me(self):
        self.assertIs(123, xxx+y)

    def test_everybody(self):
        self.assertIs(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertIs(123+z, xxx+z, msg='This is wrong!')
        self.assertIs(123, xxx+z, 'This is wrong!')


class TestAssertIsNot(TestCase):
    def test_you(self):
        self.assertIsNot(abc, 'xxx')

    def test_me(self):
        self.assertIsNot(123, xxx+y)

    def test_everybody(self):
        self.assertIsNot(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertIsNot(123+z, xxx+z, msg=error_message)
        self.assertIsNot(123, xxx+z, error_message)


class TestAssertIn(TestCase):
    def test_you(self):
        self.assertIn(abc, 'xxx')

    def test_me(self):
        self.assertIn(123, xxx+y)

    def test_everybody(self):
        self.assertIn(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertIn(123, xxx+z, 'This is wrong!')
        self.assertIn(123+z, xxx+z, msg='This is wrong!')


class TestAssertNotIn(TestCase):
    def test_you(self):
        self.assertNotIn(abc, 'xxx')

    def test_me(self):
        self.assertNotIn(123, xxx+y)

    def test_everybody(self):
        self.assertNotIn(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertNotIn(123+z, xxx+z, msg=error_message)
        self.assertNotIn(123, xxx+z, error_message)


class TestAssertLess(TestCase):
    def test_you(self):
        self.assertLess(abc, 'xxx')

    def test_me(self):
        self.assertLess(123, xxx+y)

    def test_everybody(self):
        self.assertLess(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertLess(123+z, xxx+z, msg='This is wrong!')
        self.assertLess(123, xxx+z, 'This is wrong!')


class TestAssertLessEqual(TestCase):
    def test_you(self):
        self.assertLessEqual(abc, 'xxx')

    def test_me(self):
        self.assertLessEqual(123, xxx+y)

    def test_everybody(self):
        self.assertLessEqual(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertLessEqual(123+z, xxx+z, msg=error_message)
        self.assertLessEqual(123, xxx+z, error_message)



class TestAssertTrue(TestCase):
    def test_you(self):
        self.assertTrue(abc)

    def test_me(self):
        self.assertTrue(xxx+y)

    def test_everybody(self):
        self.assertTrue(   'abc'   )

    def test_message(self):
        self.assertTrue(123+z, msg='This is wrong!')
        self.assertTrue(xxx+z, error_message)


class TestAssertFalse(TestCase):
    def test_you(self):
        self.assertFalse(abc)

    def test_me(self):
        self.assertFalse(xxx+y)

    def test_everybody(self):
        self.assertFalse(    'def'   )

    def test_message(self):
        self.assertFalse(123+z, msg=error_message)
        self.assertFalse(xxx+z, 'This is wrong!')



class TestAssertIsNone(TestCase):
    def test_you(self):
        self.assertIsNone(abc)

    def test_me(self):
        self.assertIsNone(xxx+y)

    def test_everybody(self):
        self.assertIsNone(   'abc'   )

    def test_message(self):
        self.assertIsNone(123+z, msg='This is wrong!')
        self.assertIsNone(xxx+z, error_message)


class TestAssertIsNotNone(TestCase):
    def test_you(self):
        self.assertIsNotNone(abc)

    def test_me(self):
        self.assertIsNotNone(xxx+y)

    def test_everybody(self):
        self.assertIsNotNone(    'def'   )

    def test_message(self):
        self.assertIsNotNone(123+z, msg=error_message)
        self.assertIsNotNone(xxx+z, 'This is wrong!')



class TestAssertIsInstance(TestCase):
    def test_you(self):
        self.assertIsInstance(abc, 'xxx')

    def test_me(self):
        self.assertIsInstance(123, xxx+y)

    def test_everybody(self):
        self.assertIsInstance(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertIsInstance(123+z, xxx+z, msg='This is wrong!')
        self.assertIsInstance(123, xxx+z, 'This is wrong!')


class TestAssertNotIsInstance(TestCase):
    def test_you(self):
        self.assertNotIsInstance(abc, 'xxx')

    def test_me(self):
        self.assertNotIsInstance(123, xxx+y)

    def test_everybody(self):
        self.assertNotIsInstance(   'abc'   ,    'def'   )

    def test_message(self):
        self.assertNotIsInstance(123+z, xxx+z, msg=error_message)
        self.assertNotIsInstance(123, xxx+z, error_message)
