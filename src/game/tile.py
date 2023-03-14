class Tile:
    def __init__(self, location:tuple, n:int):
        self.x = location[0]
        self.y = location[1]
        self.generate_neighbors(n)
        self.state = 0 # 0 = empty, 1 = occupied player 1, 2 = occupied player 2.
        self.edge_tile = True if self.x == 0 or self.x == n-1 or self.y == 0 or self.y == n-1 else False
    
    def generate_neighbors(self, n:int):
        self.neighbors = []
        self.neighbors.append((self.x-1, self.y)) if self.x > 0 else None
        self.neighbors.append((self.x+1, self.y)) if self.x < n-1 else None
        self.neighbors.append((self.x, self.y-1)) if self.y > 0 else None
        self.neighbors.append((self.x, self.y+1)) if self.y < n-1 else None
        self.neighbors.append((self.x+1, self.y-1)) if self.x < n-1 and self.y > 0 else None
        self.neighbors.append((self.x-1, self.y+1)) if self.x > 0 and self.y < n-1 else None
    
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
