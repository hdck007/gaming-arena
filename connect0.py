##GAMING ARENA
import pygame
import os
import sys

pygame.mixer.init()
pygame.init()

screen_width = 900
screen_height = 600

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

bg=pygame.image.load("bg3.png")
bg=pygame.transform.scale(bg,(screen_width,screen_height))

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("First Game")
pygame.display.update()
clock = pygame.time.Clock()
font=pygame.font.SysFont(None,75)

def text_screen(text,color, x, y):
    screen_text=font.render(text, True, color)
    screen.blit(screen_text,(int(x),int(y)))

def tut1():
    screen_width = 900
    screen_height = 600

    bg=pygame.image.load("b3.png")
    bg=pygame.transform.scale(bg,(screen_width,screen_height))
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.blit(bg,(0,0))
    pygame.display.update()
    pygame.time.wait(3500)

    bg=pygame.image.load("b2.png")
    bg=pygame.transform.scale(bg,(screen_width,screen_height))
    screen.blit(bg,(0,0))
    pygame.display.update()
    pygame.time.wait(3500)

    bg=pygame.image.load("b1.png")
    bg=pygame.transform.scale(bg,(screen_width,screen_height))
    screen.blit(bg,(0,0))
    pygame.display.update()
    pygame.time.wait(3500)

    bg=pygame.image.load("b4.png")
    bg=pygame.transform.scale(bg,(screen_width,screen_height))
    screen.blit(bg,(0,0))
    pygame.display.update()
    pygame.time.wait(3500)

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
            text_screen("*******HELLO GAMER*******",orange,140,150)
            text_screen("Welcome To Connect-4",yellow,200,230)
            text_screen("**Press 1 For Tutorial ",green,220,310)
            text_screen("**Press 2 To Skip Tutorial",green,170,390)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        tut1()
                    if event.key == pygame.K_2:
                        import connect
        pygame.display.update()
    pygame.quit()
    quit()
pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play()
game_loop()


