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
        (board_l, board_h, num_mines) = self.get_game_type()
        self.board = board.MinesweeperBoard(board_l, board_h, num_mines)
        while self.board.game_result() == board.GameResult.STILL_RUNNING:
            self.board.display_board()
            (x_cord, y_cord, num_flags) = self.get_next_move()
            (is_valid_move, err_msg) = self.board.is_valid_move(
                x_cord, y_cord, num_flags)

            if not is_valid_move:
                print("Invalid Move at x-cord: %s - y-cord: %s" % (x_cord, y_cord))
                print(" Error Message: %s" % err_msg)
                continue

            self.board.play_move(x_cord, y_cord, num_flags)

        if self.board.game_result() == board.GameResult.WON:
            print("You won!")
            self.board.display_board()
        elif self.board.game_result() == board.GameResult.DEFEAT:
            print("You lost!")
            self.board.display_board()
        else:
            raise ValueError("Unexpected game reuslt: %s" % self.board.game_result())

    # Gets input from user and returns tuple of (length, height, num_mines).
    def get_game_type(self):
        # TODO(bonghyun): Add for custom.
        print("Enter Grid Type - ('Beginner', 'Medium', 'Expert')")
        game_type = input("'Beginner', 'Medium', 'Expert': ")
        if game_type == 'Beginner':
            self.max_x_cord = 10
            self.max_y_cord = 10
            self.num_mines = 10
        elif game_type == 'Medium':
            self.max_x_cord = 16
            self.max_y_cord = 16
            self.num_mines = 40
        elif game_type == 'Expert':
            self.max_x_cord = 16
            self.max_y_cord = 30
            self.num_mines = 99
        else:
            raise ValueError("Unexpected game_type: %s" % game_type)
        return (self.max_x_cord, self.max_y_cord, self.num_mines)

    # Gets input from user for the next move. Should give x_cord, y_cord, and
    # num_flags (0 to indicate no mine).
    def get_next_move(self):
        print("Enter x coordinate - (1 .. %s)" % self.max_x_cord)
        x_cord = input("1 .. %s: " % self.max_x_cord)

        print("Enter y coordinate - (1 .. %x)" % self.max_y_cord)
        y_cord = input("1 .. %s: " % self.max_y_cord)

        print ("Enter Number of Flags. Enter 0 for no mines")
        num_flags = input("0 .. %s: " % self.num_mines)

        return (x_cord, y_cord, num_flags)


game_master = GameMaster()
game_master.start_game()
