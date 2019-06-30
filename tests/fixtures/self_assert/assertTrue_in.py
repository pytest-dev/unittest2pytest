# required-method: assertTrue

class TestAssertTrue(TestCase):
    def test_you(self):
        self.assertTrue(abc)

    def test_me(self):
        self.assertTrue(xxx+y)
        self.assertTrue(aaa and bbb)
        self.assertTrue(ccc or ddd)
        self.assertTrue(True if You else False)

    def test_everybody(self):
        self.assertTrue(   'abc'   )

    def test_message(self):
        self.assertTrue(123+z, msg='This is wrong!')
        self.assertTrue(xxx+z, error_message)

    def test_expression_as_argument(self):
        self.assertTrue(abc not in self.data)
        self.assertTrue(abc in self.data)
        self.assertTrue(not contains)

    def test_generator(self):
        self.assertTrue((x for x in range(1)))
        self.assertTrue(x for x in range(1))
        self.assertTrue((x for x in range(1)), "This is wrong")
