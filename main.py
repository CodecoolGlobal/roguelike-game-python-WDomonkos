import util
import engine
import ui
from random import randint

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 5

BOARD_WIDTH = 30
BOARD_HEIGHT = 20
MAP_1 = 'map_1.txt'
MAP_2 = ''
MAP_3 = ''
MAP_LIST = [MAP_1, MAP_2, MAP_3]


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = { "icon": PLAYER_ICON, "position_x": PLAYER_START_X, "position_y": PLAYER_START_Y, "wallet": 0, "lives": 5, "current_room": 1}
    return player


def create_passer_by():
    passer_by = {"icon": "¤", "wallet": randint(0, 6)}
    return passer_by


def create_barkeeper():
    barkeeper = {"icon": "$", "drinks": 1, "wallet": 2}
    return barkeeper


def create_cop():
    cop = {"icon": "%", "weapon": 0}
    return cop


def create_boss():
    boss_jozsi = {"icon": "<>", "drinks": 1, "lives": 3}
    return boss_jozsi


def menu():
    print("""
  .   *   ..  . *  *
*  * @()Ooc()*   o  .
    (Q@*0CG*O()  ___
   |\_________/|/ _ \
   |  |  |  |  | / | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | \_| |
   |  |  |  |  |\___/
   |\_|__|__|_/|
    \_________/

    """)
    lives = choosing_difficulty()
    return lives


def choosing_difficulty():
    valid_input = False
    while not valid_input:
        difficulty = input("Choose a difficulty already!(h/e)")
        if difficulty.lower() == "h" or difficulty.lower() == "e":
            valid_input = True
        util.clear_screen()
    if difficulty == "h":
        lives = 3
    else:
        lives = 5
    return lives


def main():
    player = create_player()
    # board = engine.create_map()
    # board_for_print = util.map_indexing(board)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board1 = engine.board1(board)
    board2 = engine.board2(board)
    board3 = engine.board3(board)

    util.clear_screen()
    is_running = True
    while is_running:
        # engine.put_player_on_board(board_for_print, player)
        # ui.display_board(board_for_print)
        if player["current_room"] == 1:
            current_room = board1
        elif player["current_room"] == 2:
            current_room = board2
        elif player["current_room"] == 3:
            current_room = board3

        engine.put_player_on_board(current_room, player)
        ui.display_board(current_room)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            # player = engine.player_movement(board_for_print, player, key)
            player = engine.player_movement(current_room, player, key)
        util.clear_screen()


if __name__ == '__main__':
    main()
