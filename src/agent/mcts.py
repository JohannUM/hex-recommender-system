from copy import deepcopy
import math
from game.board import Board
import time
from threading import Thread

class MCTS:

    def __init__(self, player:int, game_state:Board, max_depth:int):
        self.previous_player = 3-player
        self.player = player
        self.root = Node(game_state, None, self.previous_player, move=None)
        self.max_depth = max_depth
        self.leaves:list[Node] = []
        
    def predict(self):
        current_node = self.root
        self.leaves.append(self.root)
        for _ in range(self.max_depth):
            
            current_children = current_node.create_children()
            self.leaves.extend(current_children)
            self.leaves.remove(current_node)
            #print(f'Size of leaves {len(self.leaves)}')

            if len(self.leaves) == 0:
                break

            for leaf in self.leaves:
                leaf.roll_out(player=self.player)

            for child in self.root.children:
                Thread(target=child.update()).start()

            best_score = -1
            for leaf in self.leaves:
                if leaf.score > best_score:
                    current_node = leaf
                    best_score = leaf.score

        best_move = None
        best_score = -1
        for child in self.root.children:
            if child.score > best_score:
                best_score = child.score
                best_move = child.move

        return best_move
        
class Node:

    def __init__(self, game_state:Board, parent:"Node", current_player:int, move:tuple):
        self.game_state = game_state
        self.parent = parent
        self.current_player = current_player
        self.move = move
        self.C = math.sqrt(2)
        self.w, self.n, self.N = 0, 0, 0
        self.score = 0
        self.next_player = 3-self.current_player
        self.children:list[Node] = []

        
    def create_children(self):
        possible_moves = self.game_state.get_moves()
        
        for move in possible_moves:
            new_state = deepcopy(self.game_state)
            new_state.update_position_state(move, self.next_player)
            self.children.append(Node(game_state=new_state, parent=self, current_player=self.next_player, move=move))
        return self.children


    def roll_out(self, player:int):
        # winner = self.game_state.clone_state().random_playout(self.next_player)
        winner = deepcopy(self.game_state).random_playout(self.next_player)
        win = 1 if winner == player else 0
        
        self.backpropagate(win=win)

    
    def backpropagate(self, win:int):
        self.w += win
        self.n += 1
        if self.parent is not None:
            self.parent.backpropagate(win=win)


    def update(self):
        if self.parent is not None:
            self.N = self.parent.n
            a = self.w / self.n
            b = math.log(self.N) / self.n
            c = math.sqrt(b)
            self.score = a + self.C * c
        for child in self.children:
            child.update()

    def __str__(self):
        return f'score = {self.score}\n w = {self.w}\n n = {self.n}\n N = {self.N}\n'
    
    def print_tree(self, depth:str):
        tabs = ''
        for i in range(depth): 
            tabs = tabs + '\t'
        content = f'[w={self.w}|n={self.n}|N={self.N}|score={self.score}]'
        print(f'{tabs}{content}')
        for child in self.children:
            child.print_tree(depth=(depth+1))
        

    