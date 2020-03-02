import unittest

from src.Domain.Pieces.Pawn import Pawn
from src.Domain.Pieces.Piece import Color


class TestBishop(unittest.TestCase):
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

    PAWN_DESCRIPTION = 'Pawn'
    PAWN_REPRESENTATION = 'P'

    def test_init(self):
        pawn = Pawn(Color.WHITE)
        assert pawn.description == 'Pawn'
        assert pawn.representation == 'P'
        assert pawn.color == Color.WHITE
        assert pawn.symbol == self.COLORS[Color.WHITE]['symbol']

    def test_can_reach(self):
        pawn = Pawn(Color.WHITE)
        self.assertTrue(pawn.can_reach(1, 1, 2, 1, pawn.get_color()))

    def test_can_reach_false(self):
        pawn = Pawn(Color.WHITE)
        self.assertFalse(pawn.can_reach(1, 1, 1, 1, pawn.get_color()))
        self.assertFalse(pawn.can_reach(1, 1, 0, 1, pawn.get_color()))
        self.assertFalse(pawn.can_reach(1, 1, 0, 0, pawn.get_color()))
        self.assertFalse(pawn.can_reach(1, 1, 1, 0, pawn.get_color()))
        self.assertFalse(pawn.can_reach(1, 1, 2, 0, pawn.get_color()))
        self.assertFalse(pawn.can_reach(1, 1, 2, 2, pawn.get_color()))
        self.assertFalse(pawn.can_reach(1, 1, 1, 2, pawn.get_color()))
        self.assertFalse(pawn.can_reach(1, 1, 0, 1, pawn.get_color()))


if __name__ == '__main__':
    unittest.main()
