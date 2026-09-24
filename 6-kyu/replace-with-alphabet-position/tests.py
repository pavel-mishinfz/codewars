import unittest
from .solution import alphabet_position


class TestReplaceWithAlphabetPosition(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(alphabet_position(''), '')

    def test_long_strings(self):
        self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
        
    def test_strings_with_special_symbols_and_digits(self):
        self.assertEqual(alphabet_position("The,,, sunset$ se%ts at tw!elv@###e o' cloc*&k."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(alphabet_position("The narw12223hal bacons45&&$ at midnig9901h@@t."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
