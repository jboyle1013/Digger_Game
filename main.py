# Setup Basic Framework For Game Development,
# This program creates a blank screen,
# starts the clock, and sets up
# keyboard inputs.

from pygame.locals import *

import game_states.statechanger.statechanger
from game_sprites.character.player_movement import *
from game_sprites.powerup.powerup_types.bombs import *


# Import and initialize the pygame library
# Initialize arrow keys, space bar, and escape key

def main():
    """ Main Program """
    BOMBEXPLODEEVENT = pygame.event.custom_type()
    BOMBTIMEREVENT = pygame.event.custom_type()
    pygame.init()
    game_state = "setup"

    foreground, scoring, powerup, powerdown, bomb, screen, player, ground, path_maker, background, \
    running, clock, timer, current_level, current_level_no, level_list, sprites, game_state \
        = game_states.statechanger.statechanger.statechanger(game_state)

    pygame.time.set_timer(pygame.USEREVENT, 1000)
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
            if event.type == BOMBEXPLODEEVENT:
                current_level.foreground.killBombTimer(bt)
                b.explode()
                pygame.sprite.Sprite.kill(b)
                current_level.sprite_list.remove(b)

            if event.type == BOMBTIMEREVENT and current_level.foreground.bt.bcounter > 0:
                current_level.foreground.updateBombTimer(bt)
            if event.type == BOMBTIMEREVENT and current_level.foreground.bt.bcounter == 0:
                pygame.event.post(pygame.event.Event(BOMBEXPLODEEVENT))
            if event.type == pygame.QUIT:
                # it will make exit the while loop
                pygame.quit()
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    pygame.quit()
                # Controls motion to left
                if player.pathmaker == True and player.belowground == True:
                    player_movement(event, player, path_maker)
                elif not player.belowground:
                    player_movement(event, player, path_maker)
                if event.key == K_SPACE and current_level.bomb_num > 0:
                    b = Bomb()
                    b.rect.centerx = player.rect.centerx
                    b.rect.centery = player.rect.centery
                    current_level.sprite_list.add(b)
                    pygame.sprite.LayeredUpdates.add(current_level.sprites, b)
                    current_level.bomb_num -= 1
                    current_level.foreground.update_bomb_num(current_level.bomb_num)
                    bt = current_level.foreground.spawnBombTimer()
                    current_level.sprite_list.add(bt)
                    pygame.sprite.LayeredUpdates.add(current_level.sprites, bt)
                    pygame.time.set_timer(BOMBTIMEREVENT, 1000)

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
        foreground, scoring, powerup, powerdown, bomb, screen, player, ground, path_maker, \
        background, running, clock, timer, current_level, current_level_no, level_list, \
        sprites, game_state = game_states.statechanger.statechanger.statechanger(game_state)

        # If the player gets to the end of the level, go to the next level
        # There is only one level that has been created.
        # TODO
        # Implement more levels these systems.

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # Draw background and sprites
        current_level.draw(screen)

        # TODO
        # A time controlled scroll would most likely either be here or in the
        # Child classes for the individual levels
        # Flip the display - this is required for anything to show up on the screen
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)

    clock = pygame.time.Clock()
    endScreen = True

    while endScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    endScreen = False

        pygame.display.flip()
        clock.tick(30)
    # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()
