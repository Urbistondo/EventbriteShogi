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
from src.Domain.Exceptions.CoordinatesOutOfBoundsError import CoordinatesOutOfBoundError
from src.Domain.Services.ValidateCoordinatesCommand import ValidateCoordinatesCommand
from src.Domain.Services.ValidateCoordinatesService import ValidateCoordinatesService


class TestValidateCoordinatesService(unittest.TestCase):
    def test_execute_valid(self):
        rows = 9
        columns = 9
        validate_coordinates_command = ValidateCoordinatesCommand(
                rows,
                columns,
                0,
                0
            )

        ValidateCoordinatesService.execute(validate_coordinates_command)

    def test_execute_out_of_bounds_error(self):
        rows = 9
        columns = 9
        validate_coordinates_command = ValidateCoordinatesCommand(
            rows,
            columns,
            'a',
            0
        )

        with self.assertRaises(ValueError):
            ValidateCoordinatesService.execute(validate_coordinates_command)

    def test_execute_value_error(self):
        rows = 9
        columns = 9
        validate_coordinates_command = ValidateCoordinatesCommand(
            rows,
            columns,
            -1,
            0
        )

        with self.assertRaises(CoordinatesOutOfBoundError):
            ValidateCoordinatesService.execute(validate_coordinates_command)


if __name__ == '__main__':
    unittest.main()
