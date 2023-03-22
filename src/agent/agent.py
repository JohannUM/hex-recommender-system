from game.board import Board
from agent import minimax

class Agent:

    def __init__(self, type):
        self.type = type


    def find_move(self, player, board:Board):
        if self.type == 'minimax':
            return minimax.find_move(board, player)
        elif self.type == 'mcts':
            # TODO implement and add MCTS agent
            pass
        elif self.type == 'hybrid':
            # TODO implement and add hybrid agent
            pass
