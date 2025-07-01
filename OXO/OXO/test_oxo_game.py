import unittest
from oxo_logic import Game

class TestTicTacToeGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_initial_board_is_empty(self):
        self.assertEqual(self.game.board, [" "] * 9)

    def test_user_move_marks_board(self):
        self.game.user_move(0)
        self.assertEqual(self.game.board[0], "X")

    def test_invalid_user_move_raises_error(self):
        self.game.board[0] = "X"
        with self.assertRaises(ValueError):
            self.game.user_move(0)

    def test_computer_move_places_O(self):
        self.game.computer_move()
        self.assertIn("O", self.game.board)

    def test_winning_move_detection(self):
        self.game.board = ["X", "X", " ", " ", " ", " ", " ", " ", " "]
        self.game.user_move(2)
        self.assertEqual(self.game.result, "X")

    def test_draw_detection(self):
        self.game.board = ["X", "O", "X",
                           "X", "O", "O",
                           "O", "X", " "]
        self.game.computer_move()  # Last move will fill the board
        self.assertEqual(self.game.result, "D")

if __name__ == '__main__':
    unittest.main()
