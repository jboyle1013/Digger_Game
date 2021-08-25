import pygame
import pygame.gfxdraw

from game_vals.game_vals import *
from levels.definition.level_def import Level


class Player( pygame.sprite.Sprite ):
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
        self.image = pygame.image.load( "game_sprites/character/alien.png" ).convert_alpha()
        self.image = pygame.transform.smoothscale( self.image, (45, 45) )
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
        self.level = Level( object, object, object, object, object, object, object, object )

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
                nbey = self.rect.bottom - y  # neg bottom edge y
                plex = self.rect.left + x  # pos left edge x
                pbey = self.rect.bottom + y  # pos bottom edge y
                nrex = self.rect.right - x  # neg right edge x
                ntey = self.rect.top - y  # neg top edge y
                prex = self.rect.right + x  # pos right edge x
                ptey = self.rect.top + y  # pos top edge y

                if self.change_x != 0:

                    if ([nx, self.rect.centery] not in self.path.path_coords) \
                            or ([nx, self.rect.centery] not in self.path.all_path_coords):
                        self.path.all_path_coords.append([nx, self.rect.centery])
                        if [nx, self.rect.centery] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([nx, self.rect.centery])

                    if [nx, self.rect.centery] not in self.path.path_coords \
                            or ([px, self.rect.centery] not in self.path.all_path_coords):
                        self.path.all_path_coords.append([px, self.rect.centery])
                        if [px, self.rect.centery] in self.path.path_edge_coords:
                            self.path.path_edge_coords.remove([px, self.rect.centery])

                    if ([nlex, self.rect.top] not in self.path.path_coords) \
                            or ([nlex, self.rect.top] not in self.path.all_path_coords) \
                            or ([nlex, self.rect.top] not in self.path.path_edge_coords):
                        self.path.path_edge_coords.append([nlex, self.rect.top])

                    if ([nlex, self.rect.bottom] not in self.path.path_coords) \
                            or ([nlex, self.rect.bottom] not in self.path.all_path_coords) \
                            or ([nlex, self.rect.bottom] not in self.path.path_edge_coords):
                        self.path.path_edge_coords.append([nlex, self.rect.bottom])
                    for g in range(3):
                        f = g + 1

                        if ([nlex, self.rect.top + x] not in self.path.path_coords) \
                                or ([nlex, self.rect.top + x] not in self.path.all_path_coords) \
                                or ([nlex, self.rect.top + x] not in self.path.path_edge_coords):
                            self.path.path_edge_coords.append([nlex, self.rect.top + f])

                        if ([nlex, self.rect.bottom - x] not in self.path.path_coords) \
                                or ([nlex, self.rect.bottom - x] not in self.path.all_path_coords) \
                                or ([nlex, self.rect.bottom - x] not in self.path.path_edge_coords):
                            self.path.path_edge_coords.append([nlex, self.rect.bottom - f])

                    for b in range(udist):
                        x = a
                        ndx = self.rect.centery - x  # neg x

                    for b in range(ddist):
                        x = a
                        pdx = self.rect.centery + x  # pos x

                if self.change_y != 0:

                    if ([self.rect.centerx, ny] not in self.path.path_coords) \
                            or ([self.rect.centerx, ny] not in self.path.all_path_coords):
                        self.path.all_path_coords.append([self.rect.centerx, ny])

                    if [self.rect.centerx, py] not in self.path.path_coords \
                            or ([self.rect.centerx, py] not in self.path.all_path_coords):
                        self.path.all_path_coords.append([self.rect.centerx, py])

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

                    if ([self.rect.right, py] not in self.path.path_coords) \
                            or ([self.rect.right, py] not in self.path.all_path_coords) \
                            or ([self.rect.right, py] not in self.path.path_edge_coords):
                        self.path.path_edge_coords.append([self.rect.right, py])

                    for g in range(3):
                        f = g + 1
                        if ([self.rect.left + x, ny] not in self.path.path_coords) \
                                or ([self.rect.left + x, ny] not in self.path.all_path_coords) \
                                or ([self.rect.left + x, ny] not in self.path.path_edge_coords):
                            self.path.path_edge_coords.append([self.rect.left + f, ny])

                        if ([self.rect.right - x, py] not in self.path.path_coords) \
                                or ([self.rect.right - x, py] not in self.path.all_path_coords) \
                                or ([self.rect.right - x, py] not in self.path.path_edge_coords):
                            self.path.path_edge_coords.append([self.rect.right - f, py])
                    for b in range(ldist):
                        pass
                    for b in range(rdist):
                        pass

            self.level.path_gen()
