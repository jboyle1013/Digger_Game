from game_vals.game_vals import *
from levels.definition.level_def import *


class Path_Maker( pygame.sprite.Sprite ):
    """ This class represents the path made by the character. """

    # -- Methods
    def __init__(self):

        super().__init__()
        self._layer = 1
        self.width = 50
        self.height = 50
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(PATH_COLOR)
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.level = Level(object, object, object, object, object, object)
        self.previous_Direction = None
        self.p_vh = None
        self.c_vh = None
        self.current_Direction = None
        # Background image
        self.background = None
        self.path_coords = []
        self.all_path_coords = []

    def update(self):
        """ Move the path. """
        # Move left/right
        self.rect.centerx += self.change_x

        # Move up/down
        self.rect.centery += self.change_y

        self.image = pygame.Surface( [self.width, self.height] )

        # Check and see if we hit anything

        # If the player gets near the right side, loop to other side
        if self.rect.right > SCREEN_WIDTH:
            self.rect.left = 0

        # If the player gets near the left side, loop to other side
        if self.rect.left < 0:
            self.rect.right = SCREEN_WIDTH

        if self.rect.y >= SCREEN_HEIGHT:
            self.stopy()

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def go_up(self):
        """ Called when the user hits the up arrow. """
        self.change_y = -6

    def go_down(self):
        """ Called when the user hits the down arrow. """
        self.change_y = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.change_y = 0

    def stopx(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    def stopy(self):
        """ Called when the user lets off the keyboard. """
        self.change_y = 0

    def cell_drawer(self):
        x = self.rect.centerx
        y = self.rect.centery
