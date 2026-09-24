import unittest
from .solution import count


class TestCountCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count(''), {})

    def test_same_characters(self):
        self.assertEqual(count('aaaaaa'), {'a': 6})
        self.assertEqual(count('bbbbbbbb'), {'b': 8})

    def test_various_characters(self):
        self.assertEqual(count('aabb'), {'b' : 2, 'a' : 2})
        self.assertEqual(count('aabcccbadc'), {'d': 1, 'c': 4, 'b' : 2, 'a' : 3})
