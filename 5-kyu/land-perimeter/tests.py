import unittest
from .solution import land_perimeter


class TestLandPerimeter(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(land_perimeter(['']), 'Total land perimeter: 0')
        self.assertEqual(land_perimeter(['OOOOO', 'OOOOO', 'OOOOO']), 'Total land perimeter: 0')

    def test_without_water(self):
        self.assertEqual(land_perimeter(['XXXXX', 'XXXXX', 'XXXXX']), 'Total land perimeter: 16')

    def test_islands(self):
        self.assertEqual(
            land_perimeter(
                ['OXOOOX', 'OXOXOO', 'XXOOOX', 'OXXXOO', 'OOXOOX', 'OXOOOO', 'OOXOOX', 'OOXOOO', 'OXOOOO', 'OXOOXX']
            ),
            'Total land perimeter: 60'
        )
        self.assertEqual(
            land_perimeter(
                ['OXOOO', 'OOXXX', 'OXXOO', 'XOOOO', 'XOOOO', 'XXXOO', 'XOXOO', 'OOOXO', 'OXOOX', 'XOOOO', 'OOOXO']
            ),
            'Total land perimeter: 52'
        )