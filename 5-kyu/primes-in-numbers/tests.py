import unittest
from .solution import prime_factors


class TestPrimesInNumbers(unittest.TestCase):
    def test_composite_number(self):
        self.assertEqual(prime_factors(7775460), '(2**2)(3**3)(5)(7)(11**2)(17)')

    def test_prime_number(self):
        self.assertEqual(prime_factors(7919), '(7919)')
