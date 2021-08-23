import pygame

from game_vals.game_vals import *
from levels.definition.level_def import Level


class Enemy( pygame.sprite.Sprite ):
    """ This class is the superclass for all enemis. """

    # -- Methods
    def __init__(self, path):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self._layer = 6
        self.width = 40
        self.height = 40
        self.image = pygame.Surface( [self.width, self.height] )
        self.path = path
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.belowground = False
        # Set speed vector of mob
        self.change_x = 0
        self.change_y = 0
        self.rect.center = [1000, 750]
        self.direction_list = []
        # List of sprites we can bump against
        self.level = Level( object, object, object, object, object, object, object, object )

    def update(self):
        """ Move the mob. """
        # Move left/right
        self.rect.x += self.change_x

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        self.ab_ground()

        # If the mob gets near the right side, loop to other side
        if self.rect.right > SCREEN_WIDTH:
            self.rect.left = 0

        # If the mob gets near the left side, loop to other side
        if self.rect.left < 0:
            self.rect.right = SCREEN_WIDTH

        if self.rect.bottom >= SCREEN_HEIGHT - 1:
            self.stopy()

        # If the mob gets near the left side, loop to other side
        if self.rect.bottom <= 125:
            self.stopy()

    # mob movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -5

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 5

    def go_up(self):
        """ Called when the user hits the up arrow. """
        if self.rect.bottom > 125:
            self.change_y = -5

    def go_down(self):
        """ Called when the user hits the down arrow. """
        if self.rect.bottom < SCREEN_HEIGHT:
            self.change_y = 5

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.change_y = 0
        self.path.stop()

    def stopx(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.path.stopx()

    def stopy(self):
        """ Called when the user lets off the keyboard. """
        self.change_y = 0
        self.path.stopy()

    def ab_ground(self):
        if self.rect.bottom > 125:
            self.belowground = True
        else:
            self.belowground = False


