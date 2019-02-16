import pygame
import sys
import random
from math import sqrt


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

    def __init__(self, radius, x, y, all_sprites, ball_sprite,
                 platform_sprite_bottom, platform_sprite_top):
        # super().__init__(all_sprites)
        # self.add(ball_sprite)
        super().__init__(ball_sprite)
        self.radius = radius
        self.cnt = 1 / 3
        self.move = True
        self.image = pygame.Surface(
            (2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(
            "red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = 0
        self.vy = 1
        self.speed = 4
        self.k = False
        self.bot_platform = Platform(
            172, 600, platform_sprite_bottom)
        self.top_platform = Platform(
            172, 10, platform_sprite_top)

    def update(self, width, horizontal_border_bottom, horizontal_border_top,
               vertical_borders, victory, win, platform_sprite_bottom, platform_sprite_top):
        if self.move:
            self.rect = self.rect.move(
                self.vx * self.speed, self.vy * self.speed)
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
        if pygame.sprite.spritecollideany(self, horizontal_border_bottom):
            self.move = False
            victory(win, 'Top', width)
        if pygame.sprite.spritecollideany(self, horizontal_border_top):
            self.move = False
            victory(win, 'Bottom', width)
        if pygame.sprite.spritecollideany(self, platform_sprite_top):
            self.speed += self.cnt
            self.vx = (((self.rect.x + 20) - (self.top_platform.rect.x + 61.5)) / 61.5) * 0.8
            self.vy = sqrt(1 - (self.vx ** 2))
        if pygame.sprite.spritecollideany(self, platform_sprite_bottom):
            self.speed += self.cnt
            self.vx = (((self.rect.x + 20) - (self.bot_platform.rect.x + 61.5)) / 61.5) * 0.8
            self.vy = -sqrt(1 - (self.vx ** 2))


class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = pygame.image.load('images/rectangle.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self, k):
        if(k == -1 and self.rect.x >= 8):
            self.rect = self.rect.move(self.speed * k, 0)
        elif(k == 1 and self.rect.x + 119 <= 450):
            self.rect = self.rect.move(self.speed * k, 0)
