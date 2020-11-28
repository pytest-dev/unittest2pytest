# required-method: fail

class TestAssertTrue(TestCase):
    def test_me(self):
        self.fail(xxx+y)
        self.fail(aaa % bbb)
        self.fail(ccc or ddd)

    def test_everybody(self):
        self.fail(   'abc'   )

    def test_message(self):
        self.fail(msg='This is wrong!')
        self.fail(error_message)

    def test_nothing(self):
        self.fail()
        self.fail(self.fail())
