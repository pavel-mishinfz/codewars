import unittest
from .solution import high


class TestHighestScoringWord(unittest.TestCase):
    def test_one_highest_scoring_word(self):
        self.assertEqual(high('man i need a taxi up to ubud'), 'taxi')
        self.assertEqual(high('what time are we climbing up the volcano'), 'volcano')

    def test_many_highest_scoring_word(self):
        self.assertEqual(high('take kanymes me to semynak'), 'kanymes')
        self.assertEqual(high('aa b'), 'aa')
        self.assertEqual(high('b aa'), 'b')
