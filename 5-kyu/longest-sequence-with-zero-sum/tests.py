import unittest
from .solution import max_zero_sequence


class TestLongestSequenceWithZeroSum(unittest.TestCase):
    def test_one_sequence(self):
        self.assertEqual(max_zero_sequence([1, 2, -3, 7, 8, -16]), [1, 2, -3])

    def test_some_sequences(self):
        self.assertEqual(
            max_zero_sequence([25, -35, 12, 6, 92, -115, 17, 2, 2, 2, -7, 2, -9, -2, 2, -11]),
            [92, -115, 17, 2, 2, 2]
        )
        self.assertEqual(
            max_zero_sequence([25, -35, 12, 6, 92, -115, 17, 2, 2, 2, 7, 9, -9, 3, 12, -11, -4]),
            [9, -9, 3, 12, -11, -4]
        )