import pygame


def in_game(foreground, scoring, powerup, powerdown, bomb, screen, player, ground, path_maker, background, running,
            clock, timer, current_level, current_level_no, level_list,
            sprites, game_state):
    # This function controls the behavior of the game when it is running

    running = True
    pygame.sprite.LayeredUpdates.change_layer( sprites, ground, 2 )
    """if len(current_level.gems_list.spritedict) == 0:
        running = False"""

    return foreground, scoring, powerup, powerdown, bomb, screen, player, ground, path_maker, background, running, clock, timer, current_level, current_level_no, \
           level_list, sprites, game_state
