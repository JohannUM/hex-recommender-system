from game.board import Board

from copy import deepcopy
from typing import List

import random


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
        '''else:
            player1_path = self.board.largest_path(1)
            player2_path = self.board.largest_path(2)
            print('player1_path', player1_path)
            print('player2_path', player2_path)
    
            if player1_path > player2_path:
                score = (player1_path - player2_path) / player1_path
            elif player2_path > player1_path:
                score = -(player2_path - player1_path) / player2_path
            else:
                score = 0.0'''
        
        print(self.move, score)
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



def find_move(board:Board, player:int):
    root = Node(board=deepcopy(board), player=player, moves=board.get_moves())
    score, move = minimax(node=root, depth=5, is_maximizing=True if player==1 else False)
    print('Score', score)
    return move


def minimax(node:Node, depth:int, alpha=float('-inf'), beta=float('inf'), is_maximizing=True):
    if depth == 0 or node.is_leaf():
        if node.is_leaf():
            print('REACHED LEAF')
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
    

