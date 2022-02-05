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
        print(self.board.game_result())

    # Gets input from user and returns tuple of (length, height, num_mines).
    def get_game_type(self):
        # TODO(bonghyun): Add for custom.
        print("Enter Grid Type - ('Beginner', 'Medium', 'Expert')")
        game_type = input("'Beginner', 'Medium', 'Expert': ")
        if game_type == 'Beginner':
            return (9, 9, 10)
        elif game_type == 'Medium':
            return (16, 16, 40)
        elif game_type == 'Expert':
            return (16, 30, 99)
        else:
            raise ValueError("Unexpected game_type: %s" % game_type)

game_master = GameMaster()
game_master.start_game()
