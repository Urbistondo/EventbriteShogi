import datetime

from Pieces.Piece import Color


class Game:
    board = None
    piece_factory = None
    start_date = None
    end_date = None
    pieces_white = None
    pieces_black = None
    captured_white = None
    captured_black = None

    finished = False
    winner = None
    turn = None
    current_player = None

    def __init__(self, board, piece_factory):
        self.board = board
        self.piece_factory = piece_factory
