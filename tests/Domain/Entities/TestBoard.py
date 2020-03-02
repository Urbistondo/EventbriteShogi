import unittest

from src.Domain.Entities.Board import Board
from src.Domain.Entities.Bishop import Bishop
from src.Domain.Entities.GoldGeneral import GoldGeneral
from src.Domain.Entities.King import King
from src.Domain.Entities.Knight import Knight
from src.Domain.Entities.Lance import Lance
from src.Domain.Entities.Pawn import Pawn
from src.Domain.Entities.Piece import Color
from src.Domain.Entities.PieceFactory import PieceFactory
from src.Domain.Entities.Rook import Rook
from src.Domain.Entities.SilverGeneral import SilverGeneral


class TestBoard(unittest.TestCase):
    def test_init(self):
        rows = 9
        columns = 9
        board = Board(rows, columns)
        self.assertEqual(board.get_rows(), rows)
        self.assertEqual(board.get_columns(), columns)

        self.assertEqual(len(board.get_grid()), rows)
        for i in range(rows):
            self.assertEqual(len(board.get_grid()[i]), columns)

    def test_init_error(self):
        rows = 9
        columns = 0
        with self.assertRaises(ValueError):
            Board(rows, columns)

    def test_create_pieces_white(self):
        rows = 9
        columns = 9
        board = Board(rows, columns)
        board.create_pieces(PieceFactory(), Color.WHITE)

        first_row = 0
        second_row = 1
        third_row = 2

        for square in board.get_grid()[third_row]:
            self.assertIsInstance(square.get_piece(), Pawn)

        self.assertIsInstance(board.get_grid()[second_row][1].get_piece(), Bishop)
        self.assertIsInstance(board.get_grid()[second_row][-2].get_piece(), Rook)
        self.assertIsInstance(board.get_grid()[first_row][0].get_piece(), Lance)
        self.assertIsInstance(board.get_grid()[first_row][-1].get_piece(), Lance)
        self.assertIsInstance(board.get_grid()[first_row][1].get_piece(), Knight)
        self.assertIsInstance(board.get_grid()[first_row][-2].get_piece(), Knight)
        self.assertIsInstance(board.get_grid()[first_row][2].get_piece(), SilverGeneral)
        self.assertIsInstance(board.get_grid()[first_row][-3].get_piece(), SilverGeneral)
        self.assertIsInstance(board.get_grid()[first_row][3].get_piece(), GoldGeneral)
        self.assertIsInstance(board.get_grid()[first_row][-4].get_piece(), GoldGeneral)
        self.assertIsInstance(board.get_grid()[first_row][4].get_piece(), King)

    def test_create_pieces_black(self):
        rows = 9
        columns = 9
        board = Board(rows, columns)
        board.create_pieces(PieceFactory(), Color.BLACK)

        first_row = -1
        second_row = -2
        third_row = -3

        for square in board.get_grid()[third_row]:
            self.assertIsInstance(square.get_piece(), Pawn)

        self.assertIsInstance(board.get_grid()[second_row][1].get_piece(), Bishop)
        self.assertIsInstance(board.get_grid()[second_row][-2].get_piece(), Rook)
        self.assertIsInstance(board.get_grid()[first_row][0].get_piece(), Lance)
        self.assertIsInstance(board.get_grid()[first_row][-1].get_piece(), Lance)
        self.assertIsInstance(board.get_grid()[first_row][1].get_piece(), Knight)
        self.assertIsInstance(board.get_grid()[first_row][-2].get_piece(), Knight)
        self.assertIsInstance(board.get_grid()[first_row][2].get_piece(), SilverGeneral)
        self.assertIsInstance(board.get_grid()[first_row][-3].get_piece(), SilverGeneral)
        self.assertIsInstance(board.get_grid()[first_row][3].get_piece(), GoldGeneral)
        self.assertIsInstance(board.get_grid()[first_row][-4].get_piece(), GoldGeneral)
        self.assertIsInstance(board.get_grid()[first_row][4].get_piece(), King)

    def test_is_square_empty(self):
        rows = 9
        columns = 9
        board = Board(rows, columns)

        self.assertTrue(board.is_square_empty(0, 0))

    def test_is_square_not_empty(self):
        rows = 9
        columns = 9
        board = Board(rows, columns)
        board.create_pieces(PieceFactory(), Color.WHITE)

        self.assertFalse(board.is_square_empty(0, 0))

    def test_is_square_occupied_by_friendly(self):
        rows = 9
        columns = 9
        board = Board(rows, columns)
        board.create_pieces(PieceFactory(), Color.WHITE)

        self.assertTrue(board.is_square_occupied_by_friendly(0, 0, Color.WHITE))

    def test_is_square_occupied_by_enemy(self):
        rows = 9
        columns = 9
        board = Board(rows, columns)
        board.create_pieces(PieceFactory(), Color.WHITE)

        self.assertTrue(board.is_square_occupied_by_enemy(0, 0, Color.BLACK))

    def test_get_piece_in_square(self):
        rows = 9
        columns = 9
        board = Board(rows, columns)
        board.create_pieces(PieceFactory(), Color.WHITE)

        piece = Pawn(Color.WHITE)
        board.get_grid()[0][0].set_piece(piece)

        self.assertEqual(board.get_piece_in_square(0, 0), piece)


if __name__ == '__main__':
    unittest.main()
