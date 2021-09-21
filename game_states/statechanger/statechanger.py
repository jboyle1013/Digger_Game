# Import and initialize the pygame library
# Initialize arrow keys, space bar, and escape key
from game_states.intro_screen.intro_screen_setup import *
from game_states.intro_screen.introscreenleave import *
from game_states.intro_screen.introscreenrunning import *
from game_states.running.in_game.in_game import *
from game_states.setup.setup import *


def pregamestatechanger(game_state):
    global pgm, screen, inintroscreen
    if game_state == "intro_screen_setup":
        game_state, pgm, screen, inintroscreen = intro_screen_setup()
        return game_state, pgm, screen, inintroscreen

    if game_state == "intro_screen":
        intro_screen_running()
        return game_state, pgm, screen, inintroscreen

    if game_state == "instruct_screen":
        intro_screen_running()
        return game_state, pgm, screen, inintroscreen

    if game_state == "playhit":
        game_state, pgm, screen, inintroscreen = intro_screen_leave( game_state, pgm, screen, inintroscreen )
        return game_state, pgm, screen, inintroscreen


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
