# Level Class

import random

import numpy as np

from game_sprites.path.path import *


class Level( object ):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player, ground, pathmaker, path, background, enemy, score, foreground):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player.
            :param enemy: """
        self.enemy_list = pygame.sprite.Group()  # game enemies
        self.path_list = pygame.sprite.Group()  # primary path list
        self.gems_list = pygame.sprite.Group()
        self.sprites = pygame.sprite.LayeredUpdates()  # all game sprites
        self.sprite_list = pygame.sprite.Group()  # all game sprites
        self.path_maker = pathmaker  # the pathmaker class
        self.player = player  # the player class
        self.foreground = foreground  # the foreground screen
        self.path = path  # the path class
        self.score = score  # the scoring system, also a class
        self.ground = ground  # the ground class
        self.game_grid = []  # the grid, direction system for the enemies
        self.background = background  # the background class
        self.enemy = enemy  # the enemy class
        self.size = [SCREEN_WIDTH, SCREEN_HEIGHT]  # screen size
        self.screen = pygame.display.set_mode( self.size )  # the screen
        # Background image
        self.base_font = pygame.font.Font( None, 32 )  # game font
        self.bomb_num = 3  # number of bombs available to player

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""

        self.path_list.update()
        self.sprite_list.update()
        self.gridupdate()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill( (BLACK) )
        # Draw all the sprite lists that we have
        self.path_list.draw( screen )
        self.sprite_list.draw( screen )

    def path_gen(self):
        """ Draws the game path """
        xy = self.path_maker.path_coords[-1]

        npath = Path()
        npath.rect.centerx = xy[0]
        npath.rect.centery = xy[1]
        self.path_list.add( npath )
        self.sprite_list.add( npath )

    def rand_create(self, nums):
        xvals = random.sample(range(25, 925), nums)
        yvals = random.sample( range( 150, 550 ), nums )
        slist = []
        for i in range(nums):
            slist.append([xvals[i], yvals[i]])
        return slist




    def eventtimerstart(self, time):
        """ Timer that will be used for spawning mobs """
        pygame.time.set_timer( pygame.USEREVENT, time )

        return pygame.USEREVENT

    def create(self):
        """" Creates sprites in level """
        pygame.sprite.LayeredUpdates.add( self.sprites, self.background )
        pygame.sprite.LayeredUpdates.add( self.sprites, self.ground )
        pygame.sprite.LayeredUpdates.add( self.sprites, self.player )
        pygame.sprite.LayeredUpdates.add( self.sprites, self.path_maker )
        pygame.sprite.LayeredUpdates.add( self.sprites, self.path )
        pygame.sprite.LayeredUpdates.add( self.sprites, self.enemy )

    def gridmaker(self):
        """ Creates game grid """
        game_gridglevel = np.ones( (1, 1000) )
        game_gridsky = np.zeros( (105, 1000) )
        t = np.concatenate( (game_gridsky, game_gridglevel) )
        gg = np.zeros( (519, 1000) )
        self.game_grid = np.concatenate( (t, gg) )

    def gridupdate(self):
        """ Updates game grid """

        for coords in self.path_maker.all_path_coords:
            x = coords[0]
            y = coords[1]
            if self.game_grid[(y, x)] != 1:
                self.game_grid[(y, x)] = 1

    def bomb_to_grid(self, coords):
        """ Adds bomb space to grid, use top left x and y coords. """
        x = coords[0]
        y = coords[1]
        for i in range( 100 ):
            a = i + 1
            if self.game_grid[y + a, x] != 1:
                self.game_grid[y + a, x] = 1
            if self.game_grid[y, x + a] != 1:
                self.game_grid[y, x + a] = 1
            if self.game_grid[y + a, x + a] != 1:
                self.game_grid[y + a, x + a] = 1











    def findend(self, i, j, a, output, index):
        x = len( a )
        y = len( a[0] )

        # flag to check column edge case,
        # initializing with 0
        flagc = 0

        # flag to check row edge case,
        # initializing with 0
        flagr = 0

        for m in range( i, x ):

            # loop breaks where first 1 encounters
            if a[m][j] == 1:
                flagr = 1  # set the flag
                break

            # pass because already processed
            if a[m][j] == 5:
                pass

            for n in range( j, y ):

                # loop breaks where first 1 encounters
                if a[m][n] == 1:
                    flagc = 1  # set the flag
                    break

                # fill rectangle elements with any
                # number so that we can exclude
                # next time
                a[m][n] = 5

        if flagr == 1:
            output[index].append( m - 1 )
        else:
            # when end point touch the boundary
            output[index].append( m )

        if flagc == 1:
            output[index].append( n - 1 )
        else:
            # when end point touch the boundary
            output[index].append( n )

    def get_rectangle_coordinates(self, a):

        # retrieving the column size of array
        size_of_array = len( a )

        # output array where we are going
        # to store our output
        output = []

        # It will be used for storing start
        # and end location in the same index
        index = -1

        for i in range( 0, size_of_array ):
            for j in range( 0, len( a[0] ) ):
                if a[i][j] == 0:
                    # storing initial position
                    # of rectangle
                    output.append( [i, j] )

                    # will be used for the
                    # last position
                    index = index + 1
                    self.findend( i, j, a, output, index )

        print( output )

    def check(self, p, groupies):
        a = False
        b = False
        if pygame.sprite.spritecollideany( p, groupies ) and pygame.sprite.collide_rect_ratio( 5 )( p,
                                                                                                    self.player ):
            a = True
            b = True

        if not pygame.sprite.spritecollideany( p, groupies ):
            for entity in groupies:
                if entity == self.platform:
                    continue
                if (abs( p.rect.y - entity.rect.y ) < 100) and (
                        abs( p.rect.x - entity.rect.x ) < 350):
                    a = True
        if not pygame.sprite.collide_rect_ratio( 5 )( p, self.player ):
            if (abs( p.rect.y - self.player.rect.y ) < 115) and (
                    abs( p.rect.x - self.player.rect.x ) < 105):
                b = True
        if a == True or b == True:
            return True

        else:
            return False
