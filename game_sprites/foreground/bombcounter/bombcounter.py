import pygame
import pygame.gfxdraw

from game_vals.game_vals import *
from levels.definition.level_def import Level

bc = pygame.Surface((1000, 625), pygame.SRCALPHA, )


class BombCounter(pygame.sprite.Sprite):
    """ This class represents the ground """

    # -- Methods
    def __init__(self):
        # Call the parent's constructor

        super().__init__()
        self._layer = 4
        width = 10000
        height = 10000
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.bcounter = 3
        self.bctext = self.font.render(str(self.bcounter), 1, BLACK)
        self.image = bc
        self.rect = self.image.get_rect()
        self.level = Level(object, object, object, object, object, object, object, object)
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        pygame.gfxdraw.filled_ellipse(bc, 65, 550, 45, 25, TASK_BROWN)
        pygame.gfxdraw.filled_ellipse(bc, 65, 550, 35, 15, WHITE)
        self.image.blit(self.bctext, [60, 535])

    def bombtimerupdate(self):
        self.bcounter = self.bcounter - 1
        self.bctext = self.font.render(str(self.bcounter), 1, BLACK)
        pygame.gfxdraw.filled_ellipse(bc, 65, 550, 35, 15, WHITE)
        self.image.blit(self.bctext, [60, 535])
