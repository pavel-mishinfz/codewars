import unittest
from .solution import unique_in_order


class TestUniqueInOrder(unittest.TestCase):
    def test_empty_sequence(self):
        self.assertEqual(unique_in_order(""), [])
        self.assertEqual(unique_in_order([]), [])
        self.assertEqual(unique_in_order(()), [])

    def test_sequence_with_single_item(self):
        self.assertEqual(unique_in_order("A"), ["A"])
        self.assertEqual(unique_in_order(["A"]), ["A"])
        self.assertEqual(unique_in_order(("A",)), ["A"])

    def test_sequence_with_same_items(self):
        self.assertEqual(unique_in_order("AA"), ["A"])
        self.assertEqual(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])

    def test_sequence_lower_case(self):
        self.assertEqual(unique_in_order("ABBCcA"), ["A", "B", "C", "c", "A"])

    def test_sequence_with_different_item_types(self):
        self.assertEqual(unique_in_order([1, -2, 3, 3, -1, -1, "ABC", "ABC", "AbC", -7]), [1, -2, 3, -1, "ABC", "AbC", -7])
        self.assertEqual(unique_in_order(["a", "b", "b", 5, 5, 5, "a", 6, -3, -3]), ["a", "b", 5, "a", 6, -3])
