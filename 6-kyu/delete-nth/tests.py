import unittest
from .solution import delete_nth


class TestDeleteNth(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(delete_nth([], 5), [])

    def test_repetitions_lte_max_e(self):
        self.assertEqual(delete_nth([1, 1, 1, 1, 1], 5), [1, 1, 1, 1, 1])
        self.assertEqual(delete_nth([1,1,2,2,3,4,4,5,6], 2), [1,1,2,2,3,4,4,5,6])

    def test_delete_from_middle_and_end(self):
        self.assertEqual(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
        self.assertEqual(delete_nth([12, 39, 19, 39, 12, 12, 12, 39, 39, 39, 19, 19], 1), [12, 39, 19])
        self.assertEqual(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3), [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5])
