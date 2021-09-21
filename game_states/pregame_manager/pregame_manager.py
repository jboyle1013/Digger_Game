import pygame.sprite

from game_sprites.path.path import *
from game_states.intro_screen.intro_screeen_buttons.Button.button_def import *


class PreGame( object ):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player.
            :param enemy: """
        self.screen = pygame.display.set_mode( [SCREEN_WIDTH, SCREEN_HEIGHT] )

        self.pregamesprites = pygame.sprite.LayeredUpdates()
        self.pregamesprite_list = pygame.sprite.Group
        self.playbutton = PButtton( 500, 350 )
        self.instructbutton = IButtton( 500, 450 )

    def update(self):
        """ Update everything in this level."""

        self.pregamesprite_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill( (WHITE) )

        # Draw all the sprite lists that we have
        self.pregamesprite_list.draw( screen )

    def create(self):
        pygame.sprite.LayeredUpdates.add( self.pregamesprites, self.playbutton )
        pygame.sprite.LayeredUpdates.add( self.pregamesprites, self.instructbutton )
