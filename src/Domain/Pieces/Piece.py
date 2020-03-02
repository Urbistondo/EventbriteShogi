from enum import Enum


class Color(Enum):
    WHITE = 0
    BLACK = 1


class Piece:
    description = None
    color = False
    representation = None
    symbol = None

    SYMBOL_BLACK = '^'
    SYMBOL_WHITE = 'v'

    def __init__(self, color=Color.WHITE):
        self.color = color
        self.symbol = self.SYMBOL_WHITE if color == Color.WHITE else self.SYMBOL_BLACK

    def create_white(self):
        return self.__init__(Color.WHITE)

    def create_black(self):
        return self.__init__(Color.BLACK)

    def get_color(self):
        return self.color

    def can_reach(self, origin_row, origin_col, destination_row, destination_col, color=None):
        pass

    def to_string(self):
        return self.representation + self.symbol
