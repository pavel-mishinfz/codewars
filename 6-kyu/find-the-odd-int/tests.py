import unittest
from .solution import find_it


class TestFindTheOddInt(unittest.TestCase):
    def test_one_number(self):
        self.assertEqual(find_it([10]), 10)
        self.assertEqual(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1)

    def test_same_numbers(self):
        self.assertEqual(find_it([10, 10, 10]), 10)
        self.assertEqual(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10)
        
    def test_negative_and_positive_numbers(self):
        self.assertEqual(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)
        self.assertEqual(find_it([1,1,2,-2,5,2,-4,-4,5,-2,1]), 1)
        self.assertEqual(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
