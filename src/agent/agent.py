from game.board import Board
from agent import minimax
from agent.mcts import MCTS

class Agent:

    def __init__(self, type):
        self.type = type
        self.hybrid_tresholds = {
            3: 0.0,
            5: 0.5,
            7: 0.7,
            9: 0.8,
            11: 0.9
        }


    def find_move(self, player, board:Board, hybrid_threshold=0.7):
        if self.type == 'minimax':
            return minimax.find_move(board, player)
        elif self.type == 'mcts':
            mcts = MCTS(player=player, game_state=board, max_depth=5)
            return mcts.predict()
        elif self.type == 'hybrid':
            if board.percentage_occupied() >= self.hybrid_tresholds[board.gridsize]:
                print('minimax')
                return minimax.find_move(board, player)
            else:
                print('mcts')
                mcts = MCTS(player=player, game_state=board, max_depth=5)
                return mcts.predict()
            
