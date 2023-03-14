class Tile:
    def __init__(self, location:tuple, n:int, normal_tile:bool=True):
        self.x = location[0]
        self.y = location[1]
        if normal_tile:
            self.neighbors = []
            self.state = 0 # 0 = empty, 1 = occupied player 1, 2 = occupied player 2.
            self.edge_tile = True if self.x == 0 or self.x == n-1 or self.y == 0 or self.y == n-1 else False
    
    # Boilerplate setters and getters
    def set_neighbors(self, neighbors:list):
        self.neighbors = neighbors
    
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state
    
    def get_location(self):
        return (self.x, self.y)
    
    def get_neighbors(self):
        return self.neighbors
    
    def is_edge_tile(self):
        return self.edge_tile
