"""
Board class that controlls Minesweeper board.
"""

from enum import Enum

class GameResult(Enum):
    STILL_RUNNING = 1
    WON = 2
    DEFEAT = 3


# Minesweeper Board. Represents the entire board, including each of its
# individual squares.
class MinesweeperBoard:

    def __init__(self, board_length, board_height, num_mines):
        self.board_length = board_length
        self.board_height = board_height
        self.num_mines = num_mines

    def game_result(self):
        return GameResult.STILL_RUNNING
