import numpy as np

class Hex:
    def __init__(self, gridsize:int):
        self.gridsize = gridsize
        self.board = self.init_board()

    def step(self, action:tuple):
        pass

    def get_actions(self):
        return np.where(self.board == 0)
    
    def reset(self):
        pass

    def init_board(self):
        self.board = np.zeros((self.gridsize, self.gridsize))
    
    def update_board(self, pos:tuple, player:int):
        self.board[pos] = player

    def get_board(self):
        return self.board


    
        


    