import os
import pygame


WIDTH, HEIGHT = 1400, 1000

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

DESERT = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets/images', 'background1.jpg')), (WIDTH, HEIGHT))


LAUNCHER_IMG = pygame.Surface.convert_alpha(pygame.transform.scale(pygame.image.load(
    os.path.join('Assets/images', 'launcher.png')), (120, 150)))

BULLET_IMG = pygame.Surface.convert_alpha(pygame.transform.rotate(pygame.transform.scale(
    pygame.image.load(os.path.join('Assets/images', 'bullet.png')), (100, 80)), 90))

ROCK_IMG = pygame.Surface.convert_alpha(pygame.transform.scale(pygame.image.load(os.path.join('Assets/images',
                                                                                             'stone.png')), (80, 100)))

MAX_BULLETS = 3

GAME_NAME = 'My First Pygame!'

IMAGE_INTERVAL = 100
