from src.Domain.Pieces.Bishop import Bishop
from src.Domain.Pieces.GoldGeneral import GoldGeneral
from src.Domain.Pieces.King import King
from src.Domain.Pieces.Knight import Knight
from src.Domain.Pieces.Lance import Lance
from src.Domain.Pieces.Pawn import Pawn
from src.Domain.Pieces.Rook import Rook
from src.Domain.Pieces.SilverGeneral import SilverGeneral


class PieceFactory:
    @staticmethod
    def create_bishop(color):
        return Bishop(color)

    @staticmethod
    def create_gold_general(color):
        return GoldGeneral(color)

    @staticmethod
    def create_king(color):
        return King(color)

    @staticmethod
    def create_knight(color):
        return Knight(color)

    @staticmethod
    def create_lance(color):
        return Lance(color)

    @staticmethod
    def create_pawn(color):
        return Pawn(color)

    @staticmethod
    def create_rook(color):
        return Rook(color)

    @staticmethod
    def create_silver_general(color):
        return SilverGeneral(color)
