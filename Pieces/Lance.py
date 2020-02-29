from Pieces.Piece import Piece


class Lance(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Lance'
        self.representation = 'L'
