import unittest
from .solution import duplicate_encode


class TestDuplicateEncoder(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(duplicate_encode(""),"")

    def test_string_with_same_characters(self):
        self.assertEqual(duplicate_encode("sssss"),")))))")
        self.assertEqual(duplicate_encode("asssssaa"),"))))))))")

    def test_string_with_unique_characters(self):
        self.assertEqual(duplicate_encode("din"),"(((")
        self.assertEqual(duplicate_encode("asssssaa"),"))))))))")

    def test_string_with_capitalizations(self):
        self.assertEqual(duplicate_encode("rEcedE"),"()()()")
        self.assertEqual(duplicate_encode("Success"),")())())")

    def test_string_with_letters_and_brackets(self):
        self.assertEqual(duplicate_encode("Vyh)R(RPSocDJOvc j! gc@FUA@"),")((()()(())())))))()())((()")
        self.assertEqual(duplicate_encode("rlHPQspd )gw(Dz"),"((()(())((((()(")

    def test_string_without_letters(self):
        self.assertEqual(duplicate_encode("(( @"),"))((")
