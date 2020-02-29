from Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Rook'
        self.representation = 'R'
