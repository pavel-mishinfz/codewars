import unittest
from .solution import dir_reduc


class TestDirectionsReduction(unittest.TestCase):
    def test_empty_arr(self):
        self.assertEqual(dir_reduc([]), [])

    def test_without_reduction(self):
        self.assertEqual(dir_reduc(['NORTH']), ['NORTH'])
        self.assertEqual(dir_reduc(['NORTH', 'WEST']), ['NORTH', 'WEST'])
        self.assertEqual(dir_reduc(['NORTH', 'WEST', 'SOUTH', 'EAST']), ['NORTH', 'WEST', 'SOUTH', 'EAST'])

    def test_reduction_to_empty_arr(self):
        self.assertEqual(dir_reduc(['NORTH','SOUTH','SOUTH','EAST','WEST','NORTH']), [])
        
    def test_basic_reduction(self):
        self.assertEqual(
            dir_reduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']),
            ['WEST']
        )
        self.assertEqual(
            dir_reduc(['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']),
            ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH']
        )
        self.assertEqual(
            dir_reduc(['EAST', 'EAST', 'WEST', 'NORTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'NORTH', 'WEST']),
            ['EAST', 'NORTH']
        )


