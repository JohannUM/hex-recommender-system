import numpy as np
from game.tile import Tile

class Hex:
    def __init__(self, gridsize:int):
        self.gridsize = gridsize
        self.board = []
        self.init_board()
        self.add_neighbors()

    def step(self, action:tuple):
        self.update_board(action[0], action[1]) # If action[0] is another tuple representing location of tile, and action[1] is current player

    def get_actions(self):
        return np.where(self.board == 0)
    
    def reset(self):
        self.init_board()

    def init_board(self):
        for y in range(self.gridsize):
            row = []
            for x in range(self.gridsize):
                row.append(Tile((x,y), self.gridsize))
            self.board.append(row)
    
    def add_neighbors(self):
        for j, row in enumerate(self.board):
            for i, tile in enumerate(row):
                neighbors = []
                neighbors.append(self.board[i-1][j]) if tile.get_location()[0] > 0 else None
                neighbors.append(self.board[i+1][j]) if tile.get_location()[0] < self.gridsize-1 else None
                neighbors.append(self.board[i][j-1]) if tile.get_location()[1] > 0 else None
                neighbors.append(self.board[i][j+1]) if tile.get_location()[1] < self.gridsize-1 else None
                neighbors.append(self.board[i+1][j-1]) if tile.get_location()[0] < self.gridsize-1 and tile.get_location()[1] > 0 else None
                neighbors.append(self.board[i-1][j+1]) if tile.get_location()[0] > 0 and tile.get_location()[1] < self.gridsize-1 else None
                tile.add_neighbors(neighbors)
    
    def update_board(self, pos:tuple, player:int):
        self.board[pos] = player

    def get_board(self):
        return self.board


    
        


    