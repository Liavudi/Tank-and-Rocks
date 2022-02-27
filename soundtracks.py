import pygame
import os
pygame.mixer.pre_init()



class SoundTrack:
    '''This class is our in game sound'''

    def background():
        return pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join('Assets/soundeffects', 'Marimba Boy.wav')), -1)

    def second_background():
        return pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join('Assets/soundeffects', 'Free Game Loop.wav')), -1)

    def starting_background():
        return pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join('Assets/soundeffects', 'mixkit-close-sea-waves-loop-1195.wav')), -1)

    def gunshot():
        return pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join('Assets/soundeffects', 'gunshot.mp3')))

    def playerhit():
        return pygame.mixer.Channel(2).play(pygame.mixer.Sound(os.path.join('Assets/soundeffects', 'HitSound.wav')))

    def enemyhit():
        return pygame.mixer.Channel(3).play(pygame.mixer.Sound(os.path.join('Assets/soundeffects', 'explode.wav')))

    def collect():
        return pygame.mixer.Channel(4).play(pygame.mixer.Sound(os.path.join('Assets/soundeffects', 'zapsplat_multimedia_alert_action_collect_pick_up_point_or_item_79293.mp3')))
