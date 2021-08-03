import pygame


def in_game(foreground, screen, player, ground, path_maker, background, running, clock, timer, current_level, current_level_no, level_list,
            sprites, game_state):
    running = True
    pygame.sprite.LayeredUpdates.change_layer(sprites, ground, 2)

    return foreground, screen, player, ground, path_maker, background, running, clock, timer, current_level, current_level_no, \
        level_list, sprites, game_state
