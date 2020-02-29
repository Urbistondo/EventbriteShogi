from Board import Board
from Game import Game
from Pieces.Piece import Color
from Pieces.PieceFactory import PieceFactory


def prompt_move(board, turn, player):
    next_color = 'Black' if player == Color.BLACK else 'White'
    print('Turn ' + str(turn) + ' - ' + next_color)
    origin_coordinates = input('From (row col):\n')
    destination_coordinates = input('To (row col):\n')

    return (int(origin_coordinates[0]), int(origin_coordinates[1])),\
           (int(destination_coordinates[0]), int(destination_coordinates[1]))


board = Board(9, 9)
piece_factory = PieceFactory()
game = Game(board, piece_factory)
game.start_game()

while not game.is_finished():
    game.board.to_string()
    color = game.get_current_player()
    origin_coordinates, destination_coordinates = prompt_move(board, game.get_turn(), color)
    game.next_turn()

