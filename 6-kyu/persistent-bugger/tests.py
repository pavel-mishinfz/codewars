import unittest
from .solution import persistence


class TestPersistentBugger(unittest.TestCase):
    def test_number_lte_10(self):
        self.assertEqual(persistence(0), 0)
        self.assertEqual(persistence(4), 0)
        self.assertEqual(persistence(10), 1)

    def test_number_gt_10(self):
        self.assertEqual(persistence(39), 3)
        self.assertEqual(persistence(25), 2)
        self.assertEqual(persistence(999), 4)

    def test_large_number(self):
        self.assertEqual(persistence(10000000000000000), 1)
        self.assertEqual(persistence(10000000900000000), 1)
        self.assertEqual(persistence(9999999999999999999), 2)
        self.assertEqual(persistence(6178234728542782344), 2)
