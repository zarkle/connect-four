"""Connect Four Game"""
import numpy as np
import pygame
import sys


# define board size
ROW_COUNT = 6
COLUMN_COUNT = 7
# define colors (in RGB value):
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


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
                # game_over = True
                return True

    # Check all vertical locations
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                # game_over = True
                return True

    # Check positively sloped diagonals
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                # game_over = True
                return True

    # Check negatively sloped diagonals
    for col in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                # game_over = True
                return True


def draw_board(board):
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen, YELLOW, (column * SQUARESIZE, row * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (column * SQUARESIZE + SQUARESIZE // 2, row * SQUARESIZE + SQUARESIZE + SQUARESIZE // 2), RADIUS)

    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][column] == 1:  # player 2 piece
                pygame.draw.circle(screen, RED, (column * SQUARESIZE + SQUARESIZE // 2, height - (row * SQUARESIZE + SQUARESIZE // 2)), RADIUS)
            elif board[row][column] == 2:  # player 2 piece
                pygame.draw.circle(screen, BLUE, (column * SQUARESIZE + SQUARESIZE // 2, height - (row * SQUARESIZE + SQUARESIZE // 2)), RADIUS)
    # re-render the screen with the new changes
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

# initialize pygame
pygame.init()

# define screen size (how big will the game be)
# imagine board as a grid, define each square in pixels (SQUARESIZE)
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
# circle radius
RADIUS = SQUARESIZE // 2 - 5

# to get pygame to read it
screen = pygame.display.set_mode(size)
draw_board(board)
# make sure to update display
pygame.display.update()

# font to display winner
myfont = pygame.font.SysFont('monospace', 75)

# main game functionality
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # draw the pieces in the top row (above board) for the current player
        if event.type == pygame.MOUSEMOTION:
            # draw a black rectangle to cover any previously drawn circles (to clear the row above the board)
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            x_pos = event.pos[0]
            if turn == 0:  # player 1 turn
                pygame.draw.circle(screen, RED, (x_pos, SQUARESIZE // 2), RADIUS)
            else:  # player 2 turn
                pygame.draw.circle(screen, BLUE, (x_pos, SQUARESIZE // 2), RADIUS)
        pygame.display.update()

        # click on column piece will drop in
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # Ask for Player 1 input
            if turn == 0:
                x_pos = event.pos[0]
                column = x_pos // SQUARESIZE

                if is_valid_column(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 1)

                    if winning_move(board, 1):
                        print('Player 1 is the winner!')
                        label = myfont.render('Player 1 is the winner!', 1, RED)
                        # update a specific part of the screen instead of update the entire display
                        screen.blit(label, (40, 10))
                        game_over = True
                else:
                    print('Invalid move')
                    label = myfont.render('Invalid move, try again', 1, RED)
                    screen.blit(label, (40, 10))
                    turn -= 1

            # Ask for Player 2 input
            else:
                x_pos = event.pos[0]
                column = x_pos // SQUARESIZE

                if is_valid_column(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 2)

                    if winning_move(board, 2):
                        print('Player 2 is the winner!')
                        label = myfont.render('Player 2 is the winner!', 1, BLUE)
                        # update a specific part of the screen instead of update the entire display
                        screen.blit(label, (40, 10))
                        game_over = True
                else:
                    print('Invalid move')
                    label = myfont.render('Invalid move, try again', 1, BLUE)
                    screen.blit(label, (40, 10))
                    turn -= 1

            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2  # to alternate between player 1 and player 2

            # once finish game, notify winning player and wait before closing
            if game_over:
                pygame.time.wait(5000)
