import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption('ИГРА ТИР')
icon1 = pygame.image.load("_hand.ico")
pygame.display.set_icon(icon1)

target = pygame.image.load("target.ico")
target_width = 50
target_height = 50
target_x = SCREEN_WIDTH
target_y = SCREEN_HEIGHT


running = True

while running:
    pass

pygame.quit()
