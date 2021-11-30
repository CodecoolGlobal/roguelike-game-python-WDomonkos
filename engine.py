from typing import Counter
from math import floor

from main import PLAYER_ICON, PLAYER_START_X, PLAYER_START_Y


def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    wall = "#"
    empty = " "
    gate = "¤"
    board = []
    for row in range(height):
        column = []
        for col in range(width):
            if row == 0 or row == height -1:    # northern and southern wall
                column.append(wall)
            elif height % 2 == 1 and floor(height / 2) == row:  # gate if height is odd
                if col == 0 or col == width -1:
                    column.append(gate)
                else:
                    column.append(empty)
            elif height % 2 == 0 and (height / 2) -1 == row or (height / 2) == row:     # gate if height is even
                if col == 0 or col == width -1:
                    column.append(gate)
                else:
                    column.append(empty)
            else:                                   # every other row
                if col == 0 or col == width -1:
                    column.append(wall)
                else:
                    column.append(empty)
        board.append(column)
    return board
            

def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    for row in board:           # deleting the player from board (h ne húzzon csíkot, mint egy csiga)
        if player["icon"] in row:
            row[row.index(player["icon"])] = " "
    board[player["position_y"]][player["position_x"]] = player["icon"]
    return board


def player_movement(board, player, key):
    player_original = player.copy()
    keys = {"a": -1, "d": +1, "w": -1, "s": +1}
    if key == "a" or key == "d":
        player["position_x"] += keys[key]
    elif key == "w" or key == "s":
        player["position_y"] += keys[key]
    if board[player["position_y"]][player["position_x"]] == "#":
        return player_original
    return player
