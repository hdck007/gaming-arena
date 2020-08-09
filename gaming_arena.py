##GAMING ARENA
import pygame
import os
import sys

pygame.mixer.init()
pygame.init()

screen_width = 900
screen_height = 600

yellow=(253,254,2)
orange=(254,154,0)
magenta=(255,0,255)
h=(102, 255, 255)

bg=pygame.image.load("bg3.png")
bg=pygame.transform.scale(bg,(screen_width,screen_height))

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("First Game")
pygame.display.update()
clock = pygame.time.Clock()
font=pygame.font.SysFont(None,65)

def text_screen(text,color, x, y):
    screen_text=font.render(text, True, color)
    screen.blit(screen_text,(int(x),int(y)))

def game_loop():
    exit_game = False
    game_over = False
    
    while not exit_game:
        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    exit_game = True   
        else:
            

            screen.blit(bg,(0,0))
            text_screen("*******HELLO GAMER*******",orange,185,130)
            text_screen("Select YOur Game",magenta,275,230)            
            text_screen("*Press 1 to ",h,70,400)
            text_screen(" play CONNECT ",h,30,460)
            text_screen(" Double Player ",yellow,40,520)
            text_screen("*Press 2 to",h,608,400)
            text_screen(" play SNAKE ",h,573,460)
            text_screen(" Single Player ",yellow,568,520)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        import connect0
                    if event.key == pygame.K_2:
                        import snake
        pygame.display.update()
    pygame.quit()
    quit()
pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play()
game_loop()


