import pygame
from game_vals.game_vals import *
from game_sprites.powerup.powerup_def.powerup import *


class Bomb( PowerUp ):

    def __init__(self):
        PowerUp().__init__()
        self.image = pygame.image.load( "game_sprites/powerup/powerup_types/bomb.png" ).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (35, 35))
        self.rect = self.image.get_rect()


