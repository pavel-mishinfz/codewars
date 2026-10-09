import unittest
from .solution import score


class TestGreedIsGood(unittest.TestCase):
    def test_zero_score(self):
        self.assertEqual(score([2, 3, 4, 6, 2]), 0)

    def test_jackpot(self):
        self.assertEqual(score([1, 1, 1, 1, 1]), 1200)

    def test_various_combs(self):
        self.assertEqual(score([5, 1, 3, 4, 1]), 250)
        self.assertEqual(score([1, 1, 1, 3, 1]), 1100)
        self.assertEqual(score([4, 4, 4, 3, 3]), 400)
        self.assertEqual(score([2, 4, 4, 5, 4]), 450)