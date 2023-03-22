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
            '''player1_path = self.board.largest_path(1)
            player2_path = self.board.largest_path(2)
    
            if player1_path > player2_path:
                score = (player1_path - player2_path) / player1_path
            elif player2_path > player1_path:
                score = -(player2_path - player1_path) / player2_path
            else:
                score = 0.0'''
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



def find_move(board:Board, player:int):
    root = Node(board=deepcopy(board), player=player, moves=board.get_moves())
    score, move = minimax(node=root, depth=5, is_maximizing=True if player==1 else False)
    print(f'minimax decides {move} with score {score}')
    return move


def minimax(node: Node, depth: int, alpha: float = float('-inf'), beta: float = float('inf'), is_maximizing: bool = True, transposition_table: dict = None):
    if depth == 0 or node.is_leaf():
        if node.is_leaf():
            print('REACHED LEAF')
        return node.evaluate(), None
    
    if transposition_table is not None and node.board in transposition_table:
        return transposition_table[node.board], None
    
    if is_maximizing:
        node.expand()
        children = sorted(node.children, key=lambda x: x.evaluate(), reverse=True)
        max_score, best_move = float('-inf'), None
        for child in children:
            score, _ = minimax(child, depth - 1, alpha, beta, False, transposition_table)
            if score > max_score:
                max_score, best_move = score, child.move
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        if transposition_table is not None:
            transposition_table[node.board] = max_score
        return max_score, best_move
    else:
        node.expand()
        children = sorted(node.children, key=lambda x: x.evaluate())
        min_score, best_move = float('inf'), None
        for child in children:
            score, _ = minimax(child, depth - 1, alpha, beta, True, transposition_table)
            if score < min_score:
                min_score, best_move = score, child.move
            beta = min(beta, min_score)
            if beta <= alpha:
                break
        if transposition_table is not None:
            transposition_table[node.board] = min_score
        return min_score, best_move
    

