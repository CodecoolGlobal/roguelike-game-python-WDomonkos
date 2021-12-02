import util
from main import PLAYER_ICON, PLAYER_START_X, PLAYER_START_Y
import copy
from random import randint
import time


WALL = "▣"
EMPTY = " "
RIGHT_GATE = '\033[96m'+">"+'\033[00m'
LEFT_GATE = '\033[96m'+"<"+'\033[00m'
BAR_RIGHT_GATE = '\033[94m'+">"+'\033[00m'
STREET_RIGHT_GATE = '\033[93m'+">"+'\033[00m'
NEAR_BARKEEPER = "."
DOORKEY = "\033[92m"+"~"+"\033[00m"
NPC_COLLISION = [WALL, RIGHT_GATE, LEFT_GATE, DOORKEY, STREET_RIGHT_GATE, BAR_RIGHT_GATE]


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
    for i in [x for x in range(30) if x not in [6,7,13,14,22,23]]:
        new_board[8][i] = WALL

    new_board[2][-(len(orig_board[0])//2+2)] = "\033[92m"+"H"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2+1)] = "\033[92m"+"O"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2+0)] = "\033[92m"+"M"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-1)] = "\033[92m"+"E"+"\033[00m"

    new_board[randint(10, 18)][randint(1, 12)] = DOORKEY

    return new_board


def board2(orig_board):
    new_board = copy.deepcopy(orig_board)

    new_board[len(new_board)//2][-1] = STREET_RIGHT_GATE
    new_board[len(new_board)//2-1][-1] = STREET_RIGHT_GATE

    new_board[len(new_board)//2][0] = LEFT_GATE
    new_board[len(new_board)//2-1][0] = LEFT_GATE

    for i in range(4,18):
        new_board[5][i] = WALL
    for i in range(16,26):
        new_board[8][i] = WALL
    for i in range(6, 17):
        new_board[11][i] = WALL
    for i in range(10,22):
        new_board[15][i] = WALL

    new_board[2][-(len(orig_board[0])//2+3)] = "\033[92m"+"S"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2+2)] = "\033[92m"+"T"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2+1)] = "\033[92m"+"R"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-0)] = "\033[92m"+"E"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-1)] = "\033[92m"+"E"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-2)] = "\033[92m"+"T"+"\033[00m"

    return new_board


def board3(orig_board):
    new_board = copy.deepcopy(orig_board)

    new_board[len(new_board)//2][-1] = BAR_RIGHT_GATE
    new_board[len(new_board)//2-1][-1] = BAR_RIGHT_GATE

    new_board[len(new_board)//2][0] = LEFT_GATE
    new_board[len(new_board)//2-1][0] = LEFT_GATE

    for i in range(len(orig_board)-5):
        new_board[i][-8] = WALL

    for i in range(7,10):
        for j in range(-7,-4):
            new_board[i][j] = NEAR_BARKEEPER

    new_board[2][-5] = "\033[92m"+"B"+"\033[00m"
    new_board[2][-4] = "\033[92m"+"A"+"\033[00m"
    new_board[2][-3] = "\033[92m"+"R"+"\033[00m"

    return new_board


def board4(orig_board):
    new_board = copy.deepcopy(orig_board)

    new_board[len(new_board)//2][0] = LEFT_GATE
    new_board[len(new_board)//2-1][0] = LEFT_GATE

    new_board[2][-(len(orig_board[0])//2+3)] = "\033[92m"+"S"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2+2)] = "\033[92m"+"T"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2+1)] = "\033[92m"+"O"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-0)] = "\033[92m"+"R"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-1)] = "\033[92m"+"A"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-2)] = "\033[92m"+"G"+"\033[00m"
    new_board[2][-(len(orig_board[0])//2-3)] = "\033[92m"+"E"+"\033[00m"

    return new_board


def put_player_on_board(board, char_list, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    for _ in range(len(char_list)):
        for item in char_list:
            if player["random_id"] == item["random_id"]:
                for row in board:                   # UNDER CONSTRUCTION
                    if player["icon"] in row:
                        row[row.index(char_list[char_list.index(player)]["icon"])] = " "

                if board[player["position_y"]][player["position_x"]] != WALL:
                    board[player["position_y"]][player["position_x"]] = char_list[char_list.index(player)]["icon"]
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
        print("Oops, it looks like the door is closed")
        time.sleep(3)
        return player_original

    if player_position == STREET_RIGHT_GATE and player["wallet"] >= 5:
        player["current_room"] += 1
        player["position_y"] = len(board)//2
        player["position_x"] = 1
    elif player_position == STREET_RIGHT_GATE and player["wallet"] == 0:
        print("HEY, how do you want to buy a drink in the bar?")
        return player_original

    if player_position == BAR_RIGHT_GATE and player["broken_glass"] == 8:
        player["current_room"] += 1
        player["position_y"] = len(board)//2
        player["position_x"] = 1
    elif player_position == BAR_RIGHT_GATE and player["broken_glass"] == 0:
        return player_original
        
    if player_position == LEFT_GATE:
        player["current_room"] -= 1
        player["position_y"] = len(board)//2
        player["position_x"] = -2

    if player_position == NEAR_BARKEEPER:
        player["broken_glass"] += 1
    player = pick_up_item(player_position, player)
    
    return player


def npc_movement(board, npc, player, key):
    npc_original = npc.copy()
    keys = {"a": -1, "d": +1, "w": -1, "s": +1}
    if key == "a" or key == "d":
        npc["position_x"] += keys[key]
    elif key == "w" or key == "s":
        npc["position_y"] += keys[key]
    player_pos = board[npc["position_y"]][npc["position_x"]]
    if player_pos in NPC_COLLISION:
        return npc_original
    return npc


def pick_up_item(player_position, player):
    if player_position == DOORKEY:
        player["doorkey"] = 1
    return player


def is_colison(npc, main_character):
    main_position_y = main_character["position_y"]
    main_position_x = main_character["position_x"]
    character_position_y = npc["position_y"]
    character_position_x =  npc["position_x"]
    if all([main_position_y == character_position_y, main_position_x == character_position_x]):
        return True
    return False


def if_is_collison(npc_list, player):
    for char in npc_list:
        if is_colison(char, player):
            if char["icon"] == "\033[93m"+"¤"+"\033[00m":
                char["wallet"] -= 1
                player["wallet"] += 1
            elif any([char["icon"] == "\x1b[94m"+"♣"+"\x1b[00m", char["icon"] == "\x1b[96m"+"♣"+"\x1b[00m", char["icon"] == "\x1b[94m"+"%"+"\x1b[00m"]):
                player["lives"] -= 1
            elif char["icon"] == "\033[91m"+"♥"+"\033[00m":
                message = "\033[91m"+"Are you going to the pub again, you pig?!?"+"\033[00m"
            elif char["icon"] == "\033[95m"+"$"+"\033[00m":
                message = "\033[95m"+"Jozsi took the HOLY PALINKA to the storage. If you want to get drunk take it from him."+"\033[00m"
    return message
        