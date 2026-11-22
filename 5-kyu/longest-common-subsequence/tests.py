import unittest
from .solution import lcs


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(lcs("", ""), "")
        self.assertEqual(lcs("", "b"), "")
        self.assertEqual(lcs("a", "b"), "")

    def test_unique(self):
        self.assertEqual(lcs('abcde', 'ace'), 'ace')

    def test_not_unique(self):
        self.assertEqual(lcs("anothertest", "notatest"), "nottest")
        self.assertEqual(lcs("finaltest", "zzzfinallyzzz"), "final")

    def test_digits(self):
        self.assertEqual(lcs("132535365", "123456789"), "12356")
