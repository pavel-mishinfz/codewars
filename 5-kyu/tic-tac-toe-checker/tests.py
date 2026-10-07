import unittest
from .solution import is_solved


class TestTicTacToeChecker(unittest.TestCase):
    def test_not_yet_finished(self):
        board = [[0, 0, 1],
                 [0, 1, 2],
                 [2, 1, 0]]
        self.assertEqual(is_solved(board), -1)

    def test_draw(self):
        board = [[2, 1, 2],
                 [2, 1, 1],
                 [1, 2, 1]]
        self.assertEqual(is_solved(board), 0)

    def test_X_winner(self):
        board = [[1, 1, 1],
                 [0, 2, 2],
                 [0, 0, 0]]
        self.assertEqual(is_solved(board), 1)

        board = [[1, 2, 1],
                 [0, 1, 2],
                 [0, 0, 1]]
        self.assertEqual(is_solved(board), 1)

        board = [[1, 2, 1],
                 [0, 2, 1],
                 [0, 0, 1]]
        self.assertEqual(is_solved(board), 1)

    def test_O_winner(self):
        board = [[1, 2, 1],
                 [2, 2, 2],
                 [0, 1, 0]]
        self.assertEqual(is_solved(board), 2)

        board = [[1, 2, 2],
                 [1, 2, 1],
                 [2, 1, 0]]
        self.assertEqual(is_solved(board), 2)

        board = [[2, 2, 1],
                 [2, 1, 2],
                 [2, 1, 0]]
        self.assertEqual(is_solved(board), 2)
