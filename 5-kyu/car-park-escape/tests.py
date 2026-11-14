import unittest
from .solution import escape


class TestCarParkEscape(unittest.TestCase):
    def test_only_one_level(self):
        carpark = [[2, 0, 0, 0, 0]]
        result = ['R4']
        self.assertEqual(escape(carpark), result)

        carpark = [[0, 0, 0, 0, 2]]
        result = []
        self.assertEqual(escape(carpark), result)

    def test_more_than_one_level(self):
        carpark = [[1, 0, 0, 0, 2],
                   [0, 0, 0, 0, 0]]
        result = ["L4", "D1", "R4"]
        self.assertEqual(escape(carpark), result)

        carpark = [[1, 0, 0, 0, 2],
                   [0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]]
        result = ["L4", "D1", "R4", "D1", "L4", "D1", "R4"]
        self.assertEqual(escape(carpark), result)

        carpark = [[2, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0]]
        result = ["R3", "D2", "R1"]
        self.assertEqual(escape(carpark), result)

        carpark = [[0, 2, 0, 0, 1],
                   [0, 0, 0, 0, 1],
                   [0, 0, 0, 0, 1],
                   [0, 0, 0, 0, 0]]
        result = ["R3", "D3"]
        self.assertEqual(escape(carpark), result)
