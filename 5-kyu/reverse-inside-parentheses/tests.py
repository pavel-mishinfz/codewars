import unittest
from .solution import reverse_in_parentheses


class TestReverseInsideParentheses(unittest.TestCase):
    def test_str_without_brackets(self):
        self.assertEqual(reverse_in_parentheses(''), '')
        self.assertEqual(reverse_in_parentheses('hello'), 'hello')

    def test_str_without_nested_brackets(self):
        self.assertEqual(reverse_in_parentheses('h(el)lo (world)'), 'h(le)lo (dlrow)')

    def test_str_with_nested_brackets(self):
        self.assertEqual(reverse_in_parentheses('a ((d e) c b)'), 'a (b c (d e))')
        self.assertEqual(reverse_in_parentheses("one (two (three) four)"), "one (ruof (three) owt)")
        self.assertEqual(reverse_in_parentheses("one (ruof ((rht)ee) owt)"), "one (two ((thr)ee) four)")
