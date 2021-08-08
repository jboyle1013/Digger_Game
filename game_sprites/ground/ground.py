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
        self.image = pygame.image.load( "game_sprites/ground/dirt.png" ).convert_alpha()
        self.image = pygame.transform.smoothscale( self.image, (1000, 500) )

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
