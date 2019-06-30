# required-method: assertIsNotNone

class TestAssertIsNotNone(TestCase):
    def test_you(self):
        self.assertIsNotNone(abc)

    def test_me(self):
        self.assertIsNotNone(xxx+y)
        self.assertIsNotNone(aaa and bbb)
        self.assertIsNotNone(ccc or ddd)
        self.assertIsNotNone(True if You else False)

    def test_everybody(self):
        self.assertIsNotNone(    'def'   )

    def test_message(self):
        self.assertIsNotNone(123+z, msg=error_message)
        self.assertIsNotNone(xxx+z, 'This is wrong!')

    def test_generator(self):
        self.assertIsNotNone((x for x in range(1)))
        self.assertIsNotNone(x for x in range(1))
        self.assertIsNotNone((x for x in range(1)), "This is wrong")
