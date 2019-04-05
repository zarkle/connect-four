import numpy as np


ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    """Create a Connect Four board."""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece():
    """Entered input will drop a piece into Connect Four board."""
    pass


def is_valid_column(board, column):
    """Check to see if entered column has an empty spot for piece. Check this by making sure the top row of the board (5th row) contains 0 for the entered column."""
    return board[ROW_COUNT - 1][column] == 0


def get_next_open_row(board, column):
    """."""
    pass


board = create_board()
game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 input
    if turn == 0:
        column = int(input('Player 1 make your column selection (0-6): '))
        if not 0 <= selection < 7:
            continue

    # Ask for Player 2 input
    else:
        column = int(input('Player 2 make your column selection (0-6): '))
        if not 0 <= selection < 7:
            continue

    turn += 1
    turn = turn % 2  # to alternate between player 1 and player 2
