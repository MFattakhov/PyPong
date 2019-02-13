import pygame
import random


class Border(pygame.sprite.Sprite):

    def __init__(self, x1, y1, x2, y2, all_sprites, group):
        super().__init__(all_sprites)
        self.add(group)
        if x1 == x2:
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Ball(pygame.sprite.Sprite):

    def __init__(self, radius, x, y, all_sprites, ball_sprite):
        # super().__init__(all_sprites)
        # self.add(ball_sprite)
        super().__init__(ball_sprite)
        self.radius = radius
        self.image = pygame.Surface(
            (2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(
            "red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)
        self.k = False

    def update(self, horizontal_border_bottom, horizontal_border_top, 
               vertical_borders, bottom_win, top_win, win):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
        if pygame.sprite.spritecollideany(self, horizontal_border_bottom):
            bottom_win(win)
        if pygame.sprite.spritecollideany(self, horizontal_border_top):
            top_win(win)
