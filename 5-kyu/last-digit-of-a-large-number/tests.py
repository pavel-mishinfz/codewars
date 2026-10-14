import unittest
from .solution import last_digit


class TestLastDigitOfALargeNumber(unittest.TestCase):
    def test_zero_degree(self):
        for x in range(10):
            self.assertEqual(last_digit(x, 0), 1)

    def test_small_numbers(self):
        self.assertEqual(last_digit(4, 1), 4)
        self.assertEqual(last_digit(4, 2), 6)
        self.assertEqual(last_digit(9, 7), 9)
        self.assertEqual(last_digit(467, 124), 1)
        self.assertEqual(last_digit(10, 10 ** 10), 0)

    def test_large_numbers(self):
        self.assertEqual(last_digit(2 ** 200, 2 ** 300), 6)
        self.assertEqual(
            last_digit(
                3715290469715693021198967285016729344580685479654510946723,
                68819615221552997273737174557165657483427362207517952651
            ), 7)
