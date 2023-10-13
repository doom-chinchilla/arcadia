import numpy as np
import math
import pygame
import sys

BLUE = (0,0,255)
BLACK = (0,0,0)

ROW_COUNT = 6
COLUMN_COUNT = 7


EVEN = 0
ODD = 1

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board,col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board,0))

def winning_move(board, piece):
    # check horizontal locations for a win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece \
                and board[r][c+2] == piece \
                    and board[r][c+3] == piece:
                return True

    # check vertical locations for a win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c] == piece \
                    and board[r+2][c] == piece \
                        and board[r+3][c] == piece:
                    return True

    # check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece \
                and board[r+2][c+2] == piece \
                    and board[r+3][c+3] == piece:
                return True

    # check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece \
                and board[r-2][c+2] == piece \
                    and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE) )
            pygame.draw.circle(screen, BLACK )

board = create_board()
print_board(board)
GAME_OVER = False
TURN = 0

pygame.init()

SQUARE_SIZE = 100

width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT+1) * SQUARE_SIZE

size = (width, height)

RADIUS = int(SQUARE_SIZE/2 -5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not GAME_OVER:
    # as for Player 1 input:
    # todo: ask players for names
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # ask for player 1 input
            if TURN == 0:
                col = int(input("Player 1: Make your selection (0-6):"))

                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board, row, col, 1)

            # Ask for Player 2 input
            else:
                col = int(input("Player 2: Make your selection (0-6:"))

                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board,1):
                        print("Congrats! Player 1 wins!!")
                        GAME_OVER = True

                    if winning_move(board,2):
                        print("Congrats! Player 2 wins!!")
                        GAME_OVER = True

    print_board(board)

    TURN += 1
    TURN = TURN % 2
