import unittest


class DowntriangleTests(unittest.TestCase):

    def __init__(self, testname, arg):
        super(DowntriangleTests, self).__init__(testname)
        self.arg = arg

    def test_arg_type_ok(self):
        t = type(int(arg))
        self.assertEqual(t, int)

    def test_arg_is_valid(self):
        value = int(self.arg)
        self.assertTrue(value>=0)



def main():
    unittest.main()

if __name__ == '__main__':
    import sys
    arg = sys.argv[1]

    suite = unittest.TestSuite()
    suite.addTest(DowntriangleTests("test_arg_type_ok", arg))
    suite.addTest(DowntriangleTests("test_arg_is_valid", arg))

    unittest.TextTestRunner().run(suite)