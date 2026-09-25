import unittest
from .solution import order


class TestYourOrderPlease(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(order(""), "")

    def test_same_words(self):
        self.assertEqual(order("Test3 Test5 T1est Tes2t 4Test"), "T1est Tes2t Test3 4Test Test5")

    def test_simple_sentence(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        self.assertEqual(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
