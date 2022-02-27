import os
import pygame
from consts import WIDTH, HEIGHT, IMAGE_INTERVAL
import glob
from random import randint


class AnimatedBackground:
    '''This class animating our background image'''

    def __init__(self):
        self.background = []
        self.background.append(pygame.Surface.convert(pygame.transform.scale(pygame.image.load(os.path.join(
            'Assets/images/animated_background', 'frame_0_delay-0.1s.png')), (WIDTH, HEIGHT))))
        self.background.append(pygame.Surface.convert(pygame.transform.scale(pygame.image.load(os.path.join(
            'Assets/images/animated_background', 'frame_1_delay-0.1s.png')), (WIDTH, HEIGHT))))
        self.background.append(pygame.Surface.convert(pygame.transform.scale(pygame.image.load(os.path.join(
            'Assets/images/animated_background', 'frame_2_delay-0.1s.png')), (WIDTH, HEIGHT))))
        self.background.append(pygame.Surface.convert(pygame.transform.scale(pygame.image.load(os.path.join(
            'Assets/images/animated_background', 'frame_3_delay-0.1s.png')), (WIDTH, HEIGHT))))
        self.current_img = 0
        self.background_image = self.background[self.current_img]
        self.last_update = 0

    def update(self):
        '''This function moving between images in a determined speed'''
        self.current_img += 0.2
        if self.current_img >= len(self.background):
            self.current_img = 0

        self.background_image = self.background[int(self.current_img)]


class Explosion:
    '''This class animating our explosion'''

    def __init__(self):
        self.is_exploding = False
        self.explosion = []
        for frame in range(0, 11):
            if frame < 10:
                self.explosion.append(pygame.transform.scale(pygame.image.load(os.path.join(
                    'Assets/images/explosion', f'frame_0{frame}_delay-0.1s.png')), (150, 150)))
            else:
                self.explosion.append(pygame.transform.scale(pygame.image.load(os.path.join(
                    'Assets/images/explosion', f'frame_{frame}_delay-0.1s.png')), (150, 150)))

        self.current_img = 0
        self.explosion_image = self.explosion[self.current_img]

    def update(self):
        '''This function moving between images in a determined speed'''
        self.current_img += 0.2
        if self.current_img >= len(self.explosion):
            self.current_img = 0
            self.is_exploding = False
        self.explosion_image = self.explosion[int(self.current_img)]


class Heart():
    '''This class creates a heart object in the game'''

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.heart_rectangle_objects = []
        self.heart = []
        self.index = 0
        self.temp_imgs = []
        self.load_images()
        self.current_img = self.heart[self.index]
        self.heart_drop = False
        self.heart_count = 0

    def spawn(self):
        if len(self.heart_rectangle_objects) == 0:
            if self.heart_drop == True:
                self.heart_rectangle_objects.append(pygame.Rect(
                    randint(0, WIDTH), -150, self.width, self.height))

    def load_images(self):
        l_imgs = glob.glob('Assets/images/heart/*')
        for img in l_imgs:
            if len(img) == len(l_imgs[0]):
                self.heart.append(pygame.Surface.convert_alpha(pygame.transform.scale(
                    pygame.image.load(img), (self.width, self.height))))
            else:
                self.temp_imgs.append(pygame.Surface.convert_alpha(pygame.transform.scale(
                    pygame.image.load(img), (self.width, self.height))))
        self.heart.extend(self.temp_imgs)
        self.index = 0

    def update(self):
        self.index += 0.2
        if self.index >= len(self.heart):
            self.index = 0
        self.current_img = self.heart[int(self.index)]
