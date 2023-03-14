class Tile:
    def __init__(self, location:tuple, n:int, normal_tile:bool=True):
        self.row_index = location[0]
        self.col_index = location[1]
        if normal_tile:
            self.neighbors = []
            self.state = 0 # 0 = empty, 1 = occupied player 1, 2 = occupied player 2.
            self.edge_tile = True if self.row_index == 0 or self.row_index == n-1 or self.col_index == 0 or self.col_index == n-1 else False
    
    # Boilerplate setters and getters
    def set_neighbors(self, neighbors:list):
        self.neighbors = neighbors
    
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state
    
    def get_location(self):
        return (self.row_index, self.col_index)
    
    def get_neighbors(self):
        return self.neighbors
    
    def is_edge_tile(self):
        return self.edge_tile
