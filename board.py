"""
Board class that controlls Minesweeper board.
"""

from enum import Enum
import random

# Enums representing game result.
class GameResultEnum(Enum):
    STILL_RUNNING = 1
    WON = 2
    DEFEAT = 3

# Enums representing user's action.
class UserAction(Enum):
    CLICK = 1
    PLANT_FLAG = 2

# Enums representing square shown to the user.
class SquareShownEnum(Enum):
    BLANK = 1
    MINE_EXPLODED = 2
    USER_PLANTED_FLAG = 3
    SAFELY_SHOWN = 4


# Minesweeper Board. Represents the entire board, including each of its
# individual squares.
class MinesweeperBoard:

    # Class representing each square in the board.
    class Square:
        def __init__(self, x_cord, y_cord, has_mine):
            self.x_cord = x_cord
            self.y_cord = y_cord
            self.has_mine = has_mine
            self.adj_mine_count = 0
            self.square_shown_state = SquareShownEnum.BLANK

        def __str__(self):
            return "[%s][%s] | has_mine: %s | adj_mine_cnt: %s | square_shown_state: %s" % (self.x_cord, self.y_cord, self.has_mine, self.adj_mine_count, self.square_shown_state)

        def increment_adj_mine_count(self):
            self.adj_mine_count += 1

        def get_print_str_for_user(self):
            if self.square_shown_state == SquareShownEnum.BLANK:
                return "   "
            elif self.square_shown_state == SquareShownEnum.MINE_EXPLODED:
                return " ! "
            elif self.square_shown_state == SquareShownEnum.USER_PLANTED_FLAG:
                return " F "
            else:
                return " %s " % self.adj_mine_count

        def get_print_str_for_debug(self):
            if self.square_shown_state == SquareShownEnum.MINE_EXPLODED:
                return " ! "
            if self.has_mine:
                return " X "
            return " %s " % self.adj_mine_count

    # Set up class variables.
    def __init__(self):
        self.game_result = GameResultEnum.STILL_RUNNING
        self.num_xs = None
        self.num_ys = None
        self.num_mines = None
        self.squares = {}
        self.square_edges = {}
        self.num_safely_shown_squares = 0
        self.expected_safe_squares = 0

    # Sets up the game with given input. Sets up the squares along with all its
    # adjacent edges.
    def set_up(self, num_xs, num_ys, num_mines):

        # Given a square counts from 0 to (num_xs * num_ys), it will randomly
        # sample num_mines.
        def _get_random_mined_squares(num_xs, num_ys, num_mines):
            total_num_squares = num_xs * num_ys
            return set(random.sample(range(total_num_squares), num_mines))

        # Given a starting vertex (new_tup), check if the edge (tup) is valid.
        def _is_valid_new_tup(new_tup, tup, num_xs, num_ys):
            if new_tup == tup:
                return False
            if new_tup[0] < 0 or new_tup[0] >= num_xs:
                return False
            if new_tup[1] < 0 or new_tup[1] >= num_ys:
                return False
            return True

        self.num_xs = num_xs
        self.num_ys = num_ys
        self.num_mines = num_mines

        self.print_line_break()
        print("Setting up [%s X %s] Board with # %s Mines" %
              (num_xs, num_ys, num_mines))

        # Set up initial square vertices. Also set up squares with mines.
        mine_squares = _get_random_mined_squares(self.num_xs,
                                                 self.num_ys,
                                                 self.num_mines)
        s_count = 0
        for x in range(self.num_xs):
            self.squares[x] = {}
            for y in range(num_ys):
                has_mine = s_count in mine_squares
                self.squares[x][y] = self.Square(x, y, has_mine)
                s_count = s_count + 1

        # Set up edges from each squares.
        for x in range(self.num_xs):
            for y in range(self.num_ys):
                tup = (x, y)
                edges = []
                for x_change in (-1, 0, 1):
                    for y_change in (-1, 0, 1):
                        new_tup = (x + x_change, y + y_change)
                        if _is_valid_new_tup(new_tup, tup,
                                             self.num_xs, self.num_ys):
                            edges.append(new_tup)
                self.square_edges[tup] = edges

        # Loop through edges of all the squares and increment adj_mine_count.
        for x in range(self.num_xs):
            for y in range(self.num_ys):
                if not self.squares[x][y].has_mine:
                    continue
                square_tup = (x, y)
                for edge_tup in self.square_edges[square_tup]:
                    (edge_tup_x, edge_tup_y) = edge_tup
                    self.squares[edge_tup_x][edge_tup_y].increment_adj_mine_count()

        # Set expected_safe_squares
        self.expected_safe_squares = (self.num_xs * self.num_ys) - self.num_mines

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

    # Checks if the user move is valid.
    def is_valid_move(self, x_cord, y_cord, action):
        square = self.squares[x_cord][y_cord]
        if square.square_shown_state != SquareShownEnum.BLANK:
            return (False, "Square[%s][%s] already shown" % (x_cord, y_cord))
        return (True, "Success")

    # Plays the given user's input.
    def play_move(self, x_cord, y_cord, action):
        square = self.squares[x_cord][y_cord]
        if action == UserAction.PLANT_FLAG:
            square.square_shown_state = SquareShownEnum.USER_PLANTED_FLAG
            return
        elif action == UserAction.CLICK:
            if square.has_mine:
                print("!!! Clicked on Mine Square[%s][%s] !!!" % (x_cord, y_cord))
                square.square_shown_state = SquareShownEnum.MINE_EXPLODED
                self.game_result = GameResultEnum.DEFEAT
                return
        else:
            raise ValueError("Invalid action: %s" % action)

        # User has clicked on a non-mine square. Traverse edges to see if other
        # squares should be shown.
        traverse_list = [(x_cord, y_cord)]
        traversed_set = set()
        while traverse_list:
            # For a given square, put it to traversed_list and set shown_to_user
            # as True. If the given square's adj_mine_count is 0, append the
            # edges.
            (traverse_x_cord, traverse_y_cord) = traverse_list.pop()
            if (traverse_x_cord, traverse_y_cord) in traversed_set:
                continue
            traversed_set.add((traverse_x_cord, traverse_y_cord))

            square = self.squares[traverse_x_cord][traverse_y_cord]
            square.square_shown_state = SquareShownEnum.SAFELY_SHOWN
            self.num_safely_shown_squares += 1

            if square.adj_mine_count == 0:
                for edge_tup in self.square_edges[(traverse_x_cord, traverse_y_cord)]:
                    traverse_list.append(edge_tup)

        if self.num_safely_shown_squares == self.expected_safe_squares:
            self.game_result = GameResultEnum.WON
