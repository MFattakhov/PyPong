import pygame
import sys
import random
from funcs import draw_window, bottom_win, top_win
from objects import Border, Ball

pygame.init()
clock = pygame.time.Clock()

fps = 30
size = width, height = 460, 720
win = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_border_bottom = pygame.sprite.Group()
horizontal_border_top = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
ball_sprite = pygame.sprite.Group()

Border(5, 5, width - 5, 5, all_sprites, horizontal_border_top)
Border(5, height - 5, width - 5, height - 5,
       all_sprites, horizontal_border_bottom)
Border(5, 5, 5, height - 5, all_sprites, vertical_borders)
Border(width - 5, 5, width - 5, height - 5, all_sprites,
       vertical_borders)

Ball(20, 100, 100, all_sprites, ball_sprite)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_window(win, ball_sprite, horizontal_border_bottom, horizontal_border_top,
				vertical_borders, bottom_win, top_win, clock, fps, all_sprites)

pygame.quit()
sys.exit()
