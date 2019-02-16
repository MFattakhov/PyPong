import pygame
import sys


def draw_window(win, width, ball_sprite, horizontal_border_bottom, horizontal_border_top,
                vertical_borders, victory, clock, fps,
                platform_sprite_bottom, platform_sprite_top, *sprites):
    win.fill(pygame.Color('white'))
    for sprite in sprites:
        sprite.draw(win)
        sprite.update()
    ball_sprite.draw(win)
    ball_sprite.update(width, horizontal_border_bottom, horizontal_border_top,
                       vertical_borders, victory, win, platform_sprite_bottom, platform_sprite_top)
    keys = pygame.key.get_pressed()
    platform_sprite_bottom.draw(win)
    platform_sprite_top.draw(win)
    if keys[pygame.K_LEFT]:
        platform_sprite_bottom.update(-1)
    if keys[pygame.K_RIGHT]:
        platform_sprite_bottom.update(1)
    if keys[pygame.K_a]:
        platform_sprite_top.update(-1)
    if keys[pygame.K_d]:
        platform_sprite_top.update(1)
    pygame.display.flip()
    clock.tick(fps)


def victory(win, who, width):
    font = pygame.font.Font('fonts/Quicksand-Regular.ttf', 40)
    text = [f'{who} Win!',
            'Press space to restart!']
    text_coord = 150
    for line in text:
        rendered = font.render(line,
                               True, pygame.color.Color('black'))
        text_coord += 10
        rect = rendered.get_rect()
        rect.top = text_coord
        rect.x = (width - rect.width) / 2
        text_coord += rect.height
        win.blit(rendered, rect)
        pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 0
