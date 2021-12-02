import sys
import os

from engine import EMPTY


def key_pressed():
    try:
        import tty, termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def is_empty(map_matrix: list, y_index, x_index):
    if map_matrix[y_index][x_index] != EMPTY:
        return True
    return False


def read_map(current_map):  # not used
    the_map = []
    with open(current_map) as file:
        for lines in file.readlines():
            if '\n' in lines:
                the_map.append(lines[:len(lines) - 1])
            else:
                the_map.append(lines)
    return the_map


def map_indexing(string_map):   # not used
    indexed_map = []
    for line in string_map:
        row = []
        for item in line:
            row.extend(item)
        indexed_map.append(row)
    return indexed_map
