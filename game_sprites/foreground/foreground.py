import pygame
import pygame.gfxdraw
from levels.definition.level_def import Level
from game_vals.game_vals import *

foreground = pygame.Surface( (1000, 625), pygame.SRCALPHA, )
pygame.gfxdraw.box( foreground, pygame.Rect( 0, 580, 1000, 55 ), TASK_BROWN )
pygame.gfxdraw.box( foreground, pygame.Rect( 0, -10, 25, 625 ), TASK_BROWN )
pygame.gfxdraw.box( foreground, pygame.Rect( 975, 0, 25, 625 ), TASK_BROWN )
pygame.gfxdraw.filled_ellipse( foreground, 960, 20, 70, 45, TASK_BROWN )
pygame.gfxdraw.filled_ellipse( foreground, 960, 20, 50, 35, WHITE )



class Foreground( pygame.sprite.Sprite ):
    """ This class represents the ground """

    # -- Methods
    def __init__(self):
        # Call the parent's constructor

        super().__init__()
        self._layer = 4
        width = 10000
        height = 10000
        self.image = foreground
        self.rect = self.image.get_rect()
        self.level = Level( object, object, object, object, object, object )
        self.font = pygame.font.SysFont( 'Comic Sans MS', 20 )
        self.score = 0
        self.bomb = pygame.image.load("game_sprites/powerup/powerup_types/bomb.png")
        self.bomb = pygame.transform.smoothscale( self.bomb, (35, 35) )
        self.image.blit(self.bomb, [75, 590])
        self.scoretext = self.font.render( str( self.score ), 1, BLACK )
        self.image.blit( self.scoretext, [950, 10] )
        self.bombstr = "Bombs: "
        self.bombstext = self.font.render( str( self.bombstr ), 1, WHITE )
        self.image.blit( self.bombstext, [5, 590] )
        self.Xstr = "X  "
        self.Xtext = self.font.render( str( self.Xstr ), 1, WHITE )
        self.image.blit( self.Xtext, [105, 590] )

        self.bnumtext = self.font.render( str( 3 ), 1, WHITE )
        self.image.blit( self.bnumtext, [125, 590] )
        self.heart = pygame.image.load( "game_sprites/foreground/heart.png" )
        self.heart = pygame.transform.scale( self.heart, (30, 30) )
        self.image.blit( self.heart, [900, 590] )
        self.lifestr = "Lives: "
        self.lifetext = self.font.render( str( self.lifestr ), 1, WHITE )
        self.image.blit( self.lifetext, [835, 590] )
        self.LXstr = "X  "
        self.LXtext = self.font.render( str( self.LXstr ), 1, WHITE )
        self.image.blit( self.LXtext, [935, 590] )

        self.Lnumtext = self.font.render( str( 3 ), 1, WHITE )
        self.image.blit( self.Lnumtext, [955, 590] )