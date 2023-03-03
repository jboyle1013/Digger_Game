import pygame


class PowerDown(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Creates general shape, need to import image but it'll be red for now
        width = 30
        height = 30
        self.type = 'powerdown'
        self.image = pygame.image.load('game_sprites/powerdown/powerdown.png')
        self.rect = self.image.get_rect()
        self.active = False
        self.collect_time = 0
        self.curr_time = 0

    def small_jump(self, player, reset):
        """ Changes the player's jump height to -9
            If reset is True, it changes the player's jump height to -10
        """
        if reset:
            player.jumpHeight = -10
            self.active = False
        else:
            player.jumpHeight = -9
            self.active = True

    def shift_powerdown(self, shift_y, powerdown_list):
        """ When the user moves to the top of the screen and we need to scroll the powerdowns:
        """

        # Go through the powerdown list and shift
        for powerdown in powerdown_list:
            powerdown.rect.y += shift_y
