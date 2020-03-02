from Domain.Pieces.Piece import Piece


class Knight(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Knight'
        self.representation = 'N'
