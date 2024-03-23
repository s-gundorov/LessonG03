import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption('ИГРА ТИР')
icon1 = pygame.image.load("_hand.ico")
pygame.display.set_icon(icon1)

running = True

while running:
    pass

pygame.quit()
