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

    def __init__(self, radius, x, y, all_sprites, ball_sprite):
        # super().__init__(all_sprites)
        # self.add(ball_sprite)
        super().__init__(ball_sprite)
        self.radius = radius
        self.cnt = 0.001
        self.move = True
        self.image = pygame.Surface(
            (2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(
            "red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(0, 100) / 100
        self.vy = sqrt(1 - (self.vx ** 2))
        self.speed = 5 * (1 + self.cnt)
        self.k = False

    def update(self, width, platform_sprite, horizontal_border_bottom, horizontal_border_top,
               vertical_borders, victory, win):
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
        if pygame.sprite.spritecollideany(self, platform_sprite):
            self.vy = -self.vy
            self.cnt **= 2


class Platform(pygame.sprite.Sprite):

    def __init__(self, x1, y1, w, h, platform_sprite, group):
        super().__init__(platform_sprite)
        self.add(group)
        self.w = w
        self.h = h
        self.image = pygame.Surface([w, h])
        self.rect = pygame.Rect(x1, y1, w, h)
        self.speed = 5

    def update(self, k):
        if(k == -1 and self.rect.x >= 6):
            self.rect = self.rect.move(self.speed * k, 0)
        elif(k == 1 and self.rect.x + self.w <= 454):
            self.rect = self.rect.move(self.speed * k, 0)
