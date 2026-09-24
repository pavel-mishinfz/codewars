import unittest
from .solution import sort_array


class TestSortTheOdd(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_array_with_only_odd_numbers(self):
        self.assertEqual(sort_array([7]), [7])
        self.assertEqual(sort_array([7, 1]), [1, 7])
        self.assertEqual(sort_array([1, 3, 5, 7]), [1, 3, 5, 7])
        self.assertEqual(sort_array([7, 5, 3, 1]), [1, 3, 5, 7])
        self.assertEqual(sort_array([7, 7, 7, 7]), [7, 7, 7, 7])
        self.assertEqual(sort_array([-1, 7, -15, 9]), [-15, -1, 7, 9])

    def test_array_with_odd_and_even_numbers(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4, 11]), [1, 3, 2, 8, 5, 4, 11])
        self.assertEqual(sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),[1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        self.assertEqual(sort_array([0, 1, 2, 3, 4, 9, 8, 7, 6, 5]),[0, 1, 2, 3, 4, 5, 8, 7, 6, 9])
        self.assertEqual(sort_array([-5, 3, 2, -8, 0, -11, 1]), [-11, -5, 2, -8, 0, 1, 3])
