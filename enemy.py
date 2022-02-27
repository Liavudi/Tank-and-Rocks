from consts import *
from random import randint


class Enemy():
    '''This class is our enemy object'''

    def __init__(self, img, falling_speed: int):
        self.img = img
        self.enemies = []
        self.max_enemies = 1
        self.add_enemy = 100
        self.falling_speed = falling_speed
        self.next_level = 500

    def spawn(self):
        '''This function spawns our enemy at random location on the sky'''
        if len(self.enemies) < self.max_enemies:
            self.enemies.append(pygame.Rect(
                randint(0, WIDTH), -100, ROCK_IMG.get_width(), ROCK_IMG.get_height()))

    def handle_enemy(self):
        '''This function controls our enemy falling speed'''
        for falling_enemies in self.enemies:
            falling_enemies.y += self.falling_speed

    def despawn(self):
        '''This function removes our enemy if falling from the scene height'''
        for falling_enemies in self.enemies:
            if falling_enemies.y > HEIGHT:
                self.enemies.remove(falling_enemies)

    def levelup(self, score: list):

        if score[0] >= self.next_level:
            self.falling_speed += 1
            self.next_level += 500
        if score[0] >= self.add_enemy:
            self.max_enemies += 1
            self.add_enemy += 300
            if self.max_enemies >= 10:
                self.max_enemies = 10
