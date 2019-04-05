import numpy as np


ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    """Create a Connect Four board."""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def is_valid_column(board, column):
    """Check to see if entered column has an empty spot for piece. Check this by making sure the top row of the board (5th row) contains 0 for the entered column."""
    return board[ROW_COUNT - 1][column] == 0


def get_next_open_row(board, column):
    """Returns the row the piece would fall on."""
    for row in range(ROW_COUNT):
        if board[row][column] == 0:
            return row


def drop_piece(board, row, column, piece):
    """Fill in the board column with whatever piece the player just dropped."""
    board[row][column] = piece


board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 input
    if turn == 0:
        column = int(input('Player 1 make your column selection (0-6): '))
        if not 0 <= column < 7:
            continue
        if is_valid_column(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 1)

    # Ask for Player 2 input
    else:
        column = int(input('Player 2 make your column selection (0-6): '))
        if not 0 <= column < 7:
            continue
        if is_valid_column(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)

    print(board)
    turn += 1
    turn = turn % 2  # to alternate between player 1 and player 2
