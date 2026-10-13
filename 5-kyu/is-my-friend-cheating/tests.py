import unittest
from .solution import remov_nb


class TestIsMyFriendCheating(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remov_nb(26), [(15, 21), (21, 15)])
        self.assertEqual(remov_nb(100), [])
        self.assertEqual(remov_nb(101), [(55, 91), (91, 55)])
