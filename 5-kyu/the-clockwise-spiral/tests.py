import unittest
from .solution import create_spiral


class TestTheClockwiseSpiral(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(create_spiral(0), [])
        self.assertEqual(create_spiral(1), [[1]])

    def test_size_gte_3(self):
        self.assertEqual(create_spiral(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
        self.assertEqual(create_spiral(4), [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
        self.assertEqual(
            create_spiral(5),
            [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
        )
