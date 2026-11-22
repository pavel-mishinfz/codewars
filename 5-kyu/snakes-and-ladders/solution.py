LAST_SQUARE = 100


class Player:
    def __init__(self, id):
        self.id = id
        self.square = 0

    def move_to_square(self, n):
        self.square = n


class Game:
    def __init__(self):
        self.player1 = Player(id=1)
        self.player2 = Player(id=2)
        self.transitions = {
            2: 38,
            7: 14,
            8: 31,
            15: 26,
            16: 6,
            21: 42,
            28: 84,
            36: 44,
            46: 25,
            49: 11,
            51: 67,
            62: 19,
            64: 60,
            71: 91,
            74: 53,
            78: 98,
            87: 94,
            89: 68,
            92: 88,
            95: 75,
            99: 80
        }
        self.winner = None
        self.current_player = self.player1

    def move(self, n1, n2):
        if self.winner:
            return f'Game over!'

        new_square = self._calculate_new_square(n1, n2)
        self.current_player.move_to_square(new_square)

        if self.current_player.square == LAST_SQUARE:
            self.winner = self.current_player
            return f'Player {self.current_player.id} Wins!'
        result = f'Player {self.current_player.id} is on square {self.current_player.square}'
        if n1 != n2:
            self._change_player()
        return result

    def _calculate_new_square(self, n1, n2):
        new_square = self.current_player.square + n1 + n2
        if new_square > LAST_SQUARE:
            new_square = LAST_SQUARE - new_square % LAST_SQUARE
        return self.transitions[new_square] if self.transitions.get(new_square) else new_square

    def _change_player(self):
        self.current_player = self.player2 if self.current_player is self.player1 else self.player1


class SnakesLadders:

    def __init__(self):
        self.game = Game()

    def play(self, die1, die2):
        return self.game.move(die1, die2)