import unittest

from src.Domain.Pieces.Pawn import Pawn
from src.Domain.Pieces.Piece import Color


class TestPawn(unittest.TestCase):
    COLORS = {
        Color.WHITE: {
            'description': 'Whites',
            'symbol': 'v'
        },
        Color.BLACK: {
            'description': 'Blacks',
            'symbol': '^'
        },
    }

    PIECE_DESCRIPTION = 'Pawn'
    PIECE_REPRESENTATION = 'P'

    def test_init(self):
        piece = Pawn(Color.WHITE)
        assert piece.description == self.PIECE_DESCRIPTION
        assert piece.representation == self.PIECE_REPRESENTATION
        assert piece.color == Color.WHITE
        assert piece.symbol == self.COLORS[Color.WHITE]['symbol']

    def test_can_reach(self):
        piece = Pawn(Color.WHITE)

        self.assertTrue(piece.can_reach(1, 1, 2, 1, piece.get_color()))

    def test_can_reach_false(self):
        piece = Pawn(Color.WHITE)

        self.assertFalse(piece.can_reach(1, 1, 1, 1, piece.get_color()))
        self.assertFalse(piece.can_reach(1, 1, 0, 1, piece.get_color()))
        self.assertFalse(piece.can_reach(1, 1, 0, 0, piece.get_color()))
        self.assertFalse(piece.can_reach(1, 1, 1, 0, piece.get_color()))
        self.assertFalse(piece.can_reach(1, 1, 2, 0, piece.get_color()))
        self.assertFalse(piece.can_reach(1, 1, 2, 2, piece.get_color()))
        self.assertFalse(piece.can_reach(1, 1, 1, 2, piece.get_color()))
        self.assertFalse(piece.can_reach(1, 1, 0, 1, piece.get_color()))


if __name__ == '__main__':
    unittest.main()
