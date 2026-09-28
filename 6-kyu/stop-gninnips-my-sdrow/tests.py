import unittest
from .solution import spin_words


class TestStopgninnipSMysdroW(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(spin_words("a"), "a")
        self.assertEqual(spin_words("word"), "word")
        self.assertEqual(spin_words("words"), "sdrow")
        self.assertEqual(spin_words("Welcome"), "emocleW")
        self.assertEqual(spin_words("CodeWars"), "sraWedoC")

    def test_multiple_words(self):
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words("This sEnTeNcE is a sentence"), "This EcNeTnEs is a ecnetnes")