from src.Application.Services.DropPieceCommand import DropPieceCommand
from src.Application.Services.DropPieceService import DropPieceService
from src.Application.Services.MoveAndCapturePieceCommand import MoveAndCapturePieceCommand
from src.Application.Services.MoveAndCapturePieceService import MoveAndCapturePieceService
from src.Application.Services.MovePieceCommand import MovePieceCommand
from src.Domain.Exceptions.InvalidDropPieceSelectedError import InvalidDropPieceSelectedError
from src.Domain.Exceptions.PieceMovementPathObstructedError import PieceMovementPathObstructedError
from src.Domain.Services.ValidateCoordinatesService import ValidateCoordinatesService
from src.Domain.Entities.Board import Board
from src.Domain.Exceptions.CoordinatesOutOfBoundsError import CoordinatesOutOfBoundError
from src.Domain.Exceptions.DestinationSquareOccupiedError import DestinationSquareOccupiedError
from src.Domain.Exceptions.InvalidCoordinateFormatError import InvalidCoordinateFormat
from src.Domain.Exceptions.InvalidMovementForPieceError import InvalidMovementForPieceError
from src.Domain.Exceptions.OriginSquareContainsEnemyPieceError import OriginSquareContainsEnemyPieceError
from src.Domain.Exceptions.OriginSquareEmptyError import OriginSquareEmptyError
from src.Domain.Entities.Game import Game
from src.Application.Services.MovePieceService import MovePieceService
from src.Domain.Entities.PieceFactory import PieceFactory
from src.Infrastructure.Clients.CommandLineClient import CommandLineClient


ROWS = 9
COLUMNS = 9
CAPTURED_ROW_INDEX = 9

board = Board(ROWS, COLUMNS)
piece_factory = PieceFactory()
drop_piece_service = DropPieceService()
move_piece_service = MovePieceService()
move_and_capture_piece_service = MoveAndCapturePieceService()
validate_coordinates_service = ValidateCoordinatesService()

command_line_client = CommandLineClient(Game(board, piece_factory))
command_line_client.get_game().start_game()

while not command_line_client.get_game().is_finished():
    command_line_client.show_game_state()
    color = command_line_client.get_game().get_current_player()
    captured = None

    while True:
        try:
            origin_coordinates, destination_coordinates = CommandLineClient.prompt_move(
                board.get_rows(),
                board.get_columns(),
                command_line_client.get_game().get_turn(),
                color,
                validate_coordinates_service
            )

            if CAPTURED_ROW_INDEX == origin_coordinates[0]:
                dropped = drop_piece_service.execute(
                    DropPieceCommand(
                        board,
                        command_line_client.get_game().get_captured_by_color(color),
                        origin_coordinates,
                        destination_coordinates
                    )
                )
                command_line_client.get_game().remove_captured(color, dropped)
            elif board.is_square_occupied_by_enemy(destination_coordinates[0], destination_coordinates[1], color):
                captured = move_and_capture_piece_service.execute(
                    MoveAndCapturePieceCommand(board, origin_coordinates, destination_coordinates, color)
                )
                command_line_client.get_game().add_captured(color, captured)
            else:
                move_piece_service.execute(MovePieceCommand(board, origin_coordinates, destination_coordinates, color))
        except (
                CoordinatesOutOfBoundError,
                DestinationSquareOccupiedError,
                InvalidCoordinateFormat,
                InvalidDropPieceSelectedError,
                InvalidMovementForPieceError,
                OriginSquareEmptyError,
                OriginSquareContainsEnemyPieceError,
                PieceMovementPathObstructedError
        ) as e:
            print(e)
            continue

        break

    command_line_client.get_game().next_turn()
