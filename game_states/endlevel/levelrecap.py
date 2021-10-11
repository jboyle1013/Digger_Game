import pygame


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
        self.level = Level( object, object, object, object, object, object, object, object )
