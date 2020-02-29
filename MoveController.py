from Exceptions.CoordinatesOutOfBoundsError import CoordinatesOutOfBoundError
from Exceptions.InvalidCoordinateFormatError import InvalidCoordinateFormat


class MoveController:
    @staticmethod
    def validate_coordinates(board, coordinates):
        if len(coordinates) != 2:
            raise InvalidCoordinateFormat('The provided coordinates are not valid')

        row, col = int(coordinates[0]), int(coordinates[1])
        if row < 0 or col < 0 or row >= len(board.rows) or col >= row >= len(board.columns):
            raise CoordinatesOutOfBoundError('The provided coordinates are out of the bounds of the board')
