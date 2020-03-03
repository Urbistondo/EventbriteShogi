import unittest

from Domain.Entities.Board import Board
from Domain.Entities.Piece import Color
from Domain.Entities.PieceFactory import PieceFactory
from Domain.Exceptions.DestinationSquareOccupiedException import DestinationSquareOccupiedException
from Domain.Exceptions.InvalidMovementForPieceException import InvalidMovementForPieceException
from Domain.Exceptions.OriginSquareContainsEnemyPieceException import OriginSquareContainsEnemyPieceException
from Domain.Exceptions.OriginSquareEmptyException import OriginSquareEmptyException
from Domain.Exceptions.PieceMovementPathObstructedException import PieceMovementPathObstructedException
from Domain.Services.ValidateMoveCommand import ValidateMoveCommand
from Domain.Services.ValidateMoveService import ValidateMoveService


class TestValidateMoveService(unittest.TestCase):
    rows = 9
    columns = 9
    board = Board(rows, columns)
    board.initialize_board(PieceFactory())

    def test_execute_valid(self):
        ValidateMoveService.execute(ValidateMoveCommand(self.board, (0, 0), (1, 0), Color.WHITE))

    def test_execute_empty_square_error(self):
        with self.assertRaises(OriginSquareEmptyException):
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (1, 0), (3, 0), Color.WHITE))

    def test_execute_square_occupied_enemy_error(self):
        with self.assertRaises(OriginSquareContainsEnemyPieceException):
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (6, 0), (5, 0), Color.WHITE))

    def test_execute_square_occupied_friend_error(self):
        with self.assertRaises(DestinationSquareOccupiedException):
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (0, 0), (2, 0), Color.WHITE))

    def test_execute_square_not_reachable_error(self):
        with self.assertRaises(InvalidMovementForPieceException):
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (2, 0), (3, 1), Color.WHITE))

    def test_execute_path_obstructed_error(self):
        with self.assertRaises(PieceMovementPathObstructedException):
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (1, 7), (3, 5), Color.WHITE))


if __name__ == '__main__':
    unittest.main()
