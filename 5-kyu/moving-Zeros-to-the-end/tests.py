import unittest
from .solution import move_zeros


class TestMovingZerosToTheEnd(unittest.TestCase):
    def test_empty_lst(self):
        self.assertEqual(move_zeros([]), [])

    def test_lst_without_changes(self):
        self.assertEqual(move_zeros([0]), [0])
        self.assertEqual(move_zeros([0, 0]), [0, 0])
        self.assertEqual(move_zeros([1, 2, 1, 1, 3, 1]), [1, 2, 1, 1, 3, 1])

    def test_lst_requires_moving_zeros(self):
        self.assertEqual(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
        )
        self.assertEqual(
            move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )
