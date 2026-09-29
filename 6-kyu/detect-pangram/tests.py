import unittest
from .solution import is_pangram


class TestDetectPangram(unittest.TestCase):
    def test_pangrams(self):
        pangrams = ["The quick brown fox jumps over the lazy dog.",
                    "Cwm fjord bank glyphs vext quiz",
                    "Pack my box with five dozen liquor jugs.",
                    "How quickly daft jumping zebras vex.",
                    "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"]
        for pangram in pangrams:
            self.assertEqual(is_pangram(pangram), True)

    def test_non_pangrams(self):
        non_pangrams = ["This isn't a pangram!",
                        "abcdefghijklm opqrstuvwxyz",
                        "Aacdefghijklmnopqrstuvwxyz"]
        for non_pangram in non_pangrams:
            self.assertEqual(is_pangram(non_pangram), False)
