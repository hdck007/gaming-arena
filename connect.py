import numpy as np
import pygame
import sys
import math
import os
pygame.mixer.init()
pygame.init()
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
WHITE = (255 , 255, 255)
ORANGE = (255, 128,0)
PURPLE = (255,0,255)
magenta=(102, 255, 255)

PLAYER1_COLOR = BLACK
PLAYER2_COLOR = BLACK

PLAYER1_SCORE = 0
PLAYER2_SCORE = 0

ROW_COUNT = 6
COLUMN_COUNT = 7

timer_select_font = pygame.font.SysFont("monospace", 30)

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
##    print(np.flip(board, 0))
    print(1)

valid = 0

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def is_draw(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			if board[r][c] == 0:
				return False
	return True			
	

def draw_board(board, PLAYER1_COLOR, PLAYER2_COLOR):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):      
            if board[r][c] == 1:
                pygame.draw.circle(screen, PLAYER1_COLOR, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, PLAYER2_COLOR, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


board = create_board()
print_board(board)

pygame.init()

SQUARESIZE = 100

width = (COLUMN_COUNT+1)* (SQUARESIZE+1)
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
selectfont = pygame.font.SysFont("monospace", 22)
timerfont = pygame.font.SysFont("monospace", 35)
label = selectfont.render("Player 1 Select A Colour", 1, WHITE)
screen.blit(label, (40,10))
menu_font = pygame.font.SysFont("monospace", 15)
pygame.display.update()
done = True
while done:
    choice = 0
    c = 3
    label = selectfont.render("Player 1 Select A Colour", 1, WHITE)
    screen.blit(label, (40,10))
    label = selectfont.render("Click 1 for Red:", 1, RED)
    screen.blit(label, (30,130))
    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(0*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    label = selectfont.render("Click 2 for Yellow:", 1, YELLOW)
    screen.blit(label, (30,230))
    pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), int(1*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    label = selectfont.render("Click 3 for Green:", 1, GREEN)
    screen.blit(label, (30,330))
    pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE+SQUARESIZE/2), int(2*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    label = selectfont.render("Click 4 for White:", 1, WHITE)
    screen.blit(label, (30,430))
    pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), int(3*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    label = selectfont.render("Click 5 for Orange:", 1, ORANGE)
    screen.blit(label, (30,530))
    pygame.draw.circle(screen, ORANGE, (int(c*SQUARESIZE+SQUARESIZE/2), int(4*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    label = selectfont.render("Click 6 for Purple:", 1, PURPLE)
    screen.blit(label, (30,630))
    pygame.draw.circle(screen, PURPLE, (int(c*SQUARESIZE+SQUARESIZE/2), int(5*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                PLAYER1_COLOR = RED
                done = False
                choice = 1
                chosen = 1
            if event.key == pygame.K_2:
                PLAYER1_COLOR = YELLOW
                done = False
                choice = 1
                chosen = 2
            if event.key == pygame.K_3:
                PLAYER1_COLOR = GREEN
                done = False
                choice = 1
                chosen = 3
            if event.key == pygame.K_4:
                PLAYER1_COLOR = WHITE
                done = False
                choice = 1
                chosen = 4
            if event.key == pygame.K_5:
                PLAYER1_COLOR = ORANGE
                done = False
                choice = 1
                chosen = 5
            if event.key == pygame.K_6:
                PLAYER1_COLOR = PURPLE
                done = False
                choice = 1
                chosen = 6
    pygame.display.update()
    if choice:
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT+1):
                pygame.draw.rect(screen, BLACK, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))           
    while choice:
        c = 3
        label = selectfont.render("Player 2 Select A Colour", 1, WHITE)
        screen.blit(label, (40,10))
        if PLAYER1_COLOR == RED:
            label = selectfont.render("Player One's Color:", 1, RED)
            screen.blit(label, (30,130))
            pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(0*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        else:
            label = selectfont.render("Click 1 for RED:", 1, RED)
            screen.blit(label, (30,130))
            pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(0*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)        
        if PLAYER1_COLOR == YELLOW:
            label = selectfont.render("Player One's Color:", 1, YELLOW)
            screen.blit(label, (30,230))
            pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), int(1*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        else:
            label = selectfont.render("Click 2 for Yellow:", 1, YELLOW)
            screen.blit(label, (30,230))
            pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), int(1*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        if PLAYER1_COLOR == GREEN:
            choosen = 1
            label = selectfont.render("Player One's Color:", 1, GREEN)
            screen.blit(label, (30,330))
            pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE+SQUARESIZE/2), int(2*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        else:
            label = selectfont.render("Click 3 for Green:", 1, GREEN)
            screen.blit(label, (30,330))
            pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE+SQUARESIZE/2), int(2*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        if PLAYER1_COLOR == WHITE:
            choosen = 1
            label = selectfont.render("Player One's Color:", 1, WHITE)
            screen.blit(label, (30,430))
            pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), int(3*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        else:
            label = selectfont.render("Click 4 for White:", 1, WHITE)
            screen.blit(label, (30,430))
            pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), int(3*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        if PLAYER1_COLOR == ORANGE:
            label = selectfont.render("Player One's Color:", 1, ORANGE)
            screen.blit(label, (30,530))
            pygame.draw.circle(screen, ORANGE, (int(c*SQUARESIZE+SQUARESIZE/2), int(4*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        else:
            label = selectfont.render("Click 5 for Orange:", 1, ORANGE)
            screen.blit(label, (30,530))
            pygame.draw.circle(screen, ORANGE, (int(c*SQUARESIZE+SQUARESIZE/2), int(4*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        if PLAYER1_COLOR == PURPLE:
            label = selectfont.render("Player One's Color:", 1, PURPLE)
            screen.blit(label, (30,630))
            pygame.draw.circle(screen, PURPLE, (int(c*SQUARESIZE+SQUARESIZE/2), int(5*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        else:
            label = selectfont.render("Click 6 for Purple:", 1, PURPLE)
            screen.blit(label, (30,630))
            pygame.draw.circle(screen, PURPLE, (int(c*SQUARESIZE+SQUARESIZE/2), int(5*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and chosen!=1:
                    PLAYER2_COLOR = RED
                    done = False
                    choice = 0
                if event.key == pygame.K_2 and chosen!=2:
                    PLAYER2_COLOR = YELLOW
                    choice = 0
                if event.key == pygame.K_3 and chosen!=3:
                    PLAYER2_COLOR = GREEN
                    choice = 0
                if event.key == pygame.K_4 and chosen!=4:
                    PLAYER2_COLOR = WHITE
                    done = False
                    choice = 0
                if event.key == pygame.K_5 and chosen!=5:
                    PLAYER2_COLOR = ORANGE
                    done = False
                    choice = 0
                if event.key == pygame.K_6 and chosen!=6:
                    PLAYER2_COLOR = PURPLE
                    done = False
                    choice = 0                          
        
    
        pygame.display.update() 
    
    pygame.display.update()

for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT+1):
        pygame.draw.rect(screen, BLACK, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))

label = timer_select_font.render("Select a Timer", 1, WHITE)
screen.blit(label , (280 , 50))
pygame.display.update()
selected = False
while  not selected:
    pygame.draw.rect(screen, magenta, (220, 200, SQUARESIZE, SQUARESIZE)) 
    pygame.draw.rect(screen, magenta, (550, 200 , SQUARESIZE, SQUARESIZE))
    pygame.draw.rect(screen, magenta, (220, 500, SQUARESIZE, SQUARESIZE))
    pygame.draw.rect(screen, magenta, (550, 500, SQUARESIZE, SQUARESIZE)) 
    label = timer_select_font.render("5sec", 1, BLACK)
    screen.blit(label , (230 , 230))
    label = timer_select_font.render("10sec", 1, BLACK)
    screen.blit(label , (560 , 230))
    label = timer_select_font.render("15sec", 1, BLACK)
    screen.blit(label , (230 , 530))
    label = timer_select_font.render("20sec", 1, BLACK)
    screen.blit(label , (555 , 530))
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            cor = e.pos
            if (cor[0] >=220 and cor[0]<=320) and (cor[1]>=200 and cor[1]<=300):
                timer_time = 5
                selected = True
            if (cor[0] >=550 and cor[0]<=650) and (cor[1]>=200 and cor[1]<=300):
                timer_time = 10
                selected = True
            if (cor[0] >=230 and cor[0]<=330) and (cor[1]>=530 and cor[1]<=630):
                timer_time = 15
                selected = True
            if (cor[0] >=555 and cor[0]<=655) and (cor[1]>=530 and cor[1]<=630):
                timer_time = 20
                selected = True
    pygame.display.update()

for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT+1):
        pygame.draw.rect(screen, BLACK, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
label = timer_select_font.render("Select number of Games", 1, WHITE)
screen.blit(label , (240 , 50))
pygame.display.update()
times=False
while  not times:
    pygame.draw.rect(screen, magenta, (220, 200, SQUARESIZE, SQUARESIZE)) 
    pygame.draw.rect(screen, magenta, (550, 200 , SQUARESIZE, SQUARESIZE))
    pygame.draw.rect(screen, magenta, (220, 500, SQUARESIZE, SQUARESIZE))
    label = timer_select_font.render("1", 1, BLACK)
    screen.blit(label , (260 , 230))
    label = timer_select_font.render("3", 1, BLACK)
    screen.blit(label , (590 , 230))
    label = timer_select_font.render("5", 1, BLACK)
    screen.blit(label , (260 , 530))
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            cor = e.pos
            if (cor[0] >=220 and cor[0]<=320) and (cor[1]>=200 and cor[1]<=300):
                game_time = 1
                times = True
            if (cor[0] >=550 and cor[0]<=650) and (cor[1]>=200 and cor[1]<=300):
                game_time = 3
                times = True
            if (cor[0] >=230 and cor[0]<=330) and (cor[1]>=530 and cor[1]<=630):
                game_time = 5
                times = True
    pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)
def game(round_no):
    global PLAYER1_SCORE
    global PLAYER2_SCORE
    global board
    game_over = False
    turn = 0
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT+1):
            pygame.draw.rect(screen, BLACK, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))

    draw_board(board, PLAYER1_COLOR, PLAYER2_COLOR)

    myfont = pygame.font.SysFont("monospace", 75)

    pygame.display.update()


    while not game_over:

        pygame.draw.rect(screen, BLACK, (700, 0,SQUARESIZE,SQUARESIZE))
        pygame.draw.rect(screen, BLACK, (700, 100,SQUARESIZE,SQUARESIZE))
        pygame.draw.rect(screen, BLACK, (700, 500,SQUARESIZE,SQUARESIZE))        
        pointfont = pygame.font.SysFont("monospace", 22)
        label = pointfont.render("ROUND", 1, WHITE)
        screen.blit(label, (720,20))
        label = pointfont.render(str(round_no), 1, WHITE)
        screen.blit(label, (750,45))
        label = pointfont.render("Player1", 1, PLAYER1_COLOR)
        screen.blit(label, (720,120))
        label = pointfont.render("Score", 1, PLAYER1_COLOR)
        screen.blit(label, (720,145))
        label = pointfont.render("Player2", 1, PLAYER2_COLOR)
        screen.blit(label, (720,520))
        label = pointfont.render("Score", 1, PLAYER2_COLOR)
        screen.blit(label, (720,545))
        pygame.draw.rect(screen, BLACK, (700, 200,SQUARESIZE,SQUARESIZE))
        pygame.draw.rect(screen, BLACK, (700, 600,SQUARESIZE,SQUARESIZE))    
        label = timerfont.render(str(PLAYER1_SCORE), 1, PLAYER1_COLOR)
        screen.blit(label, (720,220))
        label = timerfont.render(str(PLAYER2_SCORE), 1, PLAYER2_COLOR)
        screen.blit(label, (720,620))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if turn == 0:
                Play = True
                start_time = pygame.time.get_ticks()
                seconds = 0
                pygame.draw.rect(screen, BLACK, (0*SQUARESIZE, 0*SQUARESIZE, SQUARESIZE*7, SQUARESIZE))
                label = myfont.render("Player1's Turn", 1, PLAYER1_COLOR)
                screen.blit(label, (40,10))
                while Play:
                    for e in pygame.event.get():
                        if e.type == pygame.MOUSEBUTTONDOWN:
                            posx = e.pos[0]
                            col = int(math.floor(posx/SQUARESIZE))
                            if is_valid_location(board, col):
                                row = get_next_open_row(board, col)
                                drop_piece(board, row, col, 1)
                                if winning_move(board, 1):
                                    PLAYER1_SCORE += 1
                                    pygame.draw.rect(screen, BLACK, (0*SQUARESIZE, 0*SQUARESIZE, SQUARESIZE*7, SQUARESIZE))
                                    label = myfont.render("Player 1 wins!!", 1, PLAYER1_COLOR)
                                    screen.blit(label, (40,10))
                                    game_over = True    
                                Play = False            
                            if is_draw(board):
                                pygame.draw.rect(screen, BLACK, (0*SQUARESIZE, 0*SQUARESIZE, SQUARESIZE*7, SQUARESIZE)) 
                                label = myfont.render("DRAW!!", 1, WHITE)
                                screen.blit(label, (40,10))
                                game_over=True
                                Play=False
                                     
                    seconds = (pygame.time.get_ticks()-start_time)/1000
                    pygame.draw.rect(screen, BLACK, (700, 300,SQUARESIZE,SQUARESIZE))
                    label = timerfont.render(str(int(timer_time-seconds+1)), 1, PLAYER1_COLOR)
                    screen.blit(label, (750,350))
                    if (int(seconds) > timer_time):
                        Play = False
                    pygame.display.update()
            
            else:
                Play = True
                start_time = pygame.time.get_ticks()
                seconds = 0
                pygame.draw.rect(screen, BLACK, (0*SQUARESIZE, 0*SQUARESIZE, SQUARESIZE*7, SQUARESIZE)) 
                label = myfont.render("Player2's Turn", 1, PLAYER2_COLOR)
                screen.blit(label, (40,10))
                while Play:
                    for e in pygame.event.get():
                        if e.type == pygame.MOUSEBUTTONDOWN:
                            posx = e.pos[0]
                            col = int(math.floor(posx/SQUARESIZE))
                            if is_valid_location(board, col):
                                row = get_next_open_row(board, col)
                                drop_piece(board, row, col, 2)
                                if winning_move(board, 2):
                                    PLAYER2_SCORE += 1
                                    pygame.draw.rect(screen, BLACK, (0*SQUARESIZE, 0*SQUARESIZE, SQUARESIZE*7, SQUARESIZE)) 
                                    label = myfont.render("Player 2 wins!!", 1, PLAYER2_COLOR)
                                    screen.blit(label, (40,10))
                                    game_over = True    
                                Play = False            
                            if is_draw(board):
                                pygame.draw.rect(screen, BLACK, (0*SQUARESIZE, 0*SQUARESIZE, SQUARESIZE*7, SQUARESIZE)) 
                                label = myfont.render("DRAW!!", 1, WHITE)
                                screen.blit(label, (40,10))
                                game_over=True
                                Play=False


                    seconds = (pygame.time.get_ticks()-start_time)/1000
                    pygame.draw.rect(screen, BLACK, (700, 300,SQUARESIZE,SQUARESIZE))
                    label = timerfont.render(str(int(timer_time-seconds+1)), 1, PLAYER2_COLOR)
                    screen.blit(label, (750,350))
                    if (int(seconds) > timer_time):
                        Play = False
                        break                   
                    pygame.display.update()                                                                             

            print_board(board)
            draw_board(board, PLAYER1_COLOR, PLAYER2_COLOR)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(2000)
                print(i)
                board = create_board()
                break


for i in range(game_time):
    game(i+1) 
    
for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT+1):
        pygame.draw.rect(screen, BLACK, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
display = True
while display:
    BARSIZE = 50
    pygame.draw.rect(screen, PLAYER1_COLOR,(40,400,BARSIZE*PLAYER1_SCORE,BARSIZE))
    pygame.draw.rect(screen, PLAYER2_COLOR,(40,450,BARSIZE*PLAYER2_SCORE,BARSIZE))      
        

    
    if PLAYER1_SCORE > PLAYER2_SCORE :
        label = myfont.render("Player 1 wins by ", 1, PLAYER1_COLOR)
        screen.blit(label, (40,200))
        msg = str(PLAYER1_SCORE)+"-"+str(PLAYER2_SCORE)
        winin = myfont.render(msg , 1, WHITE)   
        screen.blit(winin, (320,320))
        pygame.display.update()
        pygame.time.wait(3000)
        display = False
        import hello
    elif PLAYER1_SCORE < PLAYER2_SCORE:
        label = myfont.render("Player 2 wins by ", 1, PLAYER2_COLOR)
        screen.blit(label, (40,200))
        msg = str(PLAYER2_SCORE)+"-"+str(PLAYER1_SCORE)
        winin = myfont.render(msg , 1, WHITE)
        screen.blit(winin, (320,320))
        pygame.display.update()
        pygame.time.wait(3000)
        display = False
        import hello
    else:
        label = myfont.render("******DRAW******", 1, PLAYER2_COLOR)
        screen.blit(label, (40,200))
        msg = str(PLAYER2_SCORE)+"-"+str(PLAYER1_SCORE)
        winin = myfont.render(msg , 1, WHITE)
        screen.blit(winin, (320,320))
        pygame.display.update()
        pygame.time.wait(3000)
        display = False
        import hello
    pygame.display.update()   
