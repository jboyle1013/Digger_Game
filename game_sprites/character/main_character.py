import pygame
import pygame.gfxdraw

from game_vals.game_vals import *
from levels.definition.level_def import Level


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """

    # -- Methods
    def __init__(self, path):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self._layer = 8
        self.width = 40
        self.height = 40
        self.image = pygame.image.load("game_sprites/character/alien.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (45, 45))
        self.path = path
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.pathmaker = True
        self.belowground = False
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
        self.bombs = 3
        self.lives = 3
        self.dir_list = []
        self.prevrleft = None
        self.prevrright = None
        self.prevrtop = None
        self.prevrbottom = None
        # List of sprites we can bump against
        self.level = Level(object, object, object, object, object, object, object, object)

    def update(self):

        """ Check if character hit a gem. """
        self.gem_score()
        """ Move the player. """
        # Move left/right
        self.rect.x += self.change_x

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        self.ab_ground()

        # If the player gets near the right side, loop to other side
        if self.rect.right > SCREEN_WIDTH - 25:
            self.rect.left = 25

        # If the player gets near the left side, loop to other side
        if self.rect.left < 25:
            self.rect.right = SCREEN_WIDTH - 25

        if self.rect.bottom >= 570:
            self.stopy()

        # If the player gets near the left side, loop to other side
        if self.rect.bottom <= 125:
            self.stopy()

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def go_up(self):
        """ Called when the user hits the up arrow. """
        if self.rect.bottom > 125:
            self.change_y = -6

    def go_down(self):
        """ Called when the user hits the down arrow. """
        if self.rect.bottom < 570:
            self.change_y = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.change_y = 0
        self.path.stop()

    def stopx(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.path.stopx()

    def stopy(self):
        """ Called when the user lets off the keyboard. """
        self.change_y = 0
        self.path.stopy()

    def ab_ground(self):
        if self.rect.bottom > 125:
            self.belowground = True
        else:
            self.belowground = False

    def gem_score(self):
        gem_hit_list = pygame.sprite.spritecollide(self, self.level.gems_list, True)
        if len(gem_hit_list) > 0:
            score = self.level.score.scoreupdate()
            self.level.foreground.update_scoreboard(score)

    def pathmake(self):

        if self.change_x > 0:
            self.dir_list.append("RIGHT")
        elif self.change_x < 0:
            self.dir_list.append("LEFT")
        elif self.change_y > 0:
            self.dir_list.append("DOWN")
        elif self.change_y < 0:
            self.dir_list.append("UP")

        if self.belowground and [self.rect.x, self.rect.y] not in self.path.path_coords:
            self.path.path_coords.append([self.rect.centerx, self.rect.centery])
            self.path.uall_path_coords.append([self.rect.centerx, self.rect.centery, 1])
            self.path.all_path_coords.append([self.rect.centerx, self.rect.centery])
            if [self.rect.centerx, self.rect.centery] in self.path.path_edge_coords:
                self.path.path_edge_coords.remove([self.rect.centerx, self.rect.centery])

            for a in range(6):
                x = a + 1
                y = x
                nx = self.rect.centerx - x  # neg x
                ny = self.rect.centery - y  # neg y
                px = self.rect.centerx + x  # pos x
                py = self.rect.centery + y  # pos y
                nlex = self.rect.left - x  # neg left edge x

                if self.change_x != 0:

                    self.path.uall_path_coords.append([nx, self.rect.centery, 1])

                    self.path.uall_path_coords.append([px, self.rect.centery, 1])

                    self.path.uall_path_coords.append([nlex, self.rect.top, 4])

                    self.path.uall_path_coords.append([nlex, self.rect.bottom, 4])

                    for g in range(3):
                        f = g + 1

                        self.path.uall_path_coords.append([nlex, self.rect.top + f, 4])

                        self.path.uall_path_coords.append([nlex, self.rect.bottom - f, 4])

                    self.path.uall_path_coords.append([nlex, self.rect.top + 4, 3])

                    self.path.uall_path_coords.append([nlex, self.rect.bottom - 4, 3])

                    for b in range(19):
                        e = b
                        ndy = self.rect.centery - e  # neg y
                        pdy = self.rect.centery + e  # pos y

                        self.path.uall_path_coords.append([nx, pdy, 2])

                        self.path.uall_path_coords.append([px, pdy, 2])

                        if e < 18:
                            self.path.uall_path_coords.append([nx, ndy, 2])

                            self.path.uall_path_coords.append([px, ndy, 2])

                if self.change_y != 0:

                    self.path.uall_path_coords.append([self.rect.centerx, ny, 1])

                    self.path.uall_path_coords.append([self.rect.centerx, py, 1])

                    self.path.uall_path_coords.append([self.rect.left, ny, 4])

                    self.path.uall_path_coords.append([self.rect.right, py, 4])

                    for f in range(4):
                        self.path.uall_path_coords.append([self.rect.left + f, ny, 4])

                        self.path.uall_path_coords.append([self.rect.right - f, ny, 4])

                    for b in range(19):
                        e = b
                        ndx = self.rect.centerx - e  # neg y
                        pdx = self.rect.centerx + e  # pos y

                        self.path.uall_path_coords.append([pdx, ny, 2])

                        self.path.uall_path_coords.append([pdx, py, 2])

                        if e < 18:
                            self.path.uall_path_coords.append([ndx, ny, 2])

                            self.path.uall_path_coords.append([ndx, py, 2])

                    self.path.uall_path_coords.append([self.rect.left + 4, ny, 3])

                    self.path.uall_path_coords.append([self.rect.right - 4, ny, 3])
                d = len(self.dir_list)
                if d > 6:
                    if self.dir_list[d - 1] != self.dir_list[d - 2]:
                        if self.dir_list[d - 1] == "LEFT":
                            if self.dir_list[d - 2] == "DOWN":
                                self.level.direction_change_tile_down_left(self.rect.center, self.rect.topleft,
                                                                           self.rect.topright, self.rect.bottomleft,
                                                                           self.rect.bottomright)
                        if self.dir_list[d - 1] != self.dir_list[d - 2]:
                            if self.dir_list[d - 1] == "RIGHT":
                                if self.dir_list[d - 2] == "DOWN":
                                    self.level.direction_change_tile_down_right(self.rect.center, self.rect.topleft,
                                                                                self.rect.topright,
                                                                                self.rect.bottomleft,
                                                                                self.rect.bottomright)

                        if self.dir_list[d - 1] != self.dir_list[d - 2]:
                            if self.dir_list[d - 1] == "LEFT":
                                if self.dir_list[d - 2] == "UP":
                                    self.level.direction_change_tile_up_left(self.rect.center, self.rect.topleft,
                                                                             self.rect.topright, self.rect.bottomleft,
                                                                             self.rect.bottomright)

                        if self.dir_list[d - 1] != self.dir_list[d - 2]:
                            if self.dir_list[d - 1] == "RIGHT":
                                if self.dir_list[d - 2] == "UP":
                                    self.level.direction_change_tile_up_right(self.rect.center, self.rect.topleft,
                                                                              self.rect.topright, self.rect.bottomleft,
                                                                              self.rect.bottomright)

                        if self.dir_list[d - 1] != self.dir_list[d - 2]:
                            if self.dir_list[d - 1] == "UP":
                                if self.dir_list[d - 2] == "LEFT":
                                    self.level.direction_change_tile_left_up(self.rect.center, self.rect.topleft,
                                                                             self.rect.topright, self.rect.bottomleft,
                                                                             self.rect.bottomright)

                self.prevrleft = self.rect.left
                self.prevrright = self.rect.right
                self.prevrtop = self.rect.top
                self.prevrbottomb = self.rect.bottom

            self.level.path_gen()
