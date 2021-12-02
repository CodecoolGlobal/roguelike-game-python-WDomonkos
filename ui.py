import time

def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for row in board:
        print(" ".join(row))

def display_message(string):
    if string != None:
        print(string)
        time.sleep(4)


def display_room_number_and_player_life(player : dict):
    roomnumber = player["current_room"]
    life = player["lives"] * "♥"
    print(f"Room {roomnumber}                                     lives: {life}")


def display_player_attributes(player):
    wallet = player["wallet"]
    broken_bottle = player["weapon"]
    key = player["doorkey"]
    glass = player["broken_glass"]
    print(f"money: {wallet}   weapon: {broken_bottle}    key: {key}     broken glass: {glass}")