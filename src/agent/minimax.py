from game.board import Board

from copy import deepcopy
from typing import List

import random
import time


class Node:

    def __init__(self, board:Board, player:int, move=None, moves:List=None):
        self.board = board
        self.player = player
        self.move = move
        self.moves = moves
        self.children:List[Node] = []

        random.shuffle(self.moves)

    def evaluate(self):
        if self.board.check_winner() == 1:
            score = 1.0
        elif self.board.check_winner() == 2:
            score = -1.0
        else:
            score = 0.0
        
        return score
    
    def expand(self):
        for move in self.moves:
            new_board = deepcopy(self.board)
            new_board.update_position_state(move, self.player)
            new_moves = self.moves.copy()
            new_moves.remove(move)
            self.children.append(Node(board=new_board, player=3-self.player, move=move, moves=new_moves))
    
    def is_leaf(self):
        return not self.board.check_winner() == 0



def find_move(board:Board, player:int, max_depth=10, time_limit:int=5):
    root = Node(board=board, player=player, moves=board.get_moves())
    best_move = None
    start_time = time.time()
    depth = 1
    while time.time() - start_time < time_limit:
        if depth > max_depth:
            break
        score, move = minimax(node=root, depth=depth, is_maximizing=True if player==1 else False, start_time=start_time, time_limit=time_limit)
        if move is not None:
            best_move = move
        depth += 1
    return best_move



def minimax(node: Node, depth: int, alpha: float = float('-inf'), beta: float = float('inf'), is_maximizing: bool = True, start_time: float = None, time_limit: int = None):
    #print(f'Currently running for {time.time() - start_time}')
    if start_time is not None and time_limit is not None and time.time() - start_time > time_limit:
        return None, None
    if depth == 0 or node.is_leaf():
        return node.evaluate(), None
    
    if is_maximizing:
        node.expand()
        children = sorted(node.children, key=lambda x: x.evaluate(), reverse=True)
        max_score, best_move = float('-inf'), None
        for child in children:
            score, _ = minimax(child, depth - 1, alpha, beta, False, start_time, time_limit)
            if score is None:
                return None, None
            if score > max_score:
                max_score, best_move = score, child.move
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score, best_move
    else:
        node.expand()
        children = sorted(node.children, key=lambda x: x.evaluate())
        min_score, best_move = float('inf'), None
        for child in children:
            score, _ = minimax(child, depth - 1, alpha, beta, True, start_time, time_limit)
            if score is None:
                return None, None
            if score < min_score:
                min_score, best_move = score, child.move
            beta = min(beta, min_score)
            if beta <= alpha:
                break
        return min_score, best_move

    

