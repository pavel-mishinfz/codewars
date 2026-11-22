import unittest
from .solution import parse_molecule


class TestMoleculeToAtoms(unittest.TestCase):
    def test_without_brackets(self):
        self.assertEqual(parse_molecule('H2O'), {'H': 2, 'O' : 1})

    def test_with_brackets(self):
        self.assertEqual(parse_molecule('Mo(CO)6'), {'Mo': 1, 'C': 6, 'O' : 6})
        self.assertEqual(
            parse_molecule('As2{Be4C5[BCo3(CO2)3]2}4Cu5'),
            {'As': 2,  'Be': 16,  'C': 44,  'B': 8,  'Co': 24,  'O': 48,  'Cu': 5}
        )
