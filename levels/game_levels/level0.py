from levels.definition.level_def import Level
from game_sprites.enemies.enemy_types.gobbler import Gobbler
from game_sprites.gems.gem_def.gems_def import *
import pygame


# Create platforms for the level
class Level_0( Level ):
    """ Definition for level 0. """

    def __init__(self, player, ground, path_maker, path, background, enemy):
        """ Create level 0. """

        # Call the parent constructor
        Level.__init__( self, player, ground, path_maker, path, background, enemy)


        self.jewel_num = 5
        self.enemy_num = 6
        self.time = 60

        self.create()
        gobbler1 = Gobbler( self.path_maker )
        gobbler1.rect.centerx = 900
        gobbler1.rect.bottom = 125
        pygame.sprite.LayeredUpdates.add( self.sprites, gobbler1 )



