import unittest

from main import rearrangeWord, list_to_string

class Test(unittest.TestCase):
    def test_case1(self):
        """ Check if rearrangeWord() operates as expected """
        self.assertEqual(rearrangeWord("baca"), "bcaa")
    def test_case2(self):
        """ Check if rearrangeWord() operates as expected """
        self.assertNotEqual(rearrangeWord("xyz"), "zyx")
    def test_case3(self):
        """ Check if rearrangeWord() operates as expected """
        self.assertNotEqual(rearrangeWord("pp"), "qp")
    def test_case4(self):
        """ Check if list_to_string() operates as expected """
        self.assertEqual(list_to_string(['foo ','bar ','boo']), "foo bar boo")


if __name__ == "__main__":
    unittest.main()