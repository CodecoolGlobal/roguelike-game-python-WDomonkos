import util
from main import PLAYER_ICON, PLAYER_START_X, PLAYER_START_Y
import copy
from random import randint


WALL = "#"
EMPTY = " "
RIGHT_GATE = '\033[96m'+">"+'\033[00m'
LEFT_GATE = '\033[96m'+"<"+'\033[00m'
DOORKEY = "\033[92m"+"~"+"\033[00m"
NPC_COLLISION = [WALL, RIGHT_GATE, LEFT_GATE, DOORKEY]


def create_board(width, height, border_width=1):
    matrix = []
    for h in range(height):
        inner_list = []
        for w in range(width):
            inner_list.append(WALL)
        matrix.append(inner_list)

    if border_width in range(1, min(height, width) // 2 + 1):
        for inner_h in range(border_width, height - border_width):
            for inner_w in range(border_width, width - border_width):
                matrix[inner_h][inner_w] = EMPTY
    return matrix


def board1(orig_board):
    new_board = copy.deepcopy(orig_board)

    new_board[len(new_board)//2][-1] = RIGHT_GATE
    new_board[len(new_board)//2-1][-1] = RIGHT_GATE

    for i in range(9):
        new_board[i][10] = WALL
    for i in range(13):
        new_board[-i][16] = WALL

    new_board[2][-(len(orig_board[0])//2+2)] = "\033[92m"+"H"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2+1)] = "\033[92m"+"O"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2+0)] = "\033[92m"+"M"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-1)] = "\033[92m"+"E"+"\033[00m"

    new_board[randint(10, 18)][randint(1, 12)] = DOORKEY

    return new_board


def board2(orig_board):
    new_board = copy.deepcopy(orig_board)

    new_board[len(new_board)//2][-1] = RIGHT_GATE
    new_board[len(new_board)//2-1][-1] = RIGHT_GATE

    new_board[len(new_board)//2][0] = LEFT_GATE
    new_board[len(new_board)//2-1][0] = LEFT_GATE

    for i in range(18):
        new_board[13][i] = WALL
    for i in range(13):
        new_board[7][-i] = WALL

    new_board[2][-(len(orig_board[0])//2+3)] = "\033[92m"+"S"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2+2)] = "\033[92m"+"T"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2+1)] = "\033[92m"+"R"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-0)] = "\033[92m"+"E"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-1)] = "\033[92m"+"E"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-2)] = "\033[92m"+"T"+"\033[00m"

    return new_board


def board3(orig_board):
    new_board = copy.deepcopy(orig_board)

    new_board[len(new_board)//2][0] = LEFT_GATE
    new_board[len(new_board)//2-1][0] = LEFT_GATE

    for i in range(len(orig_board)-5):
        new_board[i][-8] = WALL

    new_board[2][-5] = "\033[92m"+"B"+"\033[00m"
    new_board[2][-4] = "\033[92m"+"A"+"\033[00m"
    new_board[2][-3] = "\033[92m"+"R"+"\033[00m"

    return new_board


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

    if board[player["position_y"]][player["position_x"]] != WALL:
        board[player["position_y"]][player["position_x"]] = player["icon"]
    return board


def player_movement(board, player, key):
    player_original = player.copy()
    keys = {"a": -1, "d": +1, "w": -1, "s": +1}
    if key == "a" or key == "d":
        player["position_x"] += keys[key]
    elif key == "w" or key == "s":
        player["position_y"] += keys[key]
    player_position = board[player["position_y"]][player["position_x"]]

    if player_position == WALL:
        return player_original

    if player_position == RIGHT_GATE and player["doorkey"] == 1:
        player["current_room"] += 1
        player["position_y"] = len(board)//2
        player["position_x"] = 1
    elif player_position == RIGHT_GATE and player["doorkey"] == 0:
        return player_original
        
    if player_position == LEFT_GATE:
        player["current_room"] -= 1
        player["position_y"] = len(board)//2
        player["position_x"] = -2

    if player_position == DOORKEY:
        player["doorkey"] = 1

    return player


def npc_movement(board, player, key):
    player_original = player.copy()
    keys = {"a": -1, "d": +1, "w": -1, "s": +1}
    if key == "a" or key == "d":
        player["position_x"] += keys[key]
    elif key == "w" or key == "s":
        player["position_y"] += keys[key]
    player_pos = board[player["position_y"]][player["position_x"]]
    if player_pos in NPC_COLLISION:
        return player_original
    return player
