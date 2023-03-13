import numpy as np

class Hex:

    def __init__(self, gridsize:tuple):
        self.gridsize = gridsize
        self.board = self.init_board()

    def step(self, action):

        pass

    def get_actions(self):
        return np.where(self.board == 0)
    
    def reset(self):
        pass

    def init_board(self):
        board = np.zeros((self.gridsize[0], self.gridsize[1]))

        return board

    
        


    