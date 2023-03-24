from game.board import Board
from agent import minimax
from agent.mcts import MCTS

class Agent:

    def __init__(self, type):
        self.type = type
        self.hybrid_tresholds = {
            3: 0.4,
            5: 0.7,
            7: 0.8,
            9: 0.9,
            11: 0.95
        }


    def find_move(self, player, board:Board):
        move = None
        if self.type == 'minimax':
            move = minimax.find_move(board, player)
        elif self.type == 'mcts':
            mcts = MCTS(player=player, game_state=board, max_depth=30)
            move = mcts.predict()
        elif self.type == 'hybrid':
            if board.percentage_occupied() > self.hybrid_tresholds[board.gridsize]:
                move = minimax.find_move(board, player)
            else:
                mcts = MCTS(player=player, game_state=board, max_depth=30)
                move = mcts.predict()
        self.explainMove(player, move, board)
        return move
    
    def explainMove(self, player:int, move:tuple, board:Board):
        board_copy = board.clone_state()
        board_copy.update_position_state(move, player)
        print('\nExplanation:')
        if board_copy.check_winner() == player:
            print(f'This move wins the game for player {player}.')
            return
        
        board_copy_2 = board.clone_state()
        board_copy_2.update_position_state(move, 3-player)
        if board_copy_2.check_winner() == 3-player:
            print(f'This move blocks the opposing player from winning.')
            return
        
        print(f'This move advances the game and increases player {player}s chance of winning.')
        

            
