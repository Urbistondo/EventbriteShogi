from src.Application.Services.MoveAndCapturePieceCommand import MoveAndCapturePieceCommand
from src.Application.Services.MoveAndCapturePieceService import MoveAndCapturePieceService
from src.Application.Services.MovePieceCommand import MovePieceCommand
from src.Domain.Exceptions.PieceMovementPathObstructedError import PieceMovementPathObstructedError
from src.Domain.Services.ValidateCoordinatesService import ValidateCoordinatesService
from src.Domain.Board import Board
from src.Domain.Exceptions.CoordinatesOutOfBoundsError import CoordinatesOutOfBoundError
from src.Domain.Exceptions.DestinationSquareOccupiedError import DestinationSquareOccupiedError
from src.Domain.Exceptions.InvalidCoordinateFormatError import InvalidCoordinateFormat
from src.Domain.Exceptions.InvalidMovementForPieceError import InvalidMovementForPieceError
from src.Domain.Exceptions.OriginSquareContainsEnemyPieceError import OriginSquareContainsEnemyPieceError
from src.Domain.Exceptions.OriginSquareEmptyError import OriginSquareEmptyError
from src.Domain.Game import Game
from src.Application.Services.MovePieceService import MovePieceService
from src.Domain.Pieces.PieceFactory import PieceFactory
from src.Infrastructure.Clients.CommandLineClient import CommandLineClient

board = Board(9, 9)
piece_factory = PieceFactory()
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

            if board.is_square_occupied_by_enemy(destination_coordinates[0], destination_coordinates[1], color):
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
                InvalidMovementForPieceError,
                OriginSquareEmptyError,
                OriginSquareContainsEnemyPieceError,
                PieceMovementPathObstructedError
        ) as e:
            print(e)
            continue

        break

    command_line_client.get_game().next_turn()
