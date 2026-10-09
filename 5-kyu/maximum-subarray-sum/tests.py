import unittest
from .solution import max_sequence


class TestMaximumSubarraySum(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(max_sequence([]), 0)

    def test_array_with_one_item(self):
        self.assertEqual(max_sequence([5]), 5)

    def test_array_with_only_negative_item(self):
        self.assertEqual(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)

    def test_array_with_only_positive_item(self):
        self.assertEqual(
            max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]),
            155
        )

    def test_array_with_pos_and_neg_items(self):
        self.assertEqual(max_sequence([-5, 9, -3]), 9)
        self.assertEqual(max_sequence([1, -5, 1]), 1)
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_large_array(self):
        large_arr = [0]*10000 + [1]*500 + [-99]*1000 + [0]*5000 + [1]*1000 + [0]*5000
        self.assertEqual(max_sequence(large_arr), 1000)
