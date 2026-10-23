import unittest
from .solution import gap


class TestRot13(unittest.TestCase):
    def test_not_gap(self):
        self.assertEqual(gap(6,100,110), None)

    def test_small_numbers(self):
        self.assertEqual(gap(2, 100, 110), [101, 103])
        self.assertEqual(gap(4, 100, 110), [103, 107])
        self.assertEqual(gap(8, 300, 400), [359, 367])
        self.assertEqual(gap(10, 300, 400), [337, 347])
        self.assertEqual(gap(2, 100, 103), [101, 103])

    def test_big_numbers(self):
        self.assertEqual(gap(2, 59800, 159800), [60089, 60091])
        self.assertEqual(gap(4, 59800, 159800), [60013, 60017])
        self.assertEqual(gap(2,926743,1026743), [927629, 927631])
        self.assertEqual(gap(8, 926743, 1026743), [926843, 926851])