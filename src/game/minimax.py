from game.board import Board

from copy import deepcopy
from typing import List


class Node:

    def __init__(self, board:Board, player:int, move=None):
        self.board = board
        self.player = player
        self.move = move
        self.children:List[Node] = []

    def evaluate(self):
        if self.board.check_winner() == 1:
            return 1.0
        if self.board.check_winner() == 2:
            return -1.0
        return 0.0
    
    def expand(self):
        for move in self.board.get_moves():
            new_board = deepcopy(self.board)
            new_board.update_position_state(move, self.player)
            self.children.append(Node(board=new_board, player=3-self.player, move=move))
    
    def is_leaf(self):
        return len(self.children) > 0



def get_move(board:Board, player):
    root = Node(board=deepcopy(board), player=player)
    _, move = minimax(node=root, depth=6, is_maximizing=True if player==1 else False)
    return move


def minimax(node:Node, depth:int, alpha=float('-inf'), beta=float('inf'), is_maximizing=True):

    if depth == 0 or node.is_leaf():
        return node.evaluate(), None
    
    if is_maximizing:
        max_score, best_move = float('-inf'), None
        node.expand()
        for child in node.children:
            score, _ = minimax(child, depth-1, alpha, beta, False)
            if score > max_score:
                max_score, best_move = score, child.move
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score, best_move
    else:
        min_score, best_move = float('inf'), None
        node.expand()
        for child in node.children:
            score, _ = minimax(child, depth-1, alpha, beta, True)
            if score < min_score:
                min_score, best_move = score, child.move
            beta = min(beta, min_score)
            if beta <= alpha:
                break
        return min_score, best_move
    

