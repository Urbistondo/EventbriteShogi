from Pieces.Piece import Piece


class King(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'King'
        self.representation = 'K'
