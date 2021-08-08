from game_sprites.powerup.powerup_def.powerup import *
from game_sprites.timer.timer import *


class Bomb( PowerUp ):

    def __init__(self):
        PowerUp.__init__( self )
        self.image = pygame.image.load( "game_sprites/powerup/powerup_types/bomb.png" ).convert_alpha()
        self.image = pygame.transform.smoothscale( self.image, (35, 35) )
        self.rect = self.image.get_rect()

    def bomb_plant(self, coords, timer):
        b = Bomb()
        b.rect.x = coords[0]
        b.rect.y = coords[1]
        self.level.sprite_list.add( b )
        self.level.u
