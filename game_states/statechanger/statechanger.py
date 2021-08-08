# Import and initialize the pygame library
# Initialize arrow keys, space bar, and escape key
from game_states.running.in_game.in_game import *
from game_states.setup.setup import setup

def statechanger(game_state):
    global foreground, scoring, powerup, powerdown, bomb, screen, sprites, level_list, current_level_no, gems, player, ground, running, path_maker, background, clock, timer, current_level
    if game_state == "setup":
        foreground, scoring, powerup, powerdown, bomb, screen, player, ground, path_maker, background, running, clock, timer, current_level, current_level_no, level_list, sprites, game_state = setup()

    if game_state == "in_game":
        foreground, scoring, powerup, powerdown, bomb, screen, player, ground, path_maker, background, running, clock, timer, current_level, current_level_no, level_list, sprites, game_state = \
            in_game( foreground, scoring, powerup, powerdown, bomb, screen, player, ground, path_maker, background,
                     running, clock, timer, current_level, current_level_no, level_list, sprites,
                     game_state )
    return foreground, scoring, powerup, powerdown, bomb, screen, player, ground, path_maker, background, running, clock, timer, current_level, current_level_no, level_list, sprites, game_state
