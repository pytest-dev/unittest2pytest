# required-method: assertFalse

class TestAssertFalse(TestCase):
    def test_you(self):
        self.assertFalse(abc)

    def test_me(self):
        self.assertFalse(xxx+y)
        self.assertFalse(aaa and bbb)
        self.assertFalse(ccc or ddd)
        self.assertFalse(True if You else False)

    def test_everybody(self):
        self.assertFalse(    'def'   )

    def test_message(self):
        self.assertFalse(123+z, msg=error_message)
        self.assertFalse(xxx+z, 'This is wrong!')

    def test_expression_as_argument(self):
        self.assertFalse(abc not in self.data)
        self.assertFalse(abc in self.data)
        self.assertFalse(not contains)

    def test_generator(self):
        self.assertFalse((x for x in range(1)))
        self.assertFalse(x for x in range(1))
        self.assertFalse((x for x in range(1)), "This is wrong")
