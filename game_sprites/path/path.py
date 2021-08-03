import pygame
from game_vals.game_vals import *


class Path( pygame.sprite.Sprite ):
    """ This class represents the path made by the character. """

    # -- Methods
    def __init__(self):
        super().__init__()
        self._layer = 3
        self.width = 50
        self.height = 50
        self.image = pygame.Surface( [self.width, self.height] )
        self.image.fill( PATH_COLOR )
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
