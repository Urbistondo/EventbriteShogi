from Pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Bishop'
        self.representation = 'B'
