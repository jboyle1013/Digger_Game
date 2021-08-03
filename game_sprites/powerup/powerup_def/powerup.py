import pygame
from game_vals.game_vals import *


class PowerUp(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Creates general shape, need to import image but it'll be black for now
        self.width = 40
        self.height = 40
        self.type = 'powerup'
        self.image = pygame.Surface( [self.width, self.height] )
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.active = False
        self.collect_time = 0
        self.curr_time = 0




