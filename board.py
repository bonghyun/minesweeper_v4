"""
Board class that controlls Minesweeper board.
"""

from enum import Enum
import random

class GameResult(Enum):
    STILL_RUNNING = 1
    WON = 2
    DEFEAT = 3


class UserAction(Enum):
    CLICK = 1
    PLANT_FLAG = 2


class Square:

    def __init__(self, x_cord, y_cord, has_mine):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.has_mine = has_mine
        self.adj_mine_count = 0
        self.shown_to_user = False
        self.user_planted_flag = False

    def get_print_str_for_user(self):
        if self.user_planted_flag:
            return " F "
        if self.shown_to_user:
            return " %s " % self.adj_mine_count
        else:
            return "   "

    def get_print_str_for_debug(self):
        if self.has_mine:
            return " X "
        else:
            return " %s " % self.adj_mine_count


# Minesweeper Board. Represents the entire board, including each of its
# individual squares.
class MinesweeperBoard:

    def __init__(self):
        self.num_xs = None
        self.num_ys = None
        self.num_mines = None
        self.squares = {}

    # Sets up the game with given input. Sets up the squares along with all its
    # adjacent edges.
    def set_up(self, num_xs, num_ys, num_mines):
        self.num_xs = num_xs
        self.num_ys = num_ys
        self.num_mines = num_mines

        self.print_line_break()
        print("Setting up [%s X %s] Board with # %s Mines" %
              (num_xs, num_ys, num_mines))

        # Set up initial square vertices. Also set up squares with mines.
        mine_squares = self._get_random_mined_squares()
        s_count = 0
        for x in range(self.num_xs):
            self.squares[x] = {}
            for y in range(num_ys):
                has_mine = s_count in mine_squares
                self.squares[x][y] = Square(x, y, has_mine)
                s_count = s_count + 1

        # Set up edges from each squares.

    # Given a square counts from 0 to (num_xs * num_ys), it will randomly sample
    # num_mines.
    def _get_random_mined_squares(self):
        total_num_squares = self.num_xs * self.num_ys
        return set(random.sample(range(total_num_squares), self.num_mines))

    # Returns true if the board has been set up.
    def is_set_up(self):
        return (self.num_xs is not None and
                self.num_ys is not None and
                self.num_mines is not None)

    # Prints line break so user can see between their inputs better.
    def print_line_break(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

    # Print the board for the user.
    def print_board(self, debug=False):
        self.print_line_break()

        for y in reversed(range(self.num_ys)):
            y_row_to_print = ("%s| " % y)
            for x in range(self.num_xs):
                square = self.squares[x][y]
                if debug:
                    y_row_to_print += square.get_print_str_for_debug()
                else:
                    y_row_to_print += square.get_print_str_for_user()
            print(y_row_to_print)

        x_break = "   "
        x_label = "   "
        for x in range(self.num_xs):
            x_break += "---"
            x_label += (" %s " % str(x))
        print(x_break)
        print(x_label)

    # Return the current game result. Could be STILL_RUNNING, WON, or DEFEAT.
    def game_result(self):
        return GameResult.STILL_RUNNING

    # Checks if the user move is valid.
    def is_valid_move(self, x_cord, y_cord, action):
        return (False, "Error")

    # Plays the given user's input.
    def play_move(self, x_cord, y_cord, action):
        pass
