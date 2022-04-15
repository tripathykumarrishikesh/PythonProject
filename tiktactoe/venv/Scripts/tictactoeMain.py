import pygame, sys
import numpy as np

########### initializes pygame
pygame.init()

WIDTH=600
HEIGHT=WIDTH
BOARD_ROWS=3
BOARD_COLS=3
SQUARE_SIZE = WIDTH//BOARD_COLS
LINE_WIDTH=15

CIRCLE_RADUIS = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CROSS_WIDTH =25
SPACE = SQUARE_SIZE//4

RED=(255,0,0)
BG_COLOR=(28,170,156)
LINE_COLOR=(23,145,135)
CROSS_COLOR = (66,66,66)
CIRCLE_COLOR = (66,66,66)

######### GUI heading
pygame.display.set_caption('TIC TAC TOE');
################# GUI dimension
screen =pygame.display.set_mode((WIDTH,HEIGHT))

############## GUI Background
screen.fill(BG_COLOR)

############# Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))
print(board)


################ 4 lines in the game

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)


    pygame.draw.line(screen, LINE_COLOR, (0, 2*SQUARE_SIZE), (WIDTH, 2*SQUARE_SIZE), LINE_WIDTH)


    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)


    pygame.draw.line(screen, LINE_COLOR, (2*SQUARE_SIZE,0), (2*SQUARE_SIZE, HEIGHT), LINE_WIDTH)



################# marking of the square
def mark_Square(row,col,player):
    board[row][col] = player


############# is the square available??
def available_square(row,col):
    return board[row][col] == 0


#################### board status
def is_board_full():
    for row in range (BOARD_ROWS):
        for col in range (BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True
############## to draw O and X

def draw_figures():
    for row in range (BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle (screen, RED, (int(col*SQUARE_SIZE+SQUARE_SIZE//2), int(row*SQUARE_SIZE+SQUARE_SIZE//2)),CIRCLE_RADUIS,CIRCLE_WIDTH)
            elif board[row][col] ==2:
                pygame.draw.line(screen,CROSS_COLOR, (col * SQUARE_SIZE+SPACE, row*SQUARE_SIZE+SQUARE_SIZE-SPACE), (col*SQUARE_SIZE+SQUARE_SIZE-SPACE, row*SQUARE_SIZE+SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),(col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE +SQUARE_SIZE - SPACE), CROSS_WIDTH)

############  check win

def check_win(player):
    for col in range (BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_verticle_winning_line(col,player)
            return True


    for row in range (BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horzizontal_winning_line(row,player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


################  draw winning line
def draw_verticle_winning_line(col,player):
    posX = col * SQUARE_SIZE+SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line (screen, color, (posX, 15 ), (posX, HEIGHT - 15),15)

def draw_horzizontal_winning_line(row,player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15,posX), (WIDTH-15,posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15,HEIGHT-15), (WIDTH - 15,15),15 )

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT-15), 15)

################ restart game

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player =1
    for row in range (BOARD_ROWS):
        for col in range (BOARD_COLS):
            board[row][col] =0



########## main loop to create GUI
draw_lines()

game_over = False

player =1
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y

            ################# to return a specific value if mouse button clicked on the squares
            clicked_row =  int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)


            if available_square(clicked_row,clicked_col):
                mark_Square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                draw_figures()



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over =False

    pygame.display.update()