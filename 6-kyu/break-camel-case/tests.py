import unittest
from .solution import solution as break_camel_case


class TestBreakCamelCase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(break_camel_case(''), '')

    def test_one_word(self):
        self.assertEqual(break_camel_case('identifier'), 'identifier')
        
    def test_any_words(self):
        self.assertEqual(break_camel_case('helloWorld'), 'hello World')
        self.assertEqual(break_camel_case('breakCamelCase'), 'break Camel Case')
        self.assertEqual(break_camel_case('lAsTtEsTcasE'), 'l As Tt Es Tcas E')