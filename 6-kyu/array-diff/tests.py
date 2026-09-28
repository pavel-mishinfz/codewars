import unittest
from .solution import array_diff


class TestArrayDiff(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(array_diff([], [1,2]), [])
        self.assertEqual(array_diff([1,2,3], []), [1,2,3])

    def test_list_with_duplicates(self):
        self.assertEqual(array_diff([1,2,2,3,3,3,3], [1]), [2,2,3,3,3,3])
        self.assertEqual(array_diff([1,2,2,3,3,3,3,4,5], [1,3,5]), [2,2,4])

    def test_list_with_unique_items(self):
        self.assertEqual(array_diff([1,2,4,-155,0,77,-99], [4,0,-99]), [1,2,-155,77])
