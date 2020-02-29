from Pieces.Piece import Piece


class SilverGeneral(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Silver General'
        self.representation = 'S'
