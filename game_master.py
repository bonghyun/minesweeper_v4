"""
Main Python function for running the Minesweeper game. Helps create the game
board and interact with user through input.
"""

from enum import Enum
import board

# Helps interact with the player and the board.
class GameMaster:

    def __init__(self):
        pass

    def start_game(self):
        # Initialize board with the given input.
        self.ms_board = board.MinesweeperBoard()

        while not self.ms_board.is_set_up():
            (num_xs, num_ys, num_mines) = self.get_game_type()
            self.ms_board.set_up(num_xs, num_ys, num_mines)

        # While game is still running, get next move from user, then try to play
        # that move.
        while self.ms_board.game_result == board.GameResultEnum.STILL_RUNNING:
            self.ms_board.print_board()
            (x_cord, y_cord, action) = self.get_next_move()
            (is_valid_move, err_msg) = self.ms_board.is_valid_move(
                x_cord, y_cord, action)

            if not is_valid_move:
                print("\nInvalid Move at x-cord: %s - y-cord: %s" % (x_cord, y_cord))
                print(" *Error Message: %s" % err_msg)
                continue

            self.ms_board.play_move(x_cord, y_cord, action)

        # Once the game is done, show the board.
        self.ms_board.print_board(True)

    # Gets input from user and returns tuple of (length, height, num_mines).
    def get_game_type(self):
        # TODO(bonghyun): Add for custom.
        while True:
            print("Enter Grid Type - ('Beginner', 'Medium', 'Expert')")
            game_type = input("'Beginner', 'Medium', 'Expert': ")
            if game_type in ('Beginner', 'B', 'b'):
                return (9, 9, 10)
            elif game_type in ('Medium', 'M', 'm'):
                return (16, 16, 40)
            elif game_type in ('Expert', 'E', 'e'):
                return (16, 30, 99)
            else:
                print("**Unexpected Game Type: %s" % game_type)


    # Gets input from user for the next move. Should give x_cord, y_cord, and
    # num_flags (0 to indicate no mine).
    def get_next_move(self):
        while True:
            print("Enter x coordinate - (0 .. %s)" % (self.ms_board.num_xs - 1))
            x_cord = input("0 .. %s: " % (self.ms_board.num_xs - 1))
            try:
                x_cord = int(x_cord)
            except:
                print("%s is not a valid int." % x_cord)
                continue
            if x_cord < 0 or x_cord >= self.ms_board.num_xs:
                print("%s is out of bounds." % x_cord)
            else:
                break

        while True:
            print("Enter y coordinate - (0 .. %s)" % (self.ms_board.num_ys - 1))
            y_cord = input("0 .. %s: " % (self.ms_board.num_ys - 1))
            try:
                y_cord = int(y_cord)
            except:
                print("%s is not a valid int." % y_cord)
                continue
            if y_cord < 0 or y_cord >= self.ms_board.num_ys:
                print("%s is out of bounds." % y_cord)
            else:
                break

        while True:
            print("Enter 'C' to click | 'F' to plant flag | 'U' to unplant a flag.")
            action_input = input("C or F or U: ")
            if action_input == "C" or action_input == "c":
                action = board.UserAction.CLICK
                break
            elif action_input == "F" or action_input == "f":
                action = board.UserAction.PLANT_FLAG
                break
            elif action_input == "U" or action_input == "u":
                action = board.UserAction.UNPLANT_FLAG
                break
            else:
                print("%s it not a valid action." % action_input)

        return (x_cord, y_cord, action)


game_master = GameMaster()
game_master.start_game()
