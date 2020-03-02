import unittest

from src.Domain.Entities.Board import Board
from src.Domain.Entities.Game import Game
from src.Domain.Entities.Pawn import Pawn
from src.Domain.Entities.Piece import Color
from src.Domain.Entities.PieceFactory import PieceFactory


class TestBoard(unittest.TestCase):
    def test_next_turn(self):
        rows = 9
        columns = 9
        board = Board(rows, columns)
        game = Game(board, PieceFactory())
        game.start_game()
        self.assertEqual(1, game.get_turn())
        self.assertEqual(Color.WHITE, game.get_current_player())

        game.next_turn()
        self.assertEqual(2, game.get_turn())
        self.assertEqual(Color.BLACK, game.get_current_player())

        game.next_turn()
        self.assertEqual(3, game.get_turn())
        self.assertEqual(Color.WHITE, game.get_current_player())

    def test_add_captured(self):
        rows = 9
        columns = 9
        board = Board(rows, columns)
        game = Game(board, PieceFactory())
        game.start_game()
        self.assertEqual([], game.get_captured_by_color(Color.WHITE))
        self.assertEqual([], game.get_captured_by_color(Color.BLACK))

        pawn = Pawn(Color.BLACK)
        game.add_captured(Color.WHITE, pawn)
        self.assertEqual([pawn], game.get_captured_by_color(Color.WHITE))
        self.assertEqual([], game.get_captured_by_color(Color.BLACK))


if __name__ == '__main__':
    unittest.main()
