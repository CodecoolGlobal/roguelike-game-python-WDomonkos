import util
import engine
import ui
from random import choice, randint

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 5

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player(life):
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''

    player = {"icon": PLAYER_ICON, "position_x": PLAYER_START_X, "position_y": PLAYER_START_Y, "wallet": 0, "lives": life, "current_room": 1, "doorkey": 0, "weapon": 0, "broken_glass": 0, "random_id": randint(10000, 99999)}
    return player


def create_key():
    key = {"icon": "~", "position_x": randint(1, BOARD_WIDTH - 1), "position_y": randint(1, BOARD_HEIGHT - 1)}
    return key


def create_passer_by():
    passer_by = {"icon": "\033[93m"+"¤"+"\033[00m", "wallet": randint(6, 6), "position_x": randint(1, BOARD_WIDTH - 1), "position_y": randint(BOARD_HEIGHT//2, BOARD_HEIGHT//2), "random_id": randint(10000, 99999)}
    return passer_by


def create_barkeeper():
    barkeeper = {"icon": "\033[95m"+"$"+"\033[00m", "drinks": 1, "wallet": 2, "position_x": -6, "position_y": 8, "random_id": randint(10000, 99999)}
    return barkeeper


def create_cop1():
    cop = {"icon": "\033[94m"+"♣"+"\033[00m", "weapon": 0, "position_x": randint(1, BOARD_WIDTH - 2), "position_y": randint(1, BOARD_HEIGHT - 2), "random_id": randint(10000, 99999)}
    return cop


def create_cop2():
    cop = {"icon": "\033[94m"+"♣"+"\033[00m", "weapon": choice([1]), "position_x": randint(1, BOARD_WIDTH - 2), "position_y": randint(1, BOARD_HEIGHT - 2), "random_id": randint(10000, 99999)}
    return cop


def create_cop3():
    cop = {"icon": "\033[94m"+"♣"+"\033[00m", "weapon": choice([1]), "position_x": randint(1, BOARD_WIDTH - 3), "position_y": randint(1, BOARD_HEIGHT - 3), "random_id": randint(10000, 99999)}
    return cop


def create_boss():
    boss_jozsi = {"icon": "§", "drinks": 1, "lives": 3, "position_x": 15, "position_y": 10}
    return boss_jozsi


def create_wife():
    wife = {"icon": "\033[91m"+"♥"+"\033[00m", "wallet": 0, "position_x": randint(12, 25), "position_y": randint(3, 7), "random_id": randint(10000, 99999)}
    return wife



def menu():
    print(r"""


  .   *   ..  . *  *
*  * @()Ooc()*   o  .
    (Q@*0CG*O()  ___
   |\_________/|/ _  \
   |  |  |  |  | / | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | \_| |
   |  |  |  |  |\___ /
   |\_|__|__|_/|
    \_________/

    """)
    lives = choosing_difficulty()
    return lives


def choosing_difficulty():
    valid_input = False
    while not valid_input:
        difficulty = input("Choose a difficulty already!\nh - hard\ne - easy\n")
        if difficulty.lower() == "h" or difficulty.lower() == "e":
            valid_input = True
        util.clear_screen()
    if difficulty == "h":
        lives = 3
    else:
        lives = 5
    return lives


def main():
    difficulty = menu()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board1 = engine.board1(board)
    board2 = engine.board2(board)
    board3 = engine.board3(board)
    board4 = engine.board4(board)
    player = create_player(difficulty)
    passer_by = create_passer_by()
    cop1 = create_cop1()
    cop2 = create_cop2()
    cop3 = create_cop3()
    wife = create_wife()
    while util.is_empty(board1, wife['position_y'], wife['position_x']):    # create a function for these to check, only for refactor
        wife = create_wife()
    while util.is_empty(board2, cop1['position_y'], cop1['position_x']):
        cop1 = create_cop1()
    while util.is_empty(board2, cop2['position_y'], cop2['position_x']):
        cop2 = create_cop2()
    barkeeper = create_barkeeper()
    boss = create_boss()

    util.clear_screen()
    is_running = True
    while is_running:
        character_list = [player, passer_by, cop1, cop2, cop3, wife, barkeeper]     #Boss is missing
        if player["current_room"] == 1:
            current_room = board1
            engine.put_player_on_board(board1, character_list, wife)

        elif player["current_room"] == 2:
            current_room = board2
            engine.put_player_on_board(current_room, character_list, cop1)
            engine.put_player_on_board(current_room, character_list, cop2)
            engine.put_player_on_board(current_room, character_list, cop3)
            engine.put_player_on_board(current_room, character_list, passer_by)
        elif player["current_room"] == 3:
            current_room = board3
            engine.put_player_on_board(board3, character_list, barkeeper)
            #engine.put_player_on_board(current_room, boss)
        elif player["current_room"] == 4:
            current_room = board4
            #engine.put_player_on_board(current_room, boss)

        engine.put_player_on_board(current_room, character_list, player)
        ui.display_room_number_and_player_life(player)
        ui.display_board(current_room)
        ui.display_player_attributes(player)
        message = engine.if_is_collison(character_list, player)
        ui.display_message(message)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            # player = engine.player_movement(board_for_print, player, key)
            
            cop1 = engine.npc_movement(board2, cop1, player, key=choice(["s", "w"]))
            cop2 = engine.npc_movement(board2, cop2, player, key=choice(["s", "w"]))
            cop3 = engine.npc_movement(board2, cop3, player, key=choice(["a", "s", "d", "w"]))
            passer_by = engine.npc_movement(board2, passer_by, player, key=choice(["a", "s", "d", "w"]))
            # boss = engine.player_movement(current_room, boss, key=choice(["a", "s", "d", "w"]))
            wife = engine.npc_movement(board1, wife, player, key=choice(["a", "s", "d", "w"]))
            player = engine.player_movement(current_room, player, key)
        
        if engine.has_lost(player):
            ui.display_message("You are dead, looser!")
            is_running = False

        util.clear_screen()


if __name__ == '__main__':
    main()
