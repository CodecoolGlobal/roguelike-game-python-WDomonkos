import util
import engine
import ui
from random import randint

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = { "icon": PLAYER_ICON, "position_x": PLAYER_START_X, "position_y": PLAYER_START_Y, "wallet": 0, "lives": 5}
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
    if difficulty == "h":
        lives = 3
    else:
        lives = 5
    return lives


def main(lives):
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            player = engine.player_movement(board, player, key)
        util.clear_screen()


if __name__ == '__main__':
    main()
