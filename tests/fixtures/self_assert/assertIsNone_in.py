# required-method: assertIsNone

class TestAssertIsNone(TestCase):
    def test_you(self):
        self.assertIsNone(abc)

    def test_me(self):
        self.assertIsNone(xxx+y)
        self.assertIsNone(aaa and bbb)
        self.assertIsNone(ccc or ddd)
        self.assertIsNone(True if You else False)

    def test_everybody(self):
        self.assertIsNone(   'abc'   )

    def test_message(self):
        self.assertIsNone(123+z, msg='This is wrong!')
        self.assertIsNone(xxx+z, error_message)

    def test_generator(self):
        self.assertIsNone((x for x in range(1)))
        self.assertIsNone(x for x in range(1))
        self.assertIsNone((x for x in range(1)), "This is wrong")
