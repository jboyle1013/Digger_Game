import pygame
from game_vals.game_vals import *
from game_sprites.powerup.powerup_def.powerup import *


class Bomb( pygame.sprite.Sprite ):

    def __init__(self):
        PowerUp().__init__()
        self.image.fill( BLACK )
        self.r
