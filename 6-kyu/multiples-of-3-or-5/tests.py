import unittest
from .solution import solution as sum_multiples_three_or_five


class TestMultiples3Or5(unittest.TestCase):
    def test_number_zero(self):
        self.assertEqual(sum_multiples_three_or_five(0), 0)

    def test_number_negative(self):
        self.assertEqual(sum_multiples_three_or_five(-99), 0)

    def test_number_equal_3_or_5(self):
        self.assertEqual(sum_multiples_three_or_five(3), 0)
        self.assertEqual(sum_multiples_three_or_five(5), 3)

    def test_various_number(self):
        self.assertEqual(sum_multiples_three_or_five(4), 3)
        self.assertEqual(sum_multiples_three_or_five(6), 8)
        self.assertEqual(sum_multiples_three_or_five(16), 60)
        self.assertEqual(sum_multiples_three_or_five(15), 45)
        self.assertEqual(sum_multiples_three_or_five(10), 23)
        self.assertEqual(sum_multiples_three_or_five(20), 78)
        self.assertEqual(sum_multiples_three_or_five(200), 9168)
