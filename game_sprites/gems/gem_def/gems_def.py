import pygame
import pygame.gfxdraw

from game_vals.game_vals import *
from levels.definition.level_def import Level


class Gems_Def( pygame.sprite.Sprite ):
    """ This class represents the gems that the player
        collects. """

    # -- Methods
    def __init__(self):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self._layer = 5
        self.width = 15
        self.height = 15

        # Player jump height
        self.image = pygame.image.load( "game_sprites/gems/gem_types/sapphire.png").convert_alpha()

        self.image = pygame.transform.smoothscale( self.image, (15, 15) )

        self.rect = self.image.get_rect()

