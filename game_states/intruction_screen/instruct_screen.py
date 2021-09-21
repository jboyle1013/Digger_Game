import pygame.gfxdraw

from game_states.pregame_manager.pregame_manager import *

instructscreen = pygame.Surface( (600, 425), pygame.SRCALPHA, )


class InstructScreen( pygame.sprite.Sprite ):
    """ This class represents the ground """

    # -- Methods
    def __init__(self, x, y):
        # Call the parent's constructor

        super().__init__()
        self._layer = 10
        self.image = instructscreen
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.instruct = pygame.image.load( "game_states/intruction_screen/Howtoplay.png" ).convert_alpha()
        self.instruct = pygame.transform.smoothscale( self.instruct, (600, 435) )
        self.image.blit( self.instruct, [0, 0] )
