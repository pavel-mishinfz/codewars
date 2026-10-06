import unittest
from .solution import increment_string


class TestStringIncrementer(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(increment_string(''), '1')

    def test_string_without_digits(self):
        self.assertEqual(increment_string('foo'), 'foo1')

    def test_string_with_one_digit(self):
        self.assertEqual(increment_string('foo1'), 'foo2')

    def test_string_with_zeros(self):
        self.assertEqual(increment_string('foobar00'), 'foobar01')
        self.assertEqual(increment_string('foobar001'), 'foobar002')
        self.assertEqual(increment_string('foobar0001230000000003459'), 'foobar0001230000000003460')

    def test_string_with_new_numeric_digit(self):
        self.assertEqual(increment_string('foo9'), 'foo10')
        self.assertEqual(increment_string('foobar099'), 'foobar100')
        self.assertEqual(increment_string('foo99999'), 'foo100000')
