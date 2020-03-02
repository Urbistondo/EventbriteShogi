from Domain.BoardVisualizer import BoardVisualizer
from Domain.Pieces.Piece import Color
from Domain.Square import Square


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

    def is_square_empty(self, row, col):
        return self.grid[row][col].is_empty()

    def is_occupied_by_friendly(self, row, col, color):
        return not self.grid[row][col].is_empty() and self.grid[row][col].get_piece().get_color() == color

    def is_occupied_by_enemy(self, row, col, color):
        return not self.grid[row][col].is_empty() and self.grid[row][col].get_piece().get_color() != color

    def get_piece_in_square(self, row, col):
        return self.grid[row][col].get_piece()

    def to_string(self, captured_white=None, captured_black=None):
        BoardVisualizer.visualize(self.grid, captured_white, captured_black)
