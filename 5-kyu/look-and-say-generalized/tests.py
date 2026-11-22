import unittest
from .solution import look_say


class TestLookSayGeneralized(unittest.TestCase):
    def test_simple_numbers(self):
        self.assertEqual(look_say(0), 10)
        self.assertEqual(look_say(1), 11)
        self.assertEqual(look_say(21), 1211)
        self.assertEqual(look_say(2014), 12101114)

    def test_multi_digits_numbers(self):
        self.assertEqual(look_say(222222222222), 122)
        self.assertEqual(look_say(33333333333331), 13311)
