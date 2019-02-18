import pygame
import sys
import random
import time
from funcs import draw_window, victory
from objects import Border, Ball, Platform

pygame.init()


def game():

    clock = pygame.time.Clock()

    fps = 120
    size = width, height = 460, 620
    win = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    horizontal_border_bottom = pygame.sprite.Group()
    horizontal_border_top = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    ball_sprite = pygame.sprite.Group()
    platform_sprite_bottom = pygame.sprite.Group()
    platform_sprite_top = pygame.sprite.Group()
    bg = pygame.image.load(f'bg/bg_{random.randint(1, 5)}.png')

    Border(5, 5, width - 5, 5, all_sprites, horizontal_border_top)
    Border(5, height - 5, width - 5, height - 5,
           all_sprites, horizontal_border_bottom)
    Border(5, 5, 5, height - 5, all_sprites, vertical_borders)
    Border(width - 5, 5, width - 5, height - 5, all_sprites,
           vertical_borders)

    ball = Ball(20, 100, 100, all_sprites, ball_sprite,
                platform_sprite_bottom, platform_sprite_top)

    run = False
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                run = True
        font = pygame.font.Font('fonts/Quicksand-Regular.ttf', 40)
        rendered = font.render('Press any key', True,
                               pygame.color.Color('white'))
        rect = rendered.get_rect()
        rect.y = 260
        rect.x = (width - rect.width) / 2
        win.blit(rendered, rect)
        pygame.display.flip()
        pygame.display.update()

    time.sleep(1)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(win, bg, width, ball_sprite, horizontal_border_bottom,
                    horizontal_border_top, vertical_borders, victory, clock, fps,
                    platform_sprite_bottom, platform_sprite_top, all_sprites)

        if ball.restart == True:
            return 0


if __name__ == "__main__":
    while True:
        game()

pygame.quit()
sys.exit()
