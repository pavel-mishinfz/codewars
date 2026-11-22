import unittest
from .solution import moving_shift, demoving_shift


class TestFirstVariationOnCaesarCipher(unittest.TestCase):
    def test_small_shift(self):
        self.assertEqual(
            moving_shift("I should have known that you would have a perfect answer for me!!!", 1),
            ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]
        )
        self.assertEqual(
            demoving_shift(["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"], 1),
            "I should have known that you would have a perfect answer for me!!!"
        )

    def test_large_shift(self):
        self.assertEqual(
            moving_shift("Every decision that we make leads us down a different road.", 35),
            ['Nfpdl sutalc', 'jj rgau zi s', 'hsn wqnrh lk', ' xjsk z ekij', 'jxlvc canr.']
        )
        self.assertEqual(
            demoving_shift(['Nfpdl sutalc', 'jj rgau zi s', 'hsn wqnrh lk', ' xjsk z ekij', 'jxlvc canr.'], 35),
            "Every decision that we make leads us down a different road."
        )