import pygame


def draw_window(win, ball_sprite, horizontal_border_bottom, horizontal_border_top,
				vertical_borders, bottom_win, top_win, clock, fps, *sprites):
    win.fill(pygame.Color('white'))
    for sprite in sprites:
        sprite.draw(win)
        sprite.update()
    ball_sprite.draw(win)
    ball_sprite.update(horizontal_border_bottom, horizontal_border_top,
                       vertical_borders, bottom_win, top_win, win)
    pygame.display.flip()
    clock.tick(fps)


def top_win(win):
    font = pygame.font.Font('fonts/Quicksand-Regular.ttf', 46)
    rendered = font.render('Top Win!\nPress space to restart!',
                           True, pygame.color.Color('white'))
    rect = rendered.get_rect()
    win.blit(rendered, rect)
    pygame.display.flip()


def bottom_win(win):
    font = pygame.font.Font('fonts/Quicksand-Regular.ttf', 46)
    rendered = font.render('Bottom Win!\nPress space to restart!',
                           True, pygame.color.Color('white'))
    rect = rendered.get_rect()
    win.blit(rendered, rect)
    pygame.display.flip()
