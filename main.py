import pygame
import random
import time

def reset_game():
    global start_time, hits, total_reaction_time, last_hit_time, average_reaction_time, target_x, target_y, show_button
    hits = 0
    total_reaction_time = 0
    last_hit_time = 0
    average_reaction_time = 0
    target_x = random.randint(0, SCREEN_WIDTH - target_width)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    start_time = time.time()
    show_button = False

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_DURATION = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ИГРА ТИР',"_target.png")
icon1 = pygame.image.load("_target.png")
#pygame.display.set_icon(icon1)

target = pygame.image.load("_target.png")
target_width = 80
target_height = 80

font = pygame.font.Font(None, 36)

# Кнопка "Еще раз" теперь будет находиться посредине окна
button_image = pygame.Surface((140, 50))
button_image.fill((0, 200, 0))
button_rect = button_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

hits = 0
total_reaction_time = 0
last_hit_time = 0
average_reaction_time = 0
start_time = time.time()

show_button = False

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

reset_game()
running = True

while running:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time >= GAME_DURATION:
        show_button = True

    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and show_button:
                reset_game()

    # Отрисовка мишени, если игра активна
    if not show_button:  # Если игра закончилась, мишень исчезает
        screen.blit(target, (target_x, target_y))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1
                reaction_time = current_time - last_hit_time if last_hit_time else 0
                total_reaction_time += reaction_time
                average_reaction_time = (total_reaction_time / hits) if hits else 0
                last_hit_time = current_time
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Отображаем кнопку "Еще раз", если игра закончилась
    if show_button:
        screen.blit(button_image, button_rect)
        draw_text('Еще раз', font, (255, 255, 255), screen, button_rect.x + 20, button_rect.y + 10)

    # Отображаем текущие результаты игры
    draw_text(f"Попаданий: {hits}", font, (0, 128, 0), screen, 5, 5)
    draw_text(f"Время реакции: {average_reaction_time:.2f} сек", font, (0, 128, 0), screen, 5, 40)

    pygame.display.update()

pygame.quit()