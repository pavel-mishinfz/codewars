import unittest
from .solution import valid_braces


class TestValidBraces(unittest.TestCase):
    def test_valid_braces(self):
        self.assertEqual(valid_braces("()"), True)
        self.assertEqual(valid_braces("[]"), True)
        self.assertEqual(valid_braces("{}"), True)
        self.assertEqual(valid_braces("{}()[]"), True)
        self.assertEqual(valid_braces("([{}])"), True)
        self.assertEqual(valid_braces("{}({})[]"), True)
        self.assertEqual(valid_braces("(({{[[]]}}))"), True)

    def test_invalid_braces(self):
        self.assertEqual(valid_braces("(}"), False)
        self.assertEqual(valid_braces("[(])"), False)
        self.assertEqual(valid_braces("([}{])"), False)
        self.assertEqual(valid_braces("(((({{"), False)
        self.assertEqual(valid_braces(")(}{]["), False)
        self.assertEqual(valid_braces("())({}}{()][]["), False)
