import math as m

import pygame


def ndig_movement(character, enemy, grid, level):
    """This function controls the movement of an npc that cannot dig """

    """ Getting Position Data """
    x2 = character.rect.centerx
    y2 = character.rect.centery
    x1 = enemy.rect.centerx
    y1 = enemy.rect.centery
    dir_options = [["STAY", [x1, y1]], ["RIGHT", [x1 + 6, y1]], ["LEFT", [x1 - 6, y1]], ["DOWN", [x1, y1 + 6]],
                   ["UP", [x1, y1 - 6]]]
    jdir = [[x1, y1], [x1 + 6, y1], [x1 - 6, y1], [x1, y1 + 6], [x1, y1 - 6]]
    ydist = y2 - y1
    xdist = x2 - x1
    dist_liststol = []
    pos_dir = None
    r_list = []
    x_pos = 0
    y_pos = 0
    for dir in dir_options:
        dist = m.dist( dir[1], character.rect.center )
        dist_liststol.append( [dir[0], dist] )
    dist_liststol.sort()
    ind = []
    path_collide_center = []
    path_collide_list = pygame.sprite.spritecollide( enemy, level.path_list, False )
    for path in path_collide_list:
        path_collide_center.append( [path.rect.centerx, path.rect.centery] )
        if [path.rect.centerx, path.rect.centery] in jdir:
            ind.append( [path.rect.centerx, path.rect.centery] )

    for opt in dir_options:
        if opt[1] in ind:
            r_list.append( opt )
            if opt[0] == "LEFT" or opt[0] == "RIGHT":
                x_pos = x_pos + 1
            if opt[0] == "UP" or opt[0] == "DOWN":
                y_pos = y_pos + 1
    bt = xdist < 0
    if x_pos > 0 and y_pos == 0:
        if xdist < 0:
            pos_dir = "LEFT"
        elif xdist > 0:
            pos_dir = "RIGHT"

    if y_pos > 0 and x_pos == 0:
        if ydist < 0:
            pos_dir = "UP"
        elif ydist > 0:
            pos_dir = "DOWN"

    elif y_pos > 0:
        for i in range( y_pos ):
            if abs( ydist ) > abs( xdist ):
                if ydist > 0:
                    pos_dir = "DOWN"
                elif ydist < 0:
                    pos_dir = "UP"

    x = dir_options
    # pos_dir = dist_liststol[0][0]

    return pos_dir


def index_from_tuple_list(list, identifier):
    for items in list:
        for objects in items:
            if objects == identifier:
                val = list.index( items )
    return val


def remove_opposites(list, words):
    i1 = index_from_tuple_list( list, words[0] )
    i2 = index_from_tuple_list( list, words[1] )

    if i1 > i2:
        list.pop( i1 )
    elif i2 > i1:
        list.pop( i2 )
    return list
