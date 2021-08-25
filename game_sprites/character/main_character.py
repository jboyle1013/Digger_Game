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
        self._layer = 6
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

        self.pathmake()

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
        if self.belowground and [self.rect.x, self.rect.y] not in self.path.path_coords:
            self.path.path_coords.append([self.rect.centerx, self.rect.centery])
            self.path.all_path_coords.append([self.rect.centerx, self.rect.centery])
            if [self.rect.centerx, self.rect.centery] in self.path.path_edge_coords:
                self.path.path_edge_coords.remove([self.rect.centerx, self.rect.centery])
            if [self.rect.x, self.rect.y] not in self.path.mpath_coords:
                self.path.uall_path_coords.append([self.rect.centerx, self.rect.centery])

            ldist = abs(self.rect.left - self.rect.centerx) - 4
            rdist = abs(self.rect.right - self.rect.centerx) - 4
            udist = abs(self.rect.top - self.rect.centery) - 4
            ddist = abs(self.rect.bottom - self.rect.centery) - 4

            for a in range(9):
                x = a + 1
                y = x
                nx = self.rect.centerx - x  # neg x
                ny = self.rect.centery - y  # neg y
                px = self.rect.centerx + x  # pos x
                py = self.rect.centery + y  # pos y
                nlex = self.rect.left - x  # neg left edge x

                if self.change_x != 0:

                    if ([nx, self.rect.centery] not in self.path.path_coords) \
                            or ([nx, self.rect.centery] not in self.path.all_path_coords):

                        self.path.all_path_coords.append([nx, self.rect.centery])

                        if [nx, self.rect.centery] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([nx, self.rect.centery])

                        if [nx, self.rect.y] not in self.path.mpath_coords:
                            self.path.uall_path_coords.append([nx, self.rect.centery, 1])

                    if [px, self.rect.centery] not in self.path.path_coords \
                            or ([px, self.rect.centery] not in self.path.all_path_coords):

                        self.path.all_path_coords.append([px, self.rect.centery])

                        if [px, self.rect.centery] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([px, self.rect.centery])

                        if [px, self.rect.y] not in self.path.mpath_coords:
                            self.path.uall_path_coords.append([px, self.rect.centery, 1])

                    if ([nlex, self.rect.top] not in self.path.path_coords) \
                            or ([nlex, self.rect.top] not in self.path.all_path_coords) \
                            or ([nlex, self.rect.top] not in self.path.path_edge_coords):

                        self.path.path_edge_coords.append([nlex, self.rect.top])

                        if [nlex, self.rect.top] not in self.path.mpath_edge_coords:
                            self.path.uall_path_coords.append([nlex, self.rect.top, 4])

                    if ([nlex, self.rect.bottom] not in self.path.path_coords) \
                            or ([nlex, self.rect.bottom] not in self.path.all_path_coords) \
                            or ([nlex, self.rect.bottom] not in self.path.path_edge_coords):

                        self.path.path_edge_coords.append([nlex, self.rect.bottom])

                        if [nlex, self.rect.bottom] not in self.path.mpath_edge_coords:
                            self.path.uall_path_coords.append([nlex, self.rect.bottom, 4])

                    for g in range(3):
                        f = g + 1

                        if ([nlex, self.rect.top + f] not in self.path.path_coords) \
                                or ([nlex, self.rect.top + f] not in self.path.all_path_coords) \
                                or ([nlex, self.rect.top + f] not in self.path.path_edge_coords):

                            self.path.path_edge_coords.append([nlex, self.rect.top + f])

                            if [nlex, self.rect.top + f] not in self.path.mpath_edge_coords:
                                self.path.uall_path_coords.append([nlex, self.rect.top + f, 4])

                        if ([nlex, self.rect.bottom - f] not in self.path.path_coords) \
                                or ([nlex, self.rect.bottom - f] not in self.path.all_path_coords) \
                                or ([nlex, self.rect.bottom - f] not in self.path.path_edge_coords):

                            self.path.path_edge_coords.append([nlex, self.rect.bottom - f])

                            if [nlex, self.rect.top] not in self.path.mpath_edge_coords:
                                self.path.uall_path_coords.append([nlex, self.rect.bottom - f, 4])

                    for b in range(udist):
                        e = b
                        ndy = self.rect.centery - e  # neg y

                        if ([nx, ndy] not in self.path.path_coords) \
                                or ([nx, ndy] not in self.path.all_path_coords):

                            self.path.path_mid_coords.append([nx, ndy])

                            if [nx, ndy] not in self.path.mpath_mid_coords:
                                self.path.uall_path_coords.append([nx, ndy, 2])

                        if ([px, ndy] not in self.path.path_coords) \
                                or ([px, ndy] not in self.path.all_path_coords):

                            self.path.path_mid_coords.append([px, ndy])

                            if [px, ndy] not in self.path.mpath_mid_coords:
                                self.path.uall_path_coords.append([px, ndy, 2])

                        if [px, ndy] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([px, ndy])

                        if [nx, ndy] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([nx, ndy])

                    for b in range(ddist):
                        e = b
                        pdy = self.rect.centery + e  # pos y

                        if ([nx, pdy] not in self.path.path_coords) \
                                or ([nx, pdy] not in self.path.all_path_coords):

                            self.path.path_mid_coords.append([nx, pdy])

                            if [nx, pdy] not in self.path.mpath_mid_coords:
                                self.path.uall_path_coords.append([nx, pdy, 2])

                        if ([px, pdy] not in self.path.path_coords) \
                                or ([px, pdy] not in self.path.all_path_coords):

                            self.path.path_mid_coords.append([px, pdy])

                            if [px, pdy] not in self.path.mpath_mid_coords:
                                self.path.uall_path_coords.append([px, pdy, 2])

                        if [px, pdy] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([px, pdy])

                        if [nx, pdy] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([nx, pdy])

                    pdyb = self.rect.centery + ddist

                    ndyb = self.rect.centery - udist

                    if ([nx, pdyb] not in self.path.path_coords) \
                            or ([nx, pdyb] not in self.path.all_path_coords):
                        self.path.path_mid_border_coords.append([nx, pdyb])

                    if ([px, pdyb] not in self.path.path_coords) \
                            or ([px, pdyb] not in self.path.all_path_coords):

                        self.path.path_mid_border_coords.append([px, pdyb])

                        if [px, pdyb] not in self.path.mpath_mid_border_coords:
                            self.path.uall_path_coords.append([px, pdyb, 3])

                    if [px, pdyb] in self.path.path_edge_coords:
                        self.path.path_edge_coords.remove([px, pdyb])

                    if [nx, pdyb] in self.path.path_edge_coords:
                        self.path.path_edge_coords.remove([nx, pdyb])

                    if ([nx, ndyb] not in self.path.path_coords) \
                            or ([nx, ndyb] not in self.path.all_path_coords):
                        self.path.path_mid_border_coords.append([nx, ndyb])

                    if ([px, ndyb] not in self.path.path_coords) \
                            or ([px, ndyb] not in self.path.all_path_coords):

                        self.path.path_mid_border_coords.append([px, ndyb])

                        if [px, ndyb] not in self.path.mpath_mid_border_coords:
                            self.path.uall_path_coords.append([px, ndyb, 3])

                    if [px, ndyb] in self.path.path_edge_coords:
                        self.path.path_edge_coords.remove([px, ndyb])

                    if [nx, ndyb] in self.path.path_edge_coords:
                        self.path.path_edge_coords.remove([nx, ndyb])

                if self.change_y != 0:

                    if ([self.rect.centerx, ny] not in self.path.path_coords) \
                            or ([self.rect.centerx, ny] not in self.path.all_path_coords):

                        self.path.all_path_coords.append([self.rect.centerx, ny])

                        if [self.rect.centerx, ny] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([self.rect.centerx, ny])

                        if [self.rect.centerx, ny] not in self.path.mpath_coords:
                            self.path.uall_path_coords.append([self.rect.centerx, ny, 1])

                    if [self.rect.centerx, py] not in self.path.path_coords \
                            or ([self.rect.centerx, py] not in self.path.all_path_coords):

                        self.path.all_path_coords.append([self.rect.centerx, py])

                        if [self.rect.centerx, py] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([self.rect.centerx, py])

                        if [self.rect.centerx, ny] not in self.path.mpath_coords:
                            self.path.uall_path_coords.append([self.rect.centerx, py, 1])

                    if ([self.rect.left, py] not in self.path.path_coords) \
                            or ([self.rect.left, py] not in self.path.all_path_coords) \
                            or ([self.rect.left, py] not in self.path.path_edge_coords):
                        self.path.path_edge_coords.append([self.rect.left, py])

                    if ([self.rect.right, ny] not in self.path.path_coords) \
                            or ([self.rect.right, ny] not in self.path.all_path_coords) \
                            or ([self.rect.right, ny] not in self.path.path_edge_coords):
                        self.path.path_edge_coords.append([self.rect.right, ny])

                    if ([self.rect.left, ny] not in self.path.path_coords) \
                            or ([self.rect.left, ny] not in self.path.all_path_coords) \
                            or ([self.rect.left, ny] not in self.path.path_edge_coords):
                        self.path.path_edge_coords.append([self.rect.left, ny])

                    if [self.rect.left, ny] not in self.path.mpath_edge_coords:
                        self.path.uall_path_coords.append([self.rect.left, ny, 4])

                    if ([self.rect.right, py] not in self.path.path_coords) \
                            or ([self.rect.right, py] not in self.path.all_path_coords) \
                            or ([self.rect.right, py] not in self.path.path_edge_coords):

                        self.path.path_edge_coords.append([self.rect.right, py])

                        if [self.rect.right, py] not in self.path.mpath_edge_coords:
                            self.path.uall_path_coords.append([self.rect.right, py, 4])

                    for g in range(3):
                        f = g + 1
                        if ([self.rect.left + f, ny] not in self.path.path_coords) \
                                or ([self.rect.left + f, ny] not in self.path.all_path_coords) \
                                or ([self.rect.left + f, ny] not in self.path.path_edge_coords):

                            self.path.path_edge_coords.append([self.rect.left + f, ny])

                            if [self.rect.left + f, ny] not in self.path.mpath_edge_coords:
                                self.path.uall_path_coords.append([self.rect.left + f, ny, 4])

                        if ([self.rect.right - f, py] not in self.path.path_coords) \
                                or ([self.rect.right - f, py] not in self.path.all_path_coords) \
                                or ([self.rect.right - f, py] not in self.path.path_edge_coords):

                            self.path.path_edge_coords.append([self.rect.right - f, py])

                            if [self.rect.right - f, py] not in self.path.mpath_edge_coords:
                                self.path.uall_path_coords.append([self.rect.right - f, py, 4])

                    for b in range(ldist):
                        e = b
                        ndx = self.rect.centerx - e  # neg y

                        if ([ndx, ny] not in self.path.path_coords) \
                                or ([ndx, ny] not in self.path.all_path_coords):

                            self.path.path_mid_coords.append([ndx, ny])

                            if [ndx, ny] not in self.path.mpath_mid_coords:
                                self.path.uall_path_coords.append([nx, ny, 2])

                        if ([ndx, py] not in self.path.path_coords) \
                                or ([ndx, py] not in self.path.all_path_coords):

                            self.path.path_mid_coords.append([ndx, py])

                            if [ndx, py] not in self.path.mpath_mid_coords:
                                self.path.uall_path_coords.append([ndx, py, 2])

                        if [ndx, py] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([ndx, py])

                        if [ndx, ny] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([ndx, ny])

                    for b in range(rdist):
                        e = b
                        pdx = self.rect.centerx + e  # neg y

                        if ([pdx, ny] not in self.path.path_coords) \
                                or ([pdx, ny] not in self.path.all_path_coords):

                            self.path.path_mid_coords.append([pdx, ny])

                            if self.level.game_grid[(ny, pdx)] != 1:
                                self.level.game_grid[(ny, pdx)] = 2

                        if ([pdx, py] not in self.path.path_coords) \
                                or ([pdx, py] not in self.path.all_path_coords):

                            self.path.path_mid_coords.append([pdx, py])

                            if self.level.game_grid[(py, pdx)] != 1:
                                self.level.game_grid[(py, pdx)] = 2

                        if [pdx, py] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([pdx, py])

                        if [pdx, ny] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([pdx, ny])

                    pdxb = self.rect.centerx + ddist

                    ndxb = self.rect.centerx - udist

                    if ([pdxb, ny] not in self.path.path_coords) \
                            or ([pdxb, ny] not in self.path.all_path_coords):
                        self.path.path_mid_border_coords.append([pdxb, ny])
                    if ([pdxb, py] not in self.path.path_coords) \
                            or ([pdxb, py] not in self.path.all_path_coords):
                        self.path.path_mid_border_coords.append([pdxb, py])
                    if [pdxb, py] in self.path.path_edge_coords:
                        self.path.path_edge_coords.remove([pdxb, py])
                    if [pdxb, ny] in self.path.path_edge_coords:
                        self.path.path_edge_coords.remove([pdxb, ny])

                    if ([ndxb, ny] not in self.path.path_coords) \
                            or ([ndxb, ny] not in self.path.all_path_coords):
                        self.path.path_mid_border_coords.append([ndxb, ny])
                    if ([ndxb, py] not in self.path.path_coords) \
                            or ([ndxb, py] not in self.path.all_path_coords):
                        self.path.path_mid_border_coords.append([ndxb, py])
                    if [ndxb, py] in self.path.path_edge_coords:
                        self.path.path_edge_coords.remove([ndxb, py])
                    if [ndxb, ny] in self.path.path_edge_coords:
                        self.path.path_edge_coords.remove([ndxb, ny])

            self.level.path_gen()
