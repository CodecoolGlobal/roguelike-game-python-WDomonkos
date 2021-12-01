import util
import engine
import ui
from random import choice, randint

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
    player = { "icon": PLAYER_ICON, "position_x": PLAYER_START_X, "position_y": PLAYER_START_Y, "wallet": 0, "lives": 5, "current_room": 1, "key": 0}
    return player

# def create_key():
#     key = {"icon": "~", "position_x": randint(1, BOARD_WIDTH -1), "position_y": randint(1, BOARD_HEIGHT-1)}

def create_passer_by():
    passer_by = {"icon": "¤", "wallet": randint(0, 6), "position_x": randint(1, BOARD_WIDTH -1), "position_y": randint(1, BOARD_HEIGHT-1)}
    return passer_by


def create_barkeeper():
    barkeeper = {"icon": "$", "drinks": 1, "wallet": 2, "position_x": -5, "position_y": randint(1, BOARD_HEIGHT-1)}
    return barkeeper


def create_cop():
    cop = {"icon": "%", "weapon": 0, "position_x": randint(1, BOARD_WIDTH -1), "position_y": randint(1, BOARD_HEIGHT-1)}
    return cop


def create_boss():
    boss_jozsi = {"icon": "§", "drinks": 1, "lives": 3, "position_x": 15, "position_y": 10}
    return boss_jozsi



def create_wife():
    wife = {"icon": "\033[93m"+"&"+"\033[00m", "wallet": 0, "position_x": randint(1, BOARD_WIDTH -1), "position_y": randint(1, BOARD_HEIGHT-1)}
    return wife


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
    passer_by = create_passer_by()
    cop1 = create_cop()
    cop2 = create_cop()
    cop3 = create_cop()
    wife = create_wife()
    barkeeper = create_barkeeper()
    boss = create_boss()
    # key = create_key()
    # board = engine.create_map()
    # board_for_print = util.map_indexing(board)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board1 = engine.board1(board)
    board2 = engine.board2(board)
    board3 = engine.board3(board)

    util.clear_screen()
    is_running = True
    while is_running:
        

        if player["current_room"] == 1:
            current_room = board1
            engine.put_player_on_board(current_room, wife)
            #engine.put_player_on_board(current_room, key)

        elif player["current_room"] == 2:
            current_room = board2
            engine.put_player_on_board(current_room, cop1)
            engine.put_player_on_board(current_room, cop2)
            engine.put_player_on_board(current_room, cop3)
            engine.put_player_on_board(current_room, passer_by)
        elif player["current_room"] == 3:
            current_room = board3
            engine.put_player_on_board(current_room, barkeeper)
            #engine.put_player_on_board(current_room, boss)

        engine.put_player_on_board(current_room, player)
        ui.display_board(current_room)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            # player = engine.player_movement(board_for_print, player, key)

            cop1 = engine.player_movement(current_room, cop1, key=choice(["s", "w"]))
            cop2 = engine.player_movement(current_room, cop2, key=choice(["s", "w"]))
            cop3 = engine.player_movement(current_room, cop3, key=choice(["s", "w"]))
            barkeeper = engine.player_movement(current_room, barkeeper, key=choice(["s", "w"]))
            passer_by = engine.player_movement(current_room, passer_by, key=choice(["a", "s", "d", "w"]))
            boss = engine.player_movement(current_room, boss, key=choice(["a", "s", "d", "w"]))
            wife = engine.player_movement(current_room, wife, key=choice(["a", "s", "d", "w"]))
            player = engine.player_movement(current_room, player, key)
        util.clear_screen()


if __name__ == '__main__':
    main()
