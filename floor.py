import glob
import pygame
import os


class Lava():
    '''This function returns animated lava, kinda useless honestly.'''

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rectangle = pygame.Rect(0, self.height, self.width, self.height)
        self.lava = []
        self.count = 0
        self.temp_imgs = []
        self.index = 0
        self.load_images()
        self.image = self.lava[self.index]

    def load_images(self):
        l_imgs = glob.glob('Assets/images/lava/*')
        for img in l_imgs:
            if len(img) == len(l_imgs[0]):
                self.lava.append(pygame.transform.scale(
                    pygame.image.load(img), (self.width, self.height)))
            else:
                self.temp_imgs.append(pygame.transform.scale(
                    pygame.image.load(img), (self.width, self.height)))
        self.lava.extend(self.temp_imgs)
        self.index = 0

    def update(self):
        self.count += 0.3
        if self.index == len(self.lava):
            self.index = 0
        self.image = self.lava[self.index]
        if self.count > 2:
            self.index += 1
            self.count = 0
