import heapq
from warnings import warn

from pathfinder.Node import *


def astar(maze, start, end, allow_diagonal_movement=False):
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze:
    :param start:
    :param end:
    :return:
    """

    # Create start and end node
    start_node = Node( None, start )
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node( None, end )
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Heapify the open_list and Add the start node
    heapq.heapify( open_list )
    heapq.heappush( open_list, start_node )

    # Adding a stop condition
    outer_iterations = 0
    max_iterations = (len( maze[0] ) * len( maze ) // 2)

    # what squares do we search
    adjacent_squares = ((0, -4), (0, 4), (-4, 0), (4, 0),)
    if allow_diagonal_movement:
        adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)

    # Loop until you find the end
    while len( open_list ) > 0:
        outer_iterations += 1

        if outer_iterations > max_iterations:
            # if we hit this point return the path such as it is
            # it will not contain the destination
            warn( "giving up on pathfinding too many iterations" )
            return Node.return_path( current_node )

            # Get the current node
        current_node = heapq.heappop( open_list )
        closed_list.append( current_node )

        # Found the goal
        if current_node == end_node:
            return Node.return_path( current_node )

        # Generate children
        children = []

        for new_position in adjacent_squares:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > 624 or node_position[0] < 0 or node_position[1] > 999 or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[1]][node_position[0]] != 0:
                continue

            # Create new node
            new_node = Node( current_node, node_position )

            # Append
            children.append( new_node )

        # Loop through children
        for child in children:
            # Child is on the closed list
            if len( [closed_child for closed_child in closed_list if closed_child == child] ) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                    (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len( [open_node for open_node in open_list if
                     child.position == open_node.position and child.g > open_node.g] ) > 0:
                continue

            # Add the child to the open list
            heapq.heappush( open_list, child )

    warn( "Couldn't get a path to destination" )
    return None
