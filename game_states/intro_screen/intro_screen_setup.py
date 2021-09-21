import pygame.gfxdraw
import pygame.sprite

from game_states.intro_screen.intro_screen import *
from game_states.pregame_manager.pregame_manager import *


def intro_screen_setup():
    pgm = PreGame()
    pgm.create()
    introscreen = IntroScreen()
    inintroscreen = True
    pygame.sprite.LayeredUpdates.add( pgm.pregamesprites, introscreen )
    pgm.pregamesprite_list = pgm.pregamesprites
    screen = pgm.screen
    pgm.draw( screen )
    game_state = "intro_screen"
    return game_state, pgm, screen, inintroscreen
