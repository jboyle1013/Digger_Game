# Setup Basic Framework For Game Development,
# This program creates a blank screen,
# starts the clock, and sets up
# keyboard inputs.

from pygame.locals import *

from game_sprites.character.player_movement import *
from game_sprites.enemies.enemy_def.npc_movement import *
from game_states.intruction_screen.instruct_screen import *
from game_states.intruction_screen.instructclose import *
from game_states.statechanger.statechanger import *


# Import and initialize the pygame library
# Initialize arrow keys, space bar, and escape key

def main():
    """ Main Program """
    BOMBEXPLODEEVENT = pygame.event.custom_type()
    BOMBTIMEREVENT = pygame.event.custom_type()
    pygame.init()

    loc_list = []
    game_state = "intro_screen_setup"
    game_state, pgm, screen, inintroscreen = pregamestatechanger( game_state )

    while inintroscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # it will make Exit the while loop
                pygame.quit()
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == MOUSEMOTION:
                x, y = event.pos
                if game_state == "instruct_screen":
                    if Exit.rect.collidepoint( x, y ):
                        Exit.rollon()
                    else:
                        Exit.rolloff()
                if pgm.playbutton.rect.collidepoint( x, y ):
                    pgm.playbutton.rollon()
                else:
                    pgm.playbutton.rolloff()

                if pgm.instructbutton.rect.collidepoint( x, y ):
                    pgm.instructbutton.rollon()
                else:
                    pgm.instructbutton.rolloff()

            if event.type == MOUSEBUTTONUP:
                x, y = event.pos
                if pgm.instructbutton.rect.collidepoint( x, y ):
                    instruct = InstructScreen( 500, 300 )
                    Exit = Instructclose( 785, 110 )
                    pygame.sprite.LayeredUpdates.add( pgm.pregamesprites, instruct )
                    pygame.sprite.LayeredUpdates.add( pgm.pregamesprites, Exit )
                    game_state = "instruct_screen"
                if game_state == "instruct_screen":
                    if Exit.rect.collidepoint( x, y ):
                        pygame.sprite.Sprite.kill( instruct )
                        pygame.sprite.Sprite.kill( Exit )
                        pgm.pregamesprite_list.remove( instruct )
                        pgm.pregamesprite_list.remove( Exit )
                        game_state = "intro_screen"
                if pgm.playbutton.rect.collidepoint( x, y ) and game_state != "instruct_screen":
                    game_state = "playhit"

        pgm.update()
        game_state, pgm, screen, inintroscreen = pregamestatechanger( game_state )
        pgm.draw( screen )
        pygame.display.flip()

    game_state = "setup"

    foreground, scoring, powerup, powerdown, bomb, screen, player, ground, path_maker, background, \
    running, clock, timer, current_level, current_level_no, level_list, sprites, game_state \
        = statechanger( game_state )

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
                current_level.time = current_level.time - 0
            if event.type == BOMBEXPLODEEVENT:
                current_level.foreground.killBombTimer( bt )
                b.explode()
                pygame.sprite.Sprite.kill( b )
                current_level.sprite_list.remove( b )

            if event.type == BOMBTIMEREVENT and current_level.foreground.bt.bcounter > 0:
                current_level.foreground.updateBombTimer( bt )
            if event.type == BOMBTIMEREVENT and current_level.foreground.bt.bcounter == 0:
                pygame.event.post( pygame.event.Event( BOMBEXPLODEEVENT ) )
                current_level.bomb_to_grid( [b.rect.centerx, b.rect.centery] )
            if event.type == pygame.QUIT:
                # it will make Exit the while loop
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
                if event.key == K_SPACE and current_level.bomb_num > 0:
                    b = Bomb()
                    b.rect.centerx = player.rect.centerx
                    b.rect.centery = player.rect.centery
                    current_level.sprite_list.add( b )
                    pygame.sprite.LayeredUpdates.add( current_level.sprites, b )
                    current_level.bomb_num -= 1
                    current_level.foreground.update_bomb_num( current_level.bomb_num )
                    bt = current_level.foreground.spawnBombTimer()
                    current_level.sprite_list.add( bt )
                    pygame.sprite.LayeredUpdates.add( current_level.sprites, bt )
                    pygame.time.set_timer( BOMBTIMEREVENT, 1000 )

            # stops main character when key is released
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and player.change_x < -1:
                    player.stopx()
                    path_maker.stopx()
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and player.change_x > -1:
                    player.stopx()
                    path_maker.stopx()
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and player.change_y < -1:
                    player.stopy()
                    path_maker.stopy()
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and player.change_y > -1:
                    player.stopy()
                    path_maker.stopy()
        # update screen
        poss_dir, coll_list = ndig_movement(player, current_level.gobbler1, current_level.game_grid, current_level)
        current_level.gobbler1.moveinterpret(poss_dir, coll_list)
        # Update items in the level

        current_level.update()
        foreground, scoring, powerup, powerdown, bomb, screen, player, ground, path_maker, \
            background, running, clock, timer, current_level, current_level_no, level_list, \
            sprites, game_state = statechanger(game_state)

        # If the player gets to the end of the level, go to the next level
        # There is only one level that has been created.
        # TODO
        # Implement more levels these systems.
        """new_loc = astar( current_level.game_grid, current_level.gobbler1.rect.center, player.rect.center,
                         allow_diagonal_movement=False )
        loc_list.append( new_loc )"""
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
    between_levels = True
    while between_levels:
        clock.tick( 30 )
        pass

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
        clock.tick( 30 )
    # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()
