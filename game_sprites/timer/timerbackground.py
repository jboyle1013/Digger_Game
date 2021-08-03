import pygame

class TimerBackground(pygame.sprite.Sprite):
    """ This class represents the ground """

    # -- Methods
    def __init__(self):
        # Call the parent's constructor

        super().__init__()
        self._layer = 6
        self.image = pygame.image.load("game_sprites/timer/timerback.jpg")
        self.rect = self.image.get_rect()