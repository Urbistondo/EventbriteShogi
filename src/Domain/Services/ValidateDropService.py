from src.Domain.Exceptions.DestinationSquareOccupiedError import DestinationSquareOccupiedError
from src.Domain.Exceptions.InvalidDropPieceSelectedError import InvalidDropPieceSelectedError
from src.Domain.Exceptions.InvalidMovementForPieceError import InvalidMovementForPieceError
from src.Domain.Exceptions.OriginSquareContainsEnemyPieceError import OriginSquareContainsEnemyPieceError
from src.Domain.Exceptions.OriginSquareEmptyError import OriginSquareEmptyError
from src.Domain.Exceptions.PieceMovementPathObstructedError import PieceMovementPathObstructedError
from src.Domain.Services.ValidateCoordinatesCommand import ValidateCoordinatesCommand
from src.Domain.Services.ValidateCoordinatesService import ValidateCoordinatesService


class ValidateDropService:
    @staticmethod
    def execute(validate_drop_command):
        board = validate_drop_command.get_board()
        droppable_pieces = validate_drop_command.get_droppable_pieces()
        origin_coordinates = validate_drop_command.get_origin_coordinates()
        destination_coordinates = validate_drop_command.get_destination_coordinates()

        print(droppable_pieces)

        if origin_coordinates[0] != board.get_rows() or not (0 <= origin_coordinates[1] <= len(droppable_pieces)):
            raise InvalidDropPieceSelectedError(
                'The entered coordinates do not correspond to an available captured piece'
            )

        ValidateCoordinatesService.execute(
            ValidateCoordinatesCommand(
                board.get_rows(),
                board.get_columns(),
                destination_coordinates[0],
                destination_coordinates[1]
            )
        )

        if not board.is_square_empty(destination_coordinates[0], destination_coordinates[1]):
            raise DestinationSquareOccupiedError('The drop destination square contains another piece')
