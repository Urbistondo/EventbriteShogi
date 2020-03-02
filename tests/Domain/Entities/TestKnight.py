import unittest

from src.Domain.Entities.Knight import Knight
from src.Domain.Entities.Piece import Color


class TestKnight(unittest.TestCase):
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

    PIECE_DESCRIPTION = 'Knight'
    PIECE_REPRESENTATION = 'N'

    def test_init(self):
        piece = Knight(Color.WHITE)
        self.assertEqual(self.PIECE_DESCRIPTION, piece.description)
        self.assertEqual(self.PIECE_REPRESENTATION, piece.representation)
        self.assertEqual(Color.WHITE, piece.color)
        self.assertEqual(self.COLORS[Color.WHITE]['symbol'], piece.symbol)

    def test_can_reach(self):
        piece = Knight(Color.WHITE)

        origin_row = 2
        origin_col = 2

        valid_destinations = [
            (4, 1),
            (4, 3),
        ]

        for i in range(5):
            for j in range(5):
                if (i, j) in valid_destinations:
                    self.assertTrue(
                        piece.can_reach(origin_row, origin_col, i, j, piece.get_color())
                    )
                else:
                    self.assertFalse(
                        piece.can_reach(origin_row, origin_col, i, j, piece.get_color())
                    )


if __name__ == '__main__':
    unittest.main()
