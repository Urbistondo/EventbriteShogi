from src.Domain.Services.ValidateCoordinatesCommand import ValidateCoordinatesCommand
from src.Domain.Services.ValidateCoordinatesService import ValidateCoordinatesService
from src.Infrastructure.Services.BoardVisualizer import BoardVisualizer
from src.Domain.Pieces.Piece import Color
from src.Domain.Square import Square


class Board:
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
        first_row = 0
        second_row = 1
        third_row = 2

        if color == Color.BLACK:
            first_row = -1
            second_row = -2
            third_row = -3

        for i in range(self.columns):
            self.grid[third_row][i].set_piece(piece_factory.create_pawn(color))

        self.grid[second_row][1].set_piece(piece_factory.create_bishop(color))

        self.grid[second_row][-2].set_piece(piece_factory.create_rook(color))

        self.grid[first_row][0].set_piece(piece_factory.create_lance(color))
        self.grid[first_row][-1].set_piece(piece_factory.create_lance(color))

        self.grid[first_row][1].set_piece(piece_factory.create_knight(color))
        self.grid[first_row][-2].set_piece(piece_factory.create_knight(color))

        self.grid[first_row][2].set_piece(piece_factory.create_silver_general(color))
        self.grid[first_row][-3].set_piece(piece_factory.create_silver_general(color))

        self.grid[first_row][3].set_piece(piece_factory.create_gold_general(color))
        self.grid[first_row][-4].set_piece(piece_factory.create_gold_general(color))

        self.grid[first_row][4].set_piece(piece_factory.create_king(color))

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

    def get_piece_in_square(self, row, col):
        ValidateCoordinatesService.validate_coordinates(ValidateCoordinatesCommand(self.rows, self.columns, row, col))
        return self.grid[row][col].get_piece()

    def to_string(self, captured_white=None, captured_black=None):
        BoardVisualizer.visualize(self.grid, captured_white, captured_black)
