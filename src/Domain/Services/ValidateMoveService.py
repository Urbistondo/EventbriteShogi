from src.Domain.Exceptions.DestinationSquareOccupiedError import DestinationSquareOccupiedError
from src.Domain.Exceptions.InvalidMovementForPieceError import InvalidMovementForPieceError
from src.Domain.Exceptions.OriginSquareContainsEnemyPieceError import OriginSquareContainsEnemyPieceError
from src.Domain.Exceptions.OriginSquareEmptyError import OriginSquareEmptyError


class ValidateMoveService:
    @staticmethod
    def execute(validate_move_command):
        board = validate_move_command.get_board()
        origin_coordinates = validate_move_command.get_origin_coordinates()
        destination_coordinates = validate_move_command.get_destination_coordinates()
        color = validate_move_command.get_color()

        if board.is_square_empty(origin_coordinates[0], origin_coordinates[1]):
            raise OriginSquareEmptyError('The origin square is empty')

        if not board.is_square_occupied_by_friendly(origin_coordinates[0], origin_coordinates[1], color):
            raise OriginSquareContainsEnemyPieceError('The origin square contains an enemy piece')

        if board.is_square_occupied_by_friendly(destination_coordinates[0], destination_coordinates[1], color):
            raise DestinationSquareOccupiedError("Can't move to a square occupied by a friendly piece")

        if not board.is_square_reachable_by_piece(
                origin_coordinates[0],
                origin_coordinates[1],
                destination_coordinates[0],
                destination_coordinates[1],
                color
        ):
            raise InvalidMovementForPieceError('The destination square is not reachable by the selected piece')
