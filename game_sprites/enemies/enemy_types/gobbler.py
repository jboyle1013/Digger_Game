from game_sprites.enemies.enemy_def.enemy_def import Enemy
from game_sprites.enemies.enemy_def.npc_movement import *
from game_vals.game_vals import *


class Gobbler( Enemy ):

    def __init__(self, path):
        """ Constructor function """
        # Call the parent's constructor
        Enemy.__init__( self, path )
        self.image = pygame.image.load("game_sprites/enemies/enemy_types/gobbler.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (40, 40))

    def update(self):
        self.rect.x += self.change_x

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        self.ab_ground()
        # self.movement_control()
        # If the mob gets near the right side, loop to other side
        if self.rect.right > SCREEN_WIDTH:
            self.rect.left = 0

        # If the mob gets near the left side, loop to other side
        if self.rect.left < 0:
            self.rect.right = SCREEN_WIDTH

        if self.rect.bottom >= SCREEN_HEIGHT - 1:
            self.stopy()

        # If the mob gets near the left side, loop to other side
        if self.rect.bottom < 125:
            self.stopy()

        # mob movement:

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -3

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 3

    def go_up(self):
        """ Called when the user hits the up arrow. """
        if self.rect.bottom > 125:
            self.change_y = -3

    def go_down(self):
        """ Called when the user hits the down arrow. """
        if self.rect.bottom < SCREEN_HEIGHT:
            self.change_y = 3

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.change_y = 0
        self.path.stop()

    def stopx(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    def stopy(self):
        """ Called when the user lets off the keyboard. """
        self.change_y = 0

    def ab_ground(self):
        if self.rect.bottom > 125:
            self.belowground = True
        else:
            self.belowground = False

    def movement_control(self):
        x = self.path.rect.centerx
        y = self.path.rect.centery

        ydist = self.rect.centery - y
        xdist = self.rect.centerx - x

        if self.belowground:
            if abs( xdist ) > abs( ydist ):
                if xdist > 0:
                    self.direction_list.append("LEFT")
                    if ydist > 0:
                        self.direction_list.append( "UP" )
                        self.direction_list.append( "DOWN" )
                        self.direction_list.append( "RIGHT" )
                    elif ydist < 0:
                        self.direction_list.append( "DOWN" )
                        self.direction_list.append( "RIGHT" )
                        self.direction_list.append( "UP" )

                elif xdist < 0:
                    self.direction_list.append( "RIGHT" )
                    if ydist > 0:
                        self.direction_list.append( "UP" )
                        self.direction_list.append( "DOWN" )
                        self.direction_list.append( "LEFT" )
                    elif ydist < 0:
                        self.direction_list.append( "DOWN" )
                        self.direction_list.append( "LEFT" )
                        self.direction_list.append( "UP" )


            elif abs( ydist ) > abs( xdist ):
                if ydist > 0:
                    ndig_movement( self, self.path, "UP" )
                elif ydist < 0:
                    ndig_movement( self, self.path, "DOWN" )

        else:
            if abs( xdist ) > abs( ydist ):
                if xdist > 0:
                    ndig_movement( self, self.path, "LEFT" )
                elif xdist < 0:
                    ndig_movement( self, self.path, "RIGHT" )

            if abs( ydist ) > abs( xdist ):
                if ydist < 0:
                    ndig_movement( self, self.path, "DOWN" )
