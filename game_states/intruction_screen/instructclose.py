import pygame.gfxdraw

from game_states.pregame_manager.pregame_manager import *

exit = pygame.Surface( (40, 40), pygame.SRCALPHA, )


class Instructclose( pygame.sprite.Sprite ):
    """ This class represents the ground """

    # -- Methods
    def __init__(self, x, y):
        # Call the parent's constructor

        super().__init__()
        self._layer = 10
        self.image = exit
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.exit = pygame.image.load( "game_states/intruction_screen/exit.png" ).convert_alpha()
        self.exit = pygame.transform.smoothscale( self.exit, (40, 40) )
        self.image.blit( self.exit, [0, 0] )
