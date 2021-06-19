import pygame, sys
import numpy as np

pygame.init()

altura = 600
largura = 600
line_width = 15
board_rows = 3
board_cols = 3
square_size = largura // board_cols
circle_radius = 60
circle_width = 15
cross_width = 25
space = 55
# CORES
RED = (255, 0, 0)
bg_color = (28, 170, 156)
line_color = (23, 145, 135)
circle_color = (239, 231, 200)
cross_color = (66, 66, 66)

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(bg_color)

# TABULEIRO
board = np.zeros((board_rows, board_cols))
# print(board)

# pygame.draw.line(screen, verm, (10, 10), (300, 300), 10)


def draw_lines():
    # horizontal 1
    pygame.draw.line(screen, line_color, (0, square_size), (largura, square_size), line_width)
    # horizontal
    pygame.draw.line(screen, line_color, (0, 2*square_size), (largura, 2 * square_size), line_width)
    # vertical 1
    pygame.draw.line(screen, line_color, (square_size, 0), (square_size, altura), line_width)
    # vertical 2
    pygame.draw.line(screen, line_color, (2*square_size, 0), (2 * square_size, altura), line_width)


def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color, (int(col * square_size + square_size//2), int(row * square_size + square_size//2)), circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + square_size - space),
                                 (col * square_size + square_size - space, row * square_size + space), cross_width)
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + space),
                                 (col * square_size + square_size- space, row * square_size + square_size - space), cross_width)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False

    return True


def check_win(player):
    # VERTICAL WIN CHECK
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    # HORIZONTAL WIN CHECK
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    # ASC DIAGONAL WIN CHECK
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    # DES DIAGONAL WIN CHECK
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    posX = col * square_size + square_size//2

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (posX, 15), (posX, altura - 15), 15)


def draw_horizontal_winning_line(row, player):
    posY = row * square_size + square_size//2
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, posY), (largura - 15, posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, altura - 15), (largura - 15, 15), 15)


def draw_desc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, 15), (largura - 15, altura - 15), 15)


def restart():
    screen.fill(bg_color)
    draw_lines()
    player = 1
    # gamer_over = False
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0


draw_lines()

player = 1
gamer_over = False

# MAINLOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gamer_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // square_size)
            clicked_col = int(mouseX // square_size)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        gamer_over = True
                    player = player % 2 + 1

                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        gamer_over = True
                    player = 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                gamer_over = False

    pygame.display.update()
