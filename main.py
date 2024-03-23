import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption('ИГРА ТИР')
icon1 = pygame.image.load("_hand.ico")
pygame.display.set_icon(icon1)

target = pygame.image.load("_target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH-target_width)   #SCREEN_WIDTH / 2
target_y = random.randint(0, SCREEN_HEIGHT-target_height)   #SCREEN_HEIGHT / 2


running = True

while running:
    pass

pygame.quit()
