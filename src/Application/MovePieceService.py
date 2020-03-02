from src.Domain.Exceptions.CoordinatesOutOfBoundsError import CoordinatesOutOfBoundError
from src.Domain.Exceptions.InvalidCoordinateFormatError import InvalidCoordinateFormat
from src.Domain.Exceptions.DestinationSquareOccupiedError import DestinationSquareOccupiedError
from src.Domain.Exceptions.InvalidMovementForPieceError import InvalidMovementForPieceError
from src.Domain.Exceptions.OriginSquareContainsEnemyPieceError import OriginSquareContainsEnemyPieceError
from src.Domain.Exceptions.OriginSquareEmptyError import OriginSquareEmptyError


class MovePieceService:
    @staticmethod
    def validate_coordinates(board, coordinates):
        if len(coordinates) != 2:
            raise InvalidCoordinateFormat('The provided coordinates are not valid')

        try:
            row, col = int(coordinates[0]), int(coordinates[1])
        except ValueError:
            print('The provided coordinates include non-numeric characters')

        if row < 0 or col < 0 or row >= board.rows or col >= row >= board.columns:
            raise CoordinatesOutOfBoundError('The provided coordinates are out of the bounds of the board')

    @staticmethod
    def validate_move(board, origin_coordinates, destination_coordinates, color):
        if board.is_square_empty(origin_coordinates[0], origin_coordinates[1]):
            raise OriginSquareEmptyError('The origin square is empty')

        if not board.is_occupied_by_friendly(origin_coordinates[0], origin_coordinates[1], color):
            raise OriginSquareContainsEnemyPieceError('The origin square contains an enemy piece')

        if board.is_occupied_by_friendly(destination_coordinates[0], destination_coordinates[1], color):
            raise DestinationSquareOccupiedError("Can't move to a square occupied by a friendly piece")

        if not board.is_reachable_by_piece(
                origin_coordinates[0],
                origin_coordinates[1],
                destination_coordinates[0],
                destination_coordinates[1],
                color
        ):
            raise InvalidMovementForPieceError('The destination square is not reachable by the selected piece')

    @staticmethod
    def is_capture(board, destination_coordinates, color):
        return board.is_occupied_by_enemy(destination_coordinates[0], destination_coordinates[1], color)

    @staticmethod
    def move(move_piece_command):
        board = move_piece_command.get_board()
        origin_coordinates = move_piece_command.get_origin_coordinates()
        destination_coordinates = move_piece_command.get_destination_coordinates()
        color = move_piece_command.get_color()

        MovePieceService.validate_move(
            board,
            origin_coordinates,
            destination_coordinates,
            color
        )

        captured = None
        if MovePieceService.is_capture(board, destination_coordinates, color):
            captured = board.get_piece_in_square(
                destination_coordinates[0],
                destination_coordinates[1]
            )

        board.grid[destination_coordinates[0]][destination_coordinates[1]].set_piece(
            board.grid[origin_coordinates[0]][origin_coordinates[1]].get_piece()
        )
        board.grid[origin_coordinates[0]][origin_coordinates[1]].remove_piece()

        return captured
