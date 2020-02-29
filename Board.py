from Pieces.Piece import Color
from Square import Square


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

    def to_string(self):
        print(self.rows)
        print('============ Whites (v) ============')
        print('Captured:')
        print('9:')
        col_indices = '   '
        for i in range(self.columns):
            col_indices += ' ' + str(i) + ' '
        print(col_indices)
        print('+ ' + ' -' * len(col_indices) + ' +')
        for index, row in enumerate(self.grid):
            row_string = str(index) + '| '
            for square in row:
                row_string += square.to_string() + ' '
            print(row_string)
        print('+' + ' -' * len(col_indices) + ' +')
        print('Captured:')
        print('9:')
        print('============ Blacks (^) ============')
