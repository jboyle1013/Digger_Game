import pygame
from game_vals.game_vals import *
import pygame

from levels.definition.level_def import Level

from game_vals.game_vals import *


class Background(pygame.sprite.Sprite):
    """ This class represents the ground """

    # -- Methods
    def __init__(self):
        # Call the parent's constructor

        super().__init__()
        self._layer = 4
        width = 1000
        height = 125
        self.image = pygame.Surface([width, height])
        self.image.fill(SKY)
        self.cloud1 = pygame.image.load( "game_sprites/background/cloud.png" ).convert_alpha()
        self.cloud2 = pygame.image.load( "game_sprites/background/cloud.png" ).convert_alpha()
        self.cloud3 = pygame.image.load( "game_sprites/background/cloud.png" ).convert_alpha()
        self.cloud1 = pygame.transform.smoothscale( self.cloud1, (100, 50) )
        self.cloud2 = pygame.transform.smoothscale( self.cloud2, (100, 50) )
        self.cloud3 = pygame.transform.smoothscale( self.cloud3, (100, 50) )
        self.image.blit( self.cloud1, [245, 5] )
        self.image.blit( self.cloud2, [434, 5] )
        self.image.blit( self.cloud3, [685, 5] )
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()