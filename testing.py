import pygame
from floor import Floor

pygame.init()

WIN = pygame.display.set_mode((1400, 1000))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        key_pressed = pygame.key.get_pressed()


    pygame.display.flip()
