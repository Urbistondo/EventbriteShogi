import unittest

from src.Domain.Entities.Board import Board
from src.Domain.Entities.Piece import Color
from src.Domain.Entities.PieceFactory import PieceFactory
from src.Domain.Exceptions.DestinationSquareOccupiedError import DestinationSquareOccupiedError
from src.Domain.Exceptions.InvalidMovementForPieceError import InvalidMovementForPieceError
from src.Domain.Exceptions.OriginSquareContainsEnemyPieceError import OriginSquareContainsEnemyPieceError
from src.Domain.Exceptions.OriginSquareEmptyError import OriginSquareEmptyError
from src.Domain.Exceptions.PieceMovementPathObstructedError import PieceMovementPathObstructedError
from src.Domain.Services.ValidateMoveCommand import ValidateMoveCommand
from src.Domain.Services.ValidateMoveService import ValidateMoveService


class TestValidateMoveService(unittest.TestCase):
    rows = 9
    columns = 9
    board = Board(rows, columns)
    board.initialize_board(PieceFactory())

    def test_execute_valid(self):
        ValidateMoveService.execute(ValidateMoveCommand(self.board, (0, 0), (1, 0), Color.WHITE))

    def test_execute_empty_square_error(self):
        with self.assertRaises(OriginSquareEmptyError):
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (1, 0), (3, 0), Color.WHITE))

    def test_execute_square_occupied_enemy_error(self):
        with self.assertRaises(OriginSquareContainsEnemyPieceError):
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (6, 0), (5, 0), Color.WHITE))

    def test_execute_square_occupied_friend_error(self):
        with self.assertRaises(DestinationSquareOccupiedError):
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (0, 0), (2, 0), Color.WHITE))

    def test_execute_square_not_reachable_error(self):
        with self.assertRaises(InvalidMovementForPieceError):
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (2, 0), (3, 1), Color.WHITE))

    def test_execute_path_obstructed_error(self):
        with self.assertRaises(PieceMovementPathObstructedError):
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (1, 7), (3, 5), Color.WHITE))


if __name__ == '__main__':
    unittest.main()
