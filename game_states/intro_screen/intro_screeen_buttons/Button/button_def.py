import pygame
import pygame.gfxdraw

from game_states.intro_screen.intro_screeen_buttons.Button.rounded_rect import *

Pbutton = pygame.Surface( (140, 80), pygame.SRCALPHA, )
Ibutton = pygame.Surface( (140, 80), pygame.SRCALPHA, )


class PButtton( pygame.sprite.Sprite ):

    def __init__(self, x, y):
        # Call the parent's constructor

        super().__init__()
        self._layer = 9
        self.image = Pbutton
        self.rect = self.image.get_rect()
        self.button = pygame.image.load( "game_states/intro_screen/Play.png" ).convert_alpha()
        self.button = pygame.transform.smoothscale( self.button, (140, 80) )
        self.rect.centerx = x
        self.rect.centery = y
        self.image.blit( self.button, [0, 0] )

    def rollon(self):
        self.button = pygame.image.load( "game_states/intro_screen/Play-rollon.png" ).convert_alpha()
        self.button = pygame.transform.smoothscale( self.button, (140, 80) )
        self.image.blit( self.button, [0, 0] )

    def rolloff(self):
        self.button = pygame.image.load( "game_states/intro_screen/Play.png" ).convert_alpha()
        self.button = pygame.transform.smoothscale( self.button, (140, 80) )
        self.image.blit( self.button, [0, 0] )


class IButtton( pygame.sprite.Sprite ):

    def __init__(self, x, y):
        # Call the parent's constructor

        super().__init__()
        self._layer = 9
        self.image = Ibutton
        self.rect = self.image.get_rect()
        self.button = pygame.image.load( "game_states/intro_screen/instructions.png" ).convert_alpha()
        self.button = pygame.transform.smoothscale( self.button, (140, 80) )
        self.rect.centerx = x
        self.rect.centery = y
        self.image.blit( self.button, [0, 0] )

    def rollon(self):
        self.button = pygame.image.load( "game_states/intro_screen/instructions-rollon.png" ).convert_alpha()
        self.button = pygame.transform.smoothscale( self.button, (140, 80) )
        self.image.blit( self.button, [0, 0] )

    def rolloff(self):
        self.button = pygame.image.load( "game_states/intro_screen/instructions.png" ).convert_alpha()
        self.button = pygame.transform.smoothscale( self.button, (140, 80) )
        self.image.blit( self.button, [0, 0] )
