import pygame.gfxdraw
import pygame.time

from game_sprites.powerup.powerup_def.powerup import *
from game_sprites.timer.timer import *

bomb = pygame.Surface( (35, 35), pygame.SRCALPHA, )


class Bomb( PowerUp ):

    def __init__(self):
        PowerUp.__init__( self )
        self.image = pygame.image.load( "game_sprites/powerup/powerup_types/bomb.png" ).convert_alpha()
        self.image = pygame.transform.smoothscale( self.image, (35, 35) )
        self.rect = self.image.get_rect()

    def explode(self):
        self.image = bomb
        pygame.gfxdraw.box( bomb, pygame.Rect( self.rect.left, self.rect.top, 35, 35 ), PATH_COLOR )
