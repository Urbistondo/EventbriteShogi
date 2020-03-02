from src.Domain.Exceptions.CoordinatesOutOfBoundsError import CoordinatesOutOfBoundError


class ValidateCoordinatesService:
    @staticmethod
    def execute(validate_coordinates_command):
        row = int(validate_coordinates_command.get_row_coordinate())
        col = int(validate_coordinates_command.get_column_coordinate())

        if row < 0 or col < 0 or \
                row >= validate_coordinates_command.get_rows() or col >= validate_coordinates_command.get_columns():
            raise CoordinatesOutOfBoundError('The provided coordinates are out of the bounds of the board')
