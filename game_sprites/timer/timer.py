import pygame
import pygame.gfxdraw

from game_vals.game_vals import *
from levels.definition.level_def import Level

clock_img = pygame.Surface( (150, 150), pygame.SRCALPHA )

pygame.gfxdraw.aacircle( clock_img, 55, 55, 35, (156, 124, 56) )
pygame.gfxdraw.filled_circle( clock_img, 55, 55, 35, (156, 124, 56) )
pygame.gfxdraw.filled_circle( clock_img, 55, 55, 27, (255, 255, 240) )

pygame.gfxdraw.line( clock_img, 55, 28, 55, 35, BLACK )
pygame.gfxdraw.line( clock_img, 55, 82, 55, 75, BLACK )
pygame.gfxdraw.line( clock_img, 28, 55, 35, 55, BLACK )
pygame.gfxdraw.line( clock_img, 82, 55, 75, 55, BLACK )
pygame.gfxdraw.line( clock_img, 69, 79, 65, 72, BLACK )
pygame.gfxdraw.line( clock_img, 40, 31, 44, 38, BLACK )
pygame.gfxdraw.line( clock_img, 31, 40, 38, 44, BLACK )
pygame.gfxdraw.line( clock_img, 79, 69, 72, 65, BLACK )
pygame.gfxdraw.line( clock_img, 40, 79, 44, 72, BLACK )
pygame.gfxdraw.line( clock_img, 31, 69, 38, 65, BLACK )
pygame.gfxdraw.line( clock_img, 64, 37, 68, 30, BLACK )
pygame.gfxdraw.line( clock_img, 72, 46, 80, 41, BLACK )

pygame.draw.rect( clock_img, SKY, pygame.Rect(
    0, 0, 130, 125 ), 20, border_top_right_radius=45 )
pygame.draw.rect( clock_img, SKY, pygame.Rect(
    -40, -40, 195, 175 ), 40, border_bottom_right_radius=80 )
pygame.gfxdraw.box(clock_img, pygame.Rect(20, 95, 25, 55), TASK_BROWN)


class Timer( pygame.sprite.Sprite ):
    """ This class represents the timer. """

    # -- Methods
    def __init__(self):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()
        self._layer = 7
        self.image = clock_img

        self.rect = self.image.get_rect( center=(55, 55) )
        self.level = Level( object, object, object, object, object, object, object, object )
        self.font = pygame.font.SysFont( 'Comic Sans MS', 20 )
        self.counter = 60
        self.text = self.font.render( str( self.counter ), 1, BLACK )
        self.image.blit( self.text, [43, 40] )

    def clock_tick(self):
        self.counter -= 1
        self.text = str( self.counter )
        pygame.gfxdraw.filled_circle( clock_img, 55, 55, 20, (255, 255, 240) )
        self.text = self.font.render( str( self.counter ), 1, BLACK )
        if self.counter >= 20:
            self.image.blit( self.text, [43, 40] )
        elif self.counter >= 10:
            self.image.blit( self.text, [47, 40] )
        else:
            self.image.blit( self.text, [50, 40] )
