from copy import deepcopy

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


    def find_move(self, player, board:Board):
        move = None
        if self.type == 'minimax':
            move = minimax.find_move(board, player)
        elif self.type == 'mcts':
            mcts = MCTS(player=player, game_state=board, max_depth=5)
            move = mcts.predict()
        elif self.type == 'hybrid':
            if board.percentage_occupied() > self.hybrid_tresholds[board.gridsize]:
                #print('minimax')
                move = minimax.find_move(board, player)
            else:
                #print('mcts')
                mcts = MCTS(player=player, game_state=board, max_depth=5)
                move = mcts.predict()
        self.explainMove(player, move, board)
        return move
    
    def explainMove(self, player:int, move:tuple, board:Board):
        board_copy = deepcopy(board)
        board_copy.update_position_state(move, player)
        if board_copy.check_winner() == player:
            print(f'This move wins the game for player {player}.')
            return
        
        board_copy.update_position_state(move, 3-player)
        if board_copy.check_winner() == 3-player:
            print(f'This move blocks the opposing player from winning.')
            return
        
        print(f'This move advances the game and increases player {player}s chance of winning.')
        

            
