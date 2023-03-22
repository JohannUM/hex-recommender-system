from game.board import Board
from agent import minimax
from agent.mcts import MCTS

class Agent:

    def __init__(self, type):
        self.type = type


    def find_move(self, player, board:Board):
        if self.type == 'minimax':
            return minimax.find_move(board, player)
        elif self.type == 'mcts':
            mcts = MCTS(player=player, game_state=board, max_depth=50)
            return mcts.predict()
        elif self.type == 'hybrid':
            if board.percentage_occupied() > 0.7:
                print('minimax')
                return minimax.find_move(board, player)
            else:
                print('mcts')
                mcts = MCTS(player=player, game_state=board, max_depth=50)
                return mcts.predict()
            
