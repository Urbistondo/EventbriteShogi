from src.Application.MovePieceCommand import MovePieceCommand
from src.Application.ValidateCoordinatesCommand import ValidateCoordinatesCommand
from src.Application.ValidateCoordinatesService import ValidateCoordinatesService
from src.Domain.Board import Board
from src.Domain.Exceptions.CoordinatesOutOfBoundsError import CoordinatesOutOfBoundError
from src.Domain.Exceptions.DestinationSquareOccupiedError import DestinationSquareOccupiedError
from src.Domain.Exceptions.InvalidCoordinateFormatError import InvalidCoordinateFormat
from src.Domain.Exceptions.InvalidMovementForPieceError import InvalidMovementForPieceError
from src.Domain.Exceptions.OriginSquareContainsEnemyPieceError import OriginSquareContainsEnemyPieceError
from src.Domain.Exceptions.OriginSquareEmptyError import OriginSquareEmptyError
from src.Domain.Game import Game
from src.Application.MovePieceService import MovePieceService
from src.Domain.Pieces.Piece import Color
from src.Domain.Pieces.PieceFactory import PieceFactory


def prompt_move(rows, columns, turn, player, validate_coordinate_service):
    next_color = 'Black' if player == Color.BLACK else 'White'
    print('Turn ' + str(turn) + ' - ' + next_color)

    while True:
        origin_coordinates = input('From (row col):\n')
        validate_coordinates_command = ValidateCoordinatesCommand(
            rows,
            columns,
            origin_coordinates[0],
            origin_coordinates[1]
        )
        try:
            validate_coordinate_service.validate_coordinates(validate_coordinates_command)
        except (InvalidCoordinateFormat, CoordinatesOutOfBoundError) as e:
            print(e)
            continue

        break

    while True:
        destination_coordinates = input('To (row col):\n')
        validate_coordinates_command = ValidateCoordinatesCommand(
            rows,
            columns,
            destination_coordinates[0],
            destination_coordinates[1]
        )
        try:
            validate_coordinate_service.validate_coordinates(validate_coordinates_command)
        except (InvalidCoordinateFormat, CoordinatesOutOfBoundError) as e:
            print(e)
            continue

        break

    return (int(origin_coordinates[0]), int(origin_coordinates[1])),\
           (int(destination_coordinates[0]), int(destination_coordinates[1]))


board = Board(9, 9)
piece_factory = PieceFactory()
move_piece_service = MovePieceService()
validate_coordinates_service = ValidateCoordinatesService()
game = Game(board, piece_factory)
game.start_game()

while not game.is_finished():
    game.to_string()
    color = game.get_current_player()
    captured = None

    while True:
        try:
            origin_coordinates, destination_coordinates = prompt_move(
                board.get_rows(),
                board.get_columns(),
                game.get_turn(),
                color,
                validate_coordinates_service
            )

            captured = move_piece_service.move(
                MovePieceCommand(board, origin_coordinates, destination_coordinates, color)
            )
        except (
                CoordinatesOutOfBoundError,
                DestinationSquareOccupiedError,
                InvalidCoordinateFormat,
                InvalidMovementForPieceError,
                OriginSquareEmptyError,
                OriginSquareContainsEnemyPieceError
        ) as e:
            print(e)
            continue

        break

    if captured:
        game.add_captured(color, captured)

    game.next_turn()

