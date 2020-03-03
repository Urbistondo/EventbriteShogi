import unittest

from Domain.Exceptions.CoordinatesOutOfBoundsException import CoordinatesOutOfBoundsException
from Domain.Services.ValidateCoordinatesCommand import ValidateCoordinatesCommand
from Domain.Services.ValidateCoordinatesService import ValidateCoordinatesService


class TestValidateCoordinatesService(unittest.TestCase):
    rows = 9
    columns = 9

    def test_execute_valid(self):
        validate_coordinates_command = ValidateCoordinatesCommand(
            self.rows,
            self.columns,
            0,
            0
        )

        ValidateCoordinatesService.execute(validate_coordinates_command)

    def test_execute_out_of_bounds_error(self):
        validate_coordinates_command = ValidateCoordinatesCommand(
            self.rows,
            self.columns,
            'a',
            0
        )

        with self.assertRaises(ValueError):
            ValidateCoordinatesService.execute(validate_coordinates_command)

    def test_execute_value_error(self):
        validate_coordinates_command = ValidateCoordinatesCommand(
            self.rows,
            self.columns,
            -1,
            0
        )

        with self.assertRaises(CoordinatesOutOfBoundsException):
            ValidateCoordinatesService.execute(validate_coordinates_command)


if __name__ == '__main__':
    unittest.main()
