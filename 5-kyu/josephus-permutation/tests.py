import unittest
from .solution import josephus


class TestJosephusPermutation(unittest.TestCase):
    def test_simple_arr(self):
        self.assertEqual(josephus([],3),[])
        self.assertEqual(josephus([1],3),[1])
        self.assertEqual(josephus([1,2],3),[1,2])
        self.assertEqual(josephus([1,2,3],3),[3,1,2])

    def test_only_digits(self):
        self.assertEqual(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [2, 4, 6, 8, 10, 3, 7, 1, 9, 5])
        self.assertEqual(josephus([1, 2, 3, 4, 5, 6, 7], 3), [3, 6, 2, 7, 5, 1, 4])

    def test_only_chars(self):
        self.assertEqual(josephus(["C","o","d","e","W","a","r","s"],4),['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])

    def test_only_bool(self):
        self.assertEqual(josephus([True, False, False, True, False, True, True], 8), [True, False, True, False, False, True, True])