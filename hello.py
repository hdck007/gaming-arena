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

bg=pygame.image.load("bg5.png")
bg=pygame.transform.scale(bg,(screen_width,screen_height))

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("First Game")
pygame.display.update()
clock = pygame.time.Clock()
font=pygame.font.SysFont(None,55)

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
            text_screen("*******HELLO GAMER*******",orange,225,130)
            text_screen("Select YOur Game",magenta,295,230)            
            text_screen("*Press 1 to Play Again",h,250,350)
            text_screen("*Press 2 to go to main Menu",h,200,400)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        import connect
                    if event.key == pygame.K_2:
                        import gaming_arena
        pygame.display.update()
    pygame.quit()
    quit()
pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play()
game_loop()


