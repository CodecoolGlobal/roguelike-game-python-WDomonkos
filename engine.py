from typing import Counter
from math import floor


def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    board = []
    for row in range(height):
        column = []
        for col in range(width):
            if row == 0 or row == height -1:    # northern and southern wall
                column.append("#")
            elif height % 2 == 1 and floor(height / 2) == row:  # gate if height is odd
                if col == 0 or col == width -1:
                    column.append(" ")
                else:
                    column.append("¤")
            elif height % 2 == 0 and (height / 2) -1 == row or (height / 2) == row:     # gate if height is even
                if col == 0 or col == width -1:
                    column.append(" ")
                else:
                    column.append("¤")
            else:                                   # every other row
                if col == 0 or col == width -1:
                    column.append("#")
                else:
                    column.append("¤")
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
    pass
