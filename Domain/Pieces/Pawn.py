from Domain.Pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Pawn'
        self.representation = 'P'
