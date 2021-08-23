import pygame

from levels.definition.level_def import Level


class PowerUp( pygame.sprite.Sprite ):

    def __init__(self):
        super().__init__()

        # Creates general shape, need to import image but it'll be black for now
        self._layer = 5
        self.width = 15
        self.height = 15
        self.type = 'powerup'
        self.image = pygame.Surface( [self.width, self.height] )
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.active = False
        self.collect_time = 0
        self.curr_time = 0
        self.level = Level( object, object, object, object, object, object, object, object )
