import pygame

from game_sprites.background.background import Background
# Initialize arrow keys, space bar, and escape key
from game_sprites.character.main_character import Player
from game_sprites.ground.ground import Ground
from game_sprites.path.path_maker import Path_Maker
from levels.game_levels.level0 import Level_0
from game_sprites.path.path import *
from game_sprites.enemies.enemy_def.enemy_def import Enemy
from game_sprites.timer.timer import *
from game_sprites.timer.timerbackground import *
from game_sprites.gems.gem_def.gems_def import *
from game_sprites.foreground.foreground import *

def setup():
    """ This function sets up the game """
    path = Path()
    path_maker = Path_Maker()
    background = Background()
    ground = Ground()
    player = Player( path_maker )
    enemy = Enemy( path_maker )
    timerback = TimerBackground()
    timer = Timer()
    foreground = Foreground()

    level_list = [Level_0( player, ground, path_maker, path, background, enemy)]

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    player.level = current_level
    pygame.sprite.LayeredUpdates.add( player.level.sprites, timer )
    pygame.sprite.LayeredUpdates.add( player.level.sprites, timerback )
    pygame.sprite.LayeredUpdates.add( player.level.sprites, foreground )
    # Set up the drawing window
    sprites = player.level.sprites
    player.level.sprite_list = sprites
    screen = player.level.screen
    clock = pygame.time.Clock()
    current_level.gridmaker()
    """   infoLine1 = "Welcome to Miner"
    infoLine2 = "Enter your name and click enter to start!!"
    usertext = ''
    textEntering = True

    input_rect = pygame.Rect( 450, 200, 140, 32 )
    color = pygame.Color( 'WHITE' )
    while textEntering:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    textEntering = False
                if event.key == pygame.K_BACKSPACE:
                    usertext = usertext[0:-1]
                else:
                    usertext += event.unicode

        pygame.draw.rect( player.level.screen, color, input_rect, 2 )

        text_surface1 = player.level.base_font.render( infoLine1, True, (255, 255, 255) )
        text_surface2 = player.level.base_font.render( infoLine2, True, (255, 255, 255) )
        text_surface = player.level.base_font.render( usertext, True, (255, 255, 255) )
        player.level.screen.blit( text_surface1, (300, 40) )
        player.level.screen.blit( text_surface2, (300, 80) )

        player.level.screen.blit( text_surface, (input_rect.x + 5, input_rect.y + 5) )

        input_rect.w = max( 100, text_surface.get_width() + 10 )

        pygame.display.flip()
        clock.tick( 60 )
    """

    player.rect.x = 340
    player.rect.bottom = 125
    ground.rect.bottom = 625
    path_maker.rect.centerx = player.rect.centerx
    path_maker.rect.centery = player.rect.centery
    ngem = current_level.gem_create( current_level.jewel_num )
    for i in ngem:
        g = Gems_Def()
        g.rect.x = i[0]
        g.rect.y = i[1]
        current_level.gems_list.add( g )
        current_level.sprite_list.add( g )


    # Run until the user asks to quit
    running = False
    clock = pygame.time.Clock()
    game_state = "in_game"

    return foreground, screen, player, ground, path_maker, background, running, clock, timer, current_level, current_level_no, level_list, \
           sprites, game_state
