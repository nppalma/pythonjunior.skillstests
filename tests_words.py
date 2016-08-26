import unittest
import words
import os.path


class WordsTests(unittest.TestCase):

    def __init__(self, testname, arg):
        super(WordsTests, self).__init__(testname)
        self.arg = arg
        self.w = words.words(arg)

    def test_path_arg_exist(self):
        self.assertTrue(os.path.exists(arg))

    def test_file_name_ok(self):
        self.assertEqual(self.arg, "myfile.txt")

    def test_words_list_ok(self):
        l2 = ['Lorem', 'ipsum', 'dolor']
        self.assertEqual(self.w,l2)


def main():
    unittest.main()

if __name__ == '__main__':
    import sys
    arg = sys.argv[1]

    suite = unittest.TestSuite()
    suite.addTest(WordsTests("test_words_list_ok", arg))
    suite.addTest(WordsTests("test_path_arg_exist", arg))
    suite.addTest(WordsTests("test_file_name_ok", arg))

    unittest.TextTestRunner().run(suite)