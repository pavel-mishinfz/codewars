import unittest
from .solution import is_valid_walk


class TestTakeTenMinutesWalk(unittest.TestCase):
    def test_short_walk(self):
        self.assertEqual(is_valid_walk(['w', 'e']), False)
        self.assertEqual(is_valid_walk(['n', 's', 'w', 'e']), False)

    def test_long_walk(self):
        self.assertEqual(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), False)

    def test_walk_no_return_to_start(self):
        self.assertEqual(is_valid_walk(['n','n','n','s','n','s','n','s','n','w']), False)

    def test_valid_walk(self):
        self.assertEqual(is_valid_walk(['w','w','s','s','s','n','e','n','n','e']), True)