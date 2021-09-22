import pygame.gfxdraw

from game_states.pregame_manager.pregame_manager import *

introscreen = pygame.Surface( (1000, 625), pygame.SRCALPHA, )


class IntroScreen( pygame.sprite.Sprite ):
    """ This class represents the ground """

    # -- Methods
    def __init__(self):
        # Call the parent's constructor

        super().__init__()
        self._layer = 8
        self.image = introscreen
        self.rect = self.image.get_rect()
        self.ground = pygame.image.load( "game_states/intro_screen/soil.png" ).convert_alpha()
        self.ground = pygame.transform.smoothscale( self.ground, (1000, 450) )
        self.sky = pygame.image.load( "game_states/intro_screen/sky.png" ).convert_alpha()
        self.sky = pygame.transform.smoothscale( self.sky, (1000, 275) )
        self.words = pygame.image.load( "game_states/intro_screen/words.png" ).convert_alpha()
        self.words = pygame.transform.smoothscale( self.words, (400, 250) )

        self.image.blit( self.sky, [0, 0] )
        self.image.blit( self.ground, [0, 200] )
        self.image.blit( self.words, [300, 10] )
