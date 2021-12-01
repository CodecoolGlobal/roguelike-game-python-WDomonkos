import util
import engine
import ui

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
    player = { "icon": PLAYER_ICON, "position_x": PLAYER_START_X, "position_y": PLAYER_START_Y, "wallet": 0, "lives": 5, "current_room": 1}
    return player


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board1 = engine.board1(board)
    board2 = engine.board2(board)
    board3 = engine.board3(board)

    util.clear_screen()
    is_running = True
    while is_running:
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
            player = engine.player_movement(current_room, player, key)
        util.clear_screen()


if __name__ == '__main__':
    main()
