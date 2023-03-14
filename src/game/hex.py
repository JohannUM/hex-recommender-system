import numpy as np

from game.board import Board

class Hex:
    def __init__(self, gridsize:int):
        self.gridsize = gridsize
        self.board = Board(self.gridsize)
        self.init_board()
