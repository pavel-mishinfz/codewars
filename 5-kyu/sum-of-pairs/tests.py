import unittest
from .solution import sum_pairs


class TestSumOfPairs(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sum_pairs([1, 4, 8, 7, 3, 15], 8), [1, 7])

    def test_negative_nums(self):
        self.assertEqual(sum_pairs([1, -2, 3, 0, -6, 1], -6), [0, -6])

    def test_no_match(self):
        self.assertEqual(sum_pairs([20, -13, 40], -7), None)

    def test_first_match_from_left(self):
        self.assertEqual(sum_pairs([1, 2, 3, 4, 1, 0], 2), [1, 1])
        self.assertEqual(sum_pairs([10, 5, 2, 3, 7, 5], 10), [3, 7])

    def test_duplicates(self):
        self.assertEqual(sum_pairs([4, -2, 3, 3, 4], 8), [4, 4])
        
    def test_zeros(self):
        self.assertEqual(sum_pairs([0, 2, 0], 0), [0, 0])
        
    def test_subtraction(self):
        self.assertEqual(sum_pairs([5, 9, 13, -3], 10), [13, -3])
        
    def test_large_list(self):
        arr = [1] * 10000000
        arr[len(arr) // 2 - 1] = 6
        arr[len(arr) // 2] = 7
        arr[len(arr) - 2] = 8
        arr[len(arr) - 1] = -3
        arr[0] = 13
        arr[1] = 3
        
        self.assertEqual(sum_pairs(arr, 13), [6, 7])
        self.assertEqual(sum_pairs(arr, 5), [8, -3])
        self.assertEqual(sum_pairs(arr, 16), [13, 3])
        self.assertEqual(sum_pairs(arr, 31), None)