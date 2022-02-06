"""
Board class that controlls Minesweeper board.
"""

from enum import Enum


class GameResult(Enum):
    STILL_RUNNING = 1
    WON = 2
    DEFEAT = 3


class UserAction(Enum):
    CLICK = 1
    PLANT_FLAG = 2


class Square:

    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.has_mine = False
        self.true_num_flags = 0
        self.user_clicked = False
        self.user_guess_flags = 0


# Minesweeper Board. Represents the entire board, including each of its
# individual squares.
class MinesweeperBoard:

    def __init__(self):
        self.num_xs = None
        self.num_ys = None
        self.num_mines = None
        self.squares = {}

    def set_up(self, num_xs, num_ys, num_mines):
        self.num_xs = num_xs
        self.num_ys = num_ys
        self.num_mines = num_mines

        self.print_line_break()
        print("Setting up [%s X %s] Board with # %s Mines" %
              (num_xs, num_ys, num_mines))

        for x in range(self.num_xs):
            self.squares[x] = {}
            for y in range(num_ys):
                self.squares[x][y] = Square(x, y)

    def is_set_up(self):
        return (self.num_xs is not None and
                self.num_ys is not None and
                self.num_mines is not None)

    def print_line_break(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def print_board(self):
        print("-------------------")

    def print_debug_board(self):
        print("+_+_+_+_+_+_+_+_+_+_")

    def game_result(self):
        return GameResult.STILL_RUNNING

    def is_valid_move(self, x_cord, y_cord, action):
        return (False, "Error")

    def play_move(self, x_cord, y_cord, action):
        pass
