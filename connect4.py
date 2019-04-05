import numpy as np


def create_board():
    board = np.zeros((6,7))
    return board

board = create_board()
game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 input
    if turn == 0:
        selection = int(input('Player 1 make your selection (0-6): '))
        if not 0 <= selection < 7:
            continue

    # Ask for Player 2 input
    else:
        selection = int(input('Player 2 make your selection (0-6): '))
        if not 0 <= selection < 7:
            continue

    turn += 1
    turn = turn % 2  # to alternate between player 1 and player 2
