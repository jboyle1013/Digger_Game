# Setup Basic Framework For Game Development,
# This program creates a blank screen,
# starts the clock, and sets up
# keyboard inputs.

from pygame import K_ESCAPE, KEYDOWN

import game_states.statechanger.statechanger
from game_sprites.character.player_movement import *
from game_sprites.timer.timer import *


# Import and initialize the pygame library
# Initialize arrow keys, space bar, and escape key


def main():
    """ Main Program """

    pygame.init()
    game_state = "setup"

    foreground, screen, player, ground, path_maker, background, running, clock, timer, current_level, current_level_no, level_list, \
    sprites, game_state = game_states.statechanger.statechanger.statechanger( game_state )

    pygame.time.set_timer( pygame.USEREVENT, 1000 )
    while running:
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.USEREVENT and timer.counter > 0:
                timer.clock_tick()
                current_level.time = current_level.time - 1

            if event.type == pygame.QUIT:
                # it will make exit the while loop
                pygame.quit()
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    pygame.quit()
                # Controls motion to left
                if player.pathmaker == True and player.belowground == True:
                    player_movement( event, player, path_maker )
                elif not player.belowground:
                    player_movement( event, player, path_maker )

            # stops main character when key is released
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and player.change_x < 0:
                    player.stopx()
                    path_maker.stopx()
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and player.change_x > 0:
                    player.stopx()
                    path_maker.stopx()
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and player.change_y < 0:
                    player.stopy()
                    path_maker.stopy()
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and player.change_y > 0:
                    player.stopy()
                    path_maker.stopy()

                # update screen

        # Update items in the level

        current_level.update()
        foreground, screen, player, ground, path_maker, background, running, clock, timer, current_level, \
            current_level_no, level_list, sprites, game_state = game_states.statechanger.statechanger.statechanger(
            game_state )

        # If the player gets to the end of the level, go to the next level
        # There is only one level that has been created.
        # TODO
        # Implement more levels these systems.

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # Draw background and sprites
        current_level.draw( screen )

        # TODO
        # A time controlled scroll would most likely either be here or in the
        # Child classes for the individual levels
        # Flip the display - this is required for anything to show up on the screen
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick( 30 )

    clock = pygame.time.Clock()
    endScreen = True

    color = pygame.Color( 'WHITE' )
    while endScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    endScreen = False

        pygame.display.flip()
        clock.tick( 60 )
    # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()
