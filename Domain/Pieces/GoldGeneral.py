from Domain.Pieces.Piece import Piece


class GoldGeneral(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Gold General'
        self.representation = 'G'
