import pygame
from consts import LAUNCHER_IMG


class Player():
    '''This class handles our player'''

    def __init__(self, img, left_key, right_key, screen_size):
        self.rectangle = pygame.Rect(
            0, 850, LAUNCHER_IMG.get_width(), LAUNCHER_IMG.get_height())
        self.img = img
        self.left_key = left_key
        self.right_key = right_key
        self.vel = 5
        self.bullet_vel = 10
        self.screen_size_width = screen_size[0]
        self.screen_size_height = screen_size[1]
        self.bullets = []
        self.health = 100
        self.not_moving = 0
        self_count = 0

    def handle_movement(self, key_pressed: list):
        '''This function handles our player movement: direction, which key on the keyboard and movement speed'''
        if key_pressed[self.left_key] and self.rectangle.x < self.screen_size_width - 120:
            self.rectangle.x += self.vel
            self.not_moving = pygame.time.get_ticks()

        if key_pressed[self.right_key] and self.rectangle.x > 0:
            self.rectangle.x -= self.vel
            self.not_moving = pygame.time.get_ticks()

    def handle_bullet(self):
        '''This function handles our bullet, direction, speed and what happens when it leaves the screen'''
        for b in self.bullets:
            b.y -= self.bullet_vel
            if b.y < -30:
                self.bullets.remove(b)
