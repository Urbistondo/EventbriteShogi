from Exceptions.CoordinatesOutOfBoundsError import CoordinatesOutOfBoundError
from Exceptions.InvalidCoordinateFormatError import InvalidCoordinateFormat


class MoveController:
    @staticmethod
    def validate_coordinates(board, coordinates):
        if len(coordinates) != 2:
            raise InvalidCoordinateFormat('The provided coordinates are not valid')

        row, col = int(coordinates[0]), int(coordinates[1])
        if row < 0 or col < 0 or row >= board.rows or col >= row >= board.columns:
            raise CoordinatesOutOfBoundError('The provided coordinates are out of the bounds of the board')

    @staticmethod
    def validate_move(board, origin_coordinates, destination_coordinates, color):
        if board.is_occupied_by_friendly(destination_coordinates[0], destination_coordinates[1], color):
            raise ValueError

    @staticmethod
    def is_capture(board, destination_coordinates, color):
        return board.is_occupied_by_enemy(destination_coordinates[0], destination_coordinates[1], color)

    @staticmethod
    def move(board, origin_coordinates, destination_coordinates, color):
        MoveController.validate_move(
            board,
            origin_coordinates,
            destination_coordinates,
            color
        )
        captured = None
        if MoveController.is_capture(board, destination_coordinates, color):
            captured = board.get_piece_in_square(destination_coordinates[0], destination_coordinates[1])

        board.grid[destination_coordinates[0]][destination_coordinates[1]] =\
            board.grid[origin_coordinates[0]][origin_coordinates[1]].get_piece()
        board.grid[origin_coordinates[0]][origin_coordinates[1]].remove_piece()

        return captured
