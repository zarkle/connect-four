"""Connect Four Game"""
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


def print_board(board):
    """Change orientation so board is oriented same as the actual Connect Four game with row 0 on bottom."""
    print(np.flip(board, 0))


def winning_move(board, piece):
    """
    Stop game if player wins game.
    Note: This is not the most efficient method, but the simplest method to explain.
    """
    # Check all horizontal locations
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                game_over = True
                return True

    # Check all vertical locations
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                game_over = True
                return True

    # Check positively sloped diagonals
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                game_over = True
                return True

    # Check negatively sloped diagonals
    for col in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                game_over = True
                return True

board = create_board()
print_board(board)
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

            if winning_move(board, 1):
                print('Player 1 is the winner!')
                game_over = True

    # Ask for Player 2 input
    else:
        column = int(input('Player 2 make your column selection (0-6): '))
        if not 0 <= column < 7:
            continue
        if is_valid_column(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)

            if winning_move(board, 2):
                print('Player 2 is the winner!')
                game_over = True

    print_board(board)
    turn += 1
    turn = turn % 2  # to alternate between player 1 and player 2
