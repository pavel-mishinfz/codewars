import unittest
from .solution import find_uniq


class TestFindUniqueNumber(unittest.TestCase):
    def test_small_array(self):
        self.assertEqual(find_uniq([1,1,1,1,1,4,1,1,1]), 4)
        self.assertEqual(find_uniq([0,0,0,0.55,0,0]), 0.55)
        self.assertEqual(find_uniq([5,-3,-3,-3,-3,-3]), 5)
        self.assertEqual(find_uniq([99,99,99,-7,99]), -7)

    def test_huge_array(self):
        from random import randint

        unique_item = randint(-1000, 1000)
        unique_item_at_start = [unique_item]
        unique_item_at_start.extend([randint(-1000, 1000)] * 1000000)
        self.assertEqual(find_uniq(unique_item_at_start), unique_item)

        unique_item = randint(-1000, 1000)
        unique_item_at_end = [randint(-1000, 1000)] * 1000000
        unique_item_at_end.append(unique_item)
        self.assertEqual(find_uniq(unique_item_at_end), unique_item)

        unique_item = randint(-1000, 1000)
        base_item = randint(-1000, 1000)
        left_part = [base_item] * 300000
        right_part = [base_item] * 700000
        unique_item_at_middle = left_part + [unique_item] + right_part
        self.assertEqual(find_uniq(unique_item_at_middle), unique_item)