import pygame


def player_movement(event, player, path):
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        player.go_left()
        path.go_left()
        path.rect.center = player.rect.center
        path.stopy()
        player.stopy()
        # Controls motion to right
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        player.go_right()
        path.go_right()
        path.rect.center = player.rect.center
        path.stopy()
        player.stopy()
        # Controls motion up
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        player.go_up()
        path.go_up()
        path.rect.center = player.rect.center
        path.stopx()
        player.stopx()
        # Controls motion down
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        player.go_down()
        path.go_down()
        path.rect.center = player.rect.center
        path.stopx()
        player.stopx()


def ndig_movement(event, character, path, direction):
    if direction == "LEFT":
        nx = character.rect.centerx - 6
        nc = [nx, character.rect.centery]
        tf = nc in path.path_coords
        if tf:
            character.go_left()
            character.stopy()
        if not tf:
            character.stop()

    # Controls motion to right
    if direction == "RIGHT":
        nx = character.rect.centerx + 6
        tf = [nx, character.rect.centery] in path.path_coords

        if tf:
            character.go_right()
            character.stopy()
        if not tf:
            character.stop()

    # Controls motion up
    if direction == "UP":
        ny = character.rect.centery - 6
        tf = [character.rect.centerx, ny] in path.path_coords

        if tf:
            character.go_up()
            character.stopx()
        if not tf:
            character.stop()

    # Controls motion down
    if direction == "DOWN":
        ny = character.rect.centery + 6
        tf = [character.rect.centerx, ny] in path.path_coords

        if tf:
            character.go_down()
            character.stopx()
        if not tf:
            character.stop()
