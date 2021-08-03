import pygame


class Ground(pygame.sprite.Sprite):
    """ This class represents the ground """

    # -- Methods
    def __init__(self):
        # Call the parent's constructor

        super().__init__()
        self._layer = 2
        width = 1000
        height = 500
        self.image = pygame.Surface([width, height])
        self.image.fill((122, 70, 2))
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()