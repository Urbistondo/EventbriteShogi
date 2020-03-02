from src.Domain.Pieces.Bishop import Bishop
from src.Domain.Pieces.Lance import Lance
from src.Domain.Pieces.Rook import Rook
from src.Domain.Services.ValidateCoordinatesCommand import ValidateCoordinatesCommand
from src.Domain.Services.ValidateCoordinatesService import ValidateCoordinatesService
from src.Infrastructure.Services.BoardVisualizer import BoardVisualizer
from src.Domain.Pieces.Piece import Color
from src.Domain.Square import Square


class Board:
    LEFT_LANCE_INDEX = 0
    RIGHT_LANCE_INDEX = -1
    LEFT_KNIGHT_INDEX = 1
    RIGHT_KNIGHT_INDEX = -2
    LEFT_SILVER_GENERAL_INDEX = 2
    RIGHT_SILVER_GENERAL_INDEX = -3
    LEFT_GOLD_GENERAL_INDEX = 3
    RIGHT_GOLD_GENERAL_INDEX = -4
    KING_INDEX = 4
    WHITE_BISHOP_INDEX = -2
    WHITE_ROOK_INDEX = 1
    BLACK_BISHOP_INDEX = 1
    BLACK_ROOK_INDEX = -2

    columns = -1
    rows = -1
    grid = None

    def __init__(self, rows, columns):
        if rows <= 0 or columns <= 0:
            raise ValueError

        self.rows = rows
        self.columns = columns
        self.grid = [[Square() for i in range(columns)] for j in range(rows)]

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_grid(self):
        return self.grid

    def initialize_board(self, piece_factory):
        self.create_pieces(piece_factory, Color.WHITE)
        self.create_pieces(piece_factory, Color.BLACK)

    def create_pieces(self, piece_factory, color):
        if color == Color.WHITE:
            first_row = 0
            second_row = 1
            third_row = 2

            self.grid[second_row][self.WHITE_BISHOP_INDEX].set_piece(piece_factory.create_bishop(color))
            self.grid[second_row][self.WHITE_ROOK_INDEX].set_piece(piece_factory.create_rook(color))
        else:
            first_row = -1
            second_row = -2
            third_row = -3

            self.grid[second_row][self.BLACK_BISHOP_INDEX].set_piece(piece_factory.create_bishop(color))
            self.grid[second_row][self.BLACK_ROOK_INDEX].set_piece(piece_factory.create_rook(color))

        self.grid[first_row][self.LEFT_LANCE_INDEX].set_piece(piece_factory.create_lance(color))
        self.grid[first_row][self.RIGHT_LANCE_INDEX].set_piece(piece_factory.create_lance(color))

        self.grid[first_row][self.LEFT_KNIGHT_INDEX].set_piece(piece_factory.create_knight(color))
        self.grid[first_row][self.RIGHT_KNIGHT_INDEX].set_piece(piece_factory.create_knight(color))

        self.grid[first_row][self.LEFT_SILVER_GENERAL_INDEX].set_piece(piece_factory.create_silver_general(color))
        self.grid[first_row][self.RIGHT_SILVER_GENERAL_INDEX].set_piece(piece_factory.create_silver_general(color))

        self.grid[first_row][self.LEFT_GOLD_GENERAL_INDEX].set_piece(piece_factory.create_gold_general(color))
        self.grid[first_row][self.RIGHT_GOLD_GENERAL_INDEX].set_piece(piece_factory.create_gold_general(color))

        self.grid[first_row][self.KING_INDEX].set_piece(piece_factory.create_king(color))

        for i in range(self.columns):
            self.grid[third_row][i].set_piece(piece_factory.create_pawn(color))

    def validate_coordinates(self, row, col):

        if row < 0 or col < 0 or row >= self.rows or col >= self.columns:
            raise ValueError("The provided coordinates are out of the board's bounds")

    def is_square_empty(self, row, col):
        ValidateCoordinatesService.validate_coordinates(ValidateCoordinatesCommand(self.rows, self.columns, row, col))
        return self.grid[row][col].is_empty()

    def is_square_occupied_by_friendly(self, row, col, color):
        ValidateCoordinatesService.validate_coordinates(ValidateCoordinatesCommand(self.rows, self.columns, row, col))
        return not self.grid[row][col].is_empty() and self.grid[row][col].get_piece().get_color() == color

    def is_square_occupied_by_enemy(self, row, col, color):
        ValidateCoordinatesService.validate_coordinates(ValidateCoordinatesCommand(self.rows, self.columns, row, col))
        return not self.grid[row][col].is_empty() and self.grid[row][col].get_piece().get_color() != color

    def is_square_reachable_by_piece(self, origin_row, origin_col, destination_row, destination_col, color):
        ValidateCoordinatesService.validate_coordinates(
            ValidateCoordinatesCommand(self.rows, self.columns, origin_row, origin_col)
        )
        ValidateCoordinatesService.validate_coordinates(
            ValidateCoordinatesCommand(self.rows, self.columns, destination_row, destination_col)
        )
        piece = self.grid[origin_row][origin_col].get_piece()
        return piece.can_reach(origin_row, origin_col, destination_row, destination_col, color)

    def is_path_obstructed(self, origin_row, origin_col, destination_row, destination_col):
        ValidateCoordinatesService.validate_coordinates(
            ValidateCoordinatesCommand(self.rows, self.columns, origin_row, origin_col)
        )
        ValidateCoordinatesService.validate_coordinates(
            ValidateCoordinatesCommand(self.rows, self.columns, destination_row, destination_col)
        )
        piece = self.grid[origin_row][origin_col].get_piece()

        if isinstance(piece, Bishop):
            row_direction = -1 if origin_row > destination_row else 1
            col_direction = -1 if origin_col > destination_col else 1

            distance = abs(origin_row - destination_row) - 1
            for i in range(distance):
                origin_row += row_direction
                origin_col += col_direction
                if not self.grid[origin_row][origin_col].is_empty():
                    return True

        if isinstance(piece, Lance):
            if origin_col < destination_col:
                col_start = origin_col
                col_end = destination_col
            else:
                col_start = destination_col
                col_end = origin_col

            for j in range(col_start, col_end + 1):
                if not self.grid[origin_row][j].is_empty():
                    return True

        if isinstance(piece, Rook):
            if origin_row == destination_row:
                if origin_col < destination_col:
                    col_start = origin_col
                    col_end = destination_col
                else:
                    col_start = destination_col
                    col_end = origin_col

                for j in range(col_start, col_end + 1):
                    if not self.grid[origin_row][j].is_empty():
                        return True
            else:
                if origin_row < destination_row:
                    row_start = origin_row
                    row_end = destination_row
                else:
                    row_start = destination_row
                    row_end = origin_row

                for i in range(row_start, row_end + 1):
                    if not self.grid[i][origin_col].is_empty():
                        return True

        return False

    def get_piece_in_square(self, row, col):
        ValidateCoordinatesService.validate_coordinates(ValidateCoordinatesCommand(self.rows, self.columns, row, col))
        return self.grid[row][col].get_piece()

    def to_string(self, captured_white=None, captured_black=None):
        BoardVisualizer.visualize(self.grid, captured_white, captured_black)
