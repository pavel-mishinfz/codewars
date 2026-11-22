import unittest
from .solution import SnakesLadders


game = SnakesLadders()

class TestSnakesAndLadders(unittest.TestCase):
    def test_full_game(self):
        self.assertEqual(game.play(1, 1), "Player 1 is on square 38")
        self.assertEqual(game.play(6, 4), "Player 1 is on square 48")
        self.assertEqual(game.play(4, 2), "Player 2 is on square 6")
        self.assertEqual(game.play(2, 1), "Player 1 is on square 67")
        self.assertEqual(game.play(1, 1), "Player 2 is on square 31")
        self.assertEqual(game.play(3, 5), "Player 2 is on square 39")
        self.assertEqual(game.play(6, 5), "Player 1 is on square 98")
        self.assertEqual(game.play(1, 2), "Player 2 is on square 42")
        self.assertEqual(game.play(3, 3), "Player 1 is on square 96")
        self.assertEqual(game.play(1, 3), "Player 1 Wins!")
        self.assertEqual(game.play(5, 6), "Game over!")
