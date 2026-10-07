import unittest
from .solution import rot13


class TestRot13(unittest.TestCase):
    def test_lower_case(self):
        self.assertEqual(rot13('test'), 'grfg')

    def test_upper_case(self):
        self.assertEqual(rot13('TEST'), 'GRFG')

    def test_lower_and_upper_cases(self):
        self.assertEqual(rot13('aA bB zZ'), 'nN oO mM')

    def test_nonletter(self):
        self.assertEqual(rot13('aA b !@#! B 1234 zZ'), 'nN o !@#! O 1234 mM')