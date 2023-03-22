from disjoint_set import DisjointSet
from copy import deepcopy
import random

from game.tile import Tile


class Board:
    def __init__(self, gridsize:int):
        self.gridsize = gridsize
        self.board:list[list[Tile]] = []
        self.init_board()
        self.all_cells = []
        self.populate_cells()
        # Create 4 fake Tiles which represent the edges of the boards the players need to connect
        self.top_node = (-1, 0)
        self.bottom_node = (self.gridsize, 0)
        self.left_node = (0, -1)
        self.right_node = (0, self.gridsize)
        # Create the 2 disjoint set structures for each player
        self.red_ds = DisjointSet(self.all_cells + [self.top_node, self.bottom_node])
        self.blue_ds = DisjointSet(self.all_cells + [self.left_node, self.right_node])
        # Union the top and bottom row with top and bottom point in red_ds and similarly left and right points in blue_ds
        for i in range(self.gridsize):
            self.red_ds.union((0, i), self.top_node)
            self.red_ds.union((self.gridsize-1, i), self.bottom_node)
            self.blue_ds.union((i, 0), self.left_node)
            self.blue_ds.union((i, self.gridsize-1), self.right_node)

    # Initialises the board with tiles.
    def init_board(self):
        for row in range(self.gridsize):
            row_content = []
            for col in range(self.gridsize):
                row_content.append(Tile((row,col), self.gridsize))
            self.board.append(row_content)
        self.add_neighbors()
    
    # Adds the neighboring tiles of a tile to the neighbor list.
    def add_neighbors(self):
        for row_index, row in enumerate(self.board):
            for col_index, tile in enumerate(row):
                neighbors = []
                neighbors.append(self.board[row_index-1][col_index]) if tile.get_location()[0] > 0 else None
                neighbors.append(self.board[row_index+1][col_index]) if tile.get_location()[0] < self.gridsize-1 else None
                neighbors.append(self.board[row_index][col_index-1]) if tile.get_location()[1] > 0 else None
                neighbors.append(self.board[row_index][col_index+1]) if tile.get_location()[1] < self.gridsize-1 else None
                neighbors.append(self.board[row_index+1][col_index-1]) if tile.get_location()[0] < self.gridsize-1 and tile.get_location()[1] > 0 else None
                neighbors.append(self.board[row_index-1][col_index+1]) if tile.get_location()[0] > 0 and tile.get_location()[1] < self.gridsize-1 else None
                tile.set_neighbors(neighbors)
    
    def populate_cells(self):
        for row in self.board:
            for tile in row:
                self.all_cells.append(tile.get_location())
    
    def update_position_state(self, location:tuple, player:int):
        """
        Input:
            location (tuple): containing a valid x,y location on the board
            player (int): 1/2 depending on current player
        """
        self.board[location[0]][location[1]].set_state(player) # Sets the state of the tile at location, to be 1/2
        # Check for connecting neighbors
        for neighbour in self.board[location[0]][location[1]].get_neighbors():
            if neighbour.get_state() == player:
                if player == 1:
                    self.red_ds.union(neighbour.get_location(), location)
                else:
                    self.blue_ds.union(neighbour.get_location(), location)

    def check_position_state(self, location:tuple):
        """
        Input:
            location (tuple): containing a valid x,y location on the board
        
        Output:
            The state of the tile at that location on the board. 0 if empty, 1/2 if player 1/2 occupies it
        """
        return self.board[location[0]][location[1]].get_state()
    
    def check_winner(self):
        """
        Output:
            0 if no winner, 1/2 if player 1/2 has won
        """
        if self.red_ds.find(self.top_node) == self.red_ds.find(self.bottom_node):
            return 1
        elif self.blue_ds.find(self.left_node) == self.blue_ds.find(self.right_node):
            return 2
        return 0

    def get_board_states(self):
        all_states = []
        for row in self.board:
            for col in row:
                all_states.append(col.get_state())
        return all_states


    # Below are getter/setter boilerplate functions
    def contains_location(self, location:tuple):
        return location[0] >= 0 and location[0] < self.gridsize and location[1] >= 0 and location[1] < self.gridsize

    def get_board(self):
        return self.board
    
    def set_board(self, board:list):
        self.board = board
    
    def get_gridsize(self):
        return self.gridsize
    
    def display_board(self):
        current_board = []
        for row in self.board:
            current_row = []
            for tile in row:
                current_row.append(tile.get_state())
            current_board.append(current_row)
        
        print(*current_board, sep='\n')

    
    def get_moves(self):
        moves = []
        for row in range(self.get_gridsize()):
            for col in range(self.get_gridsize()):
                if self.check_position_state((row, col)) == 0:
                    moves.append((row, col))
        return moves
    
    def random_playout(self, player):
        if not self.check_winner() == 0:
            return self.check_winner()
        
        winner = 0
        while winner == 0:
            moves = self.get_moves()
            
            move = moves[random.randint(0, len(moves)-1)]
            self.update_position_state(move, player)
            winner = self.check_winner()
            player = 3-player
        return winner

    def clone_state(self):
        clone = Board(self.gridsize)
        for row in range(self.gridsize):
            row_content = []
            for col in range(self.gridsize):
                row_content.append(self.board[row][col].clone_tile())
            clone.board.append(row_content)
        clone.add_neighbors()
        clone.populate_cells()
        clone.red_ds = deepcopy(self.red_ds)
        clone.blue_ds = deepcopy(self.blue_ds)
        return clone
        

