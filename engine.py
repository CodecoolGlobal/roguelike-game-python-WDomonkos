from typing import Counter
from math import floor
import util
from main import PLAYER_ICON, PLAYER_START_X, PLAYER_START_Y, MAP_LIST


def create_map():
    board = util.read_map(MAP_LIST[0])
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
