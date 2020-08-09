## SNAKE GAME

import pygame
import random
import os
import sys

pygame.mixer.init()
pygame.init()

red=(255,0,0)
blue=(0,0,255)
green=(0, 255, 0)
yellow=(255,255,0)
orange=(254,154,0)
navyblue=(25,25,112)
brown=(139,37,0)
magenta=(255,0,255)
purple=(160,34,240)
silver=(219,219,219)
gold=(184,134,11)
h=(102, 255, 255)
white=(255,255,255)
grey=(150,150,200)
black=(0,0,0)
bomb=(0, 0, 255)
screen_width = 900
screen_height = 600

bg=pygame.image.load("bg4.png")
bg=pygame.transform.scale(bg,(screen_width,screen_height))

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("First Game")
pygame.display.update()
clock = pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def text_screen(text,color, x, y):
    screen_text=font.render(text, True, color)
    screen.blit(screen_text,(int(x),int(y)))

def plot_snake(screen,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.circle(screen,color,[x,y,],snake_size)

def game_loop():
    exit_game = False
    game_over = False
    snake_x = 10
    snake_y = 500
    speed_x=0
    speed_y=0
    food_x = random.randint(0,screen_width)
    food_y = random.randint(0,screen_height)
    foodb_x = random.randint(0,screen_width)
    foodb_y = random.randint(0,screen_height)
    foodd_x = random.randint(0,screen_width)
    foodd_y = random.randint(0,screen_height)
    bush1_x = random.randint(50,400)
    bush1_y = random.randint(50,300)
    bush1l_x=bush1_x-3
    bush1l_y=bush1_y+15
    bush1r_x=bush1_x+32
    bush1r_y=bush1_y+15
    bush2_x = random.randint(600,830)
    bush2_y = random.randint(50,330)
    bush3_x = random.randint(50,150)
    bush3_y = random.randint(450,530)
    bush4_x = random.randint(300,850)
    bush4_y = random.randint(400,500)
    bush4a_x=bush4_x+15
    bush4a_y=bush4_y+1
    bush4b_x=bush4_x+15
    bush4b_y=bush4_y+32
    bush1_size = 30
    bush2_size = 30
    bush3_size = 30
    bush4_size = 30
    snake_size = 12
    food_size=17
    bush_color=brown
    fps = 30
    score=0
    x=0
    pause=False

    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as a:
            a.write("0")
    with open("highscore.txt","r") as a:
        highscore=a.read()
    speed =8
    snk_list=[]
    snk_length =1

    while not exit_game:
        if game_over:
            a=open("highscore.txt","w")
            a.write(str(highscore))
            screen.fill(black)
            text_screen("*****Game Over*****",orange,300,180)
            text_screen("Press ENTER to Play Again",h,210,250)            
            text_screen("Score: "+ str(score),white,235,320)
            text_screen("HighScore: "+ str(highscore),white,445,320)
            text_screen("Press 2 to go Main Menu",h,235,390)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    exit_game = True   

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("mid2.mp3")
                        pygame.mixer.music.play()
                        game_loop()

                    if event.key == pygame.K_2:
                        import gaming_arena.py
        else:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:   
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        speed_x=speed
                        speed_y=0
                    if event.key == pygame.K_LEFT:
                        speed_x=-speed
                        speed_y=0                
                    if event.key == pygame.K_UP:
                        speed_x=0
                        speed_y=-speed               
                    if event.key == pygame.K_DOWN:
                        speed_x=0
                        speed_y=speed
                    if event.key == pygame.K_p:
                        pause=True
            if pause==False:
                pygame.time.delay(0)
            else:
                text_screen("Paused for 5 Sec ",red,290,270)
                pygame.display.update()
                pygame.time.delay(5000)
                pause=False

            snake_x = snake_x + speed_x
            snake_y = snake_y + speed_y

            if abs (snake_x-foodb_x)<18 and (snake_x-foodb_x)>-13 and (snake_y-foodb_y)<19 and (snake_y-foodb_y)>-13:
                score+=50
                foodb_x = random.randint(20,screen_width/1.2)
                foodb_y = random.randint(20,screen_height/1.2)
                foodd_x = random.randint(0,screen_width)
                foodd_y = random.randint(0,screen_height)
                snk_length+=20
                speed-=2                
                if score > int(highscore):
                    highscore=score

            if abs (snake_x-food_x)<18 and (snake_x-food_x)>-13 and (snake_y-food_y)<19 and (snake_y-food_y)>-13:
                score+=10
                x=0
                food_x = random.randint(20,screen_width/1.2)
                food_y = random.randint(20,screen_height/1.2)
                snk_length+=10
                speed+=1
                if score > int(highscore):
                    highscore=score
                    


            if abs (snake_x-foodd_x)<18 and (snake_x-foodd_x)>-13 and (snake_y-foodd_y)<19 and (snake_y-foodd_y)>-13 or (snake_x-bush4a_x)<16 and (snake_x-bush4a_x)>-16 and (snake_y-bush4a_y)<16 and (snake_y-bush4a_y)>-16 or (snake_x-bush4b_x)<16 and (snake_x-bush4b_x)>-16 and (snake_y-bush4b_y)<16 and (snake_y-bush4b_y)>-16 or (snake_x-bush1r_x)<16 and (snake_x-bush1r_x)>-16 and (snake_y-bush1r_y)<16 and (snake_y-bush1r_y)>-16 or (snake_x-bush1l_x)<16 and (snake_x-bush1l_x)>-16 and (snake_y-bush1l_y)<16 and (snake_y-bush1l_y)>-16 or (snake_x-bush1_x)<33 and (snake_x-bush1_x)>-13 and (snake_y-bush1_y)<35 and (snake_y-bush1_y)>-13 or (snake_x-bush2_x)<33 and (snake_x-bush2_x)>-13 and (snake_y-bush2_y)<35 and (snake_y-bush2_y)>-13 or abs (snake_x-bush3_x)<33 and (snake_x-bush3_x)>-13 and (snake_y-bush3_y)<35 and (snake_y-bush3_y)>-13 or (snake_x-bush4_x)<33 and (snake_x-bush4_x)>-13 and (snake_y-bush4_y)<35 and (snake_y-bush4_y)>-13:
                game_over=True
                pygame.mixer.music.load("crash.mp3")
                pygame.mixer.music.play()

            screen.blit(bg,(0,0))
            text_screen("Score "+str(score),yellow,0,0)
            colorss = [white, black, silver, gold, red, blue, green, yellow, magenta, brown]
            bonus_color = random.choice(colorss)

            if score%40!=0:
                pygame.draw.rect(screen, red , [food_x , food_y, food_size, food_size])   
            else:
                if x<300:
                    pygame.draw.rect(screen, bonus_color , [foodb_x , foodb_y, food_size, food_size])
                    pygame.draw.rect(screen, bomb , [foodd_x , foodd_y, food_size, food_size])
                    x+=1
                else:
                    score-=30
                
            pygame.draw.rect(screen, bush_color , [bush1_x , bush1_y, bush1_size, bush1_size])
            pygame.draw.circle(screen, bush_color , [bush1l_x , bush1l_y], int(bush1_size/2))
            pygame.draw.circle(screen, bush_color , [bush1r_x , bush1r_y],int(bush1_size/2))
            pygame.draw.rect(screen, bush_color , [bush2_x , bush2_y, bush2_size, bush2_size])
            pygame.draw.rect(screen, bush_color , [bush3_x , bush3_y, bush3_size, bush3_size])
            pygame.draw.rect(screen, bush_color , [bush4_x , bush4_y, bush4_size, bush4_size])
            pygame.draw.circle(screen, bush_color , [bush4a_x , bush4a_y], int(bush4_size/2))
            pygame.draw.circle(screen, bush_color , [bush4b_x , bush4b_y],int(bush4_size/2))
            
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1] or snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load("crash.mp3")
                pygame.mixer.music.play()

            plot_snake(screen,navyblue,snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
pygame.mixer.music.load("mid2.mp3")
pygame.mixer.music.play()
game_loop()
