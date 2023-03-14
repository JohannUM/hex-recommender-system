from disjoint_set import DisjointSet

class HexGame:
    def __init__(self, n=11):
        self.n = n
        self.board = [[0]*n for _ in range(n)]
        self.cells = [(i, j) for i in range(n) for j in range(n)]
        self.top_node = (-1, 0)
        self.bottom_node = (n, 0)
        self.left_node = (0, -1)
        self.right_node = (0, n)
        self.ds_red = DisjointSet(self.cells + [self.top_node, self.bottom_node])
        self.ds_blue = DisjointSet(self.cells + [self.left_node, self.right_node])
        for i in range(n):
            self.ds_red.union((0, i), self.top_node)
            self.ds_red.union((n-1, i), self.bottom_node)
            self.ds_blue.union((i, 0), self.left_node)
            self.ds_blue.union((i, n-1), self.right_node)

    def play(self, i, j, player):
        assert 0 <= i < self.n and 0 <= i < self.n and self.board[i][j] == 0
        code = 1 if player == 'red' else 2
        self.board[i][j] = code
        for nei_i, nei_j in [(i+1, j), (i+1, j-1), (i, j+1), (i, j-1), (i-1, j), (i-1, j+1)]:
            if 0 <= nei_i < self.n and 0 <= nei_j < self.n and code == self.board[nei_i][nei_j]:
                if player == 'red':
                    self.ds_red.union((nei_i, nei_j), (i, j))
                else:
                    self.ds_blue.union((nei_i, nei_j), (i, j))
        print(*self.board, sep='\n')
        if self.ds_red.find(self.top_node) == self.ds_red.find(self.bottom_node):
            print('red won')
        elif self.ds_blue.find(self.left_node) == self.ds_blue.find(self.right_node):
            print('blue won')


game = HexGame(3)
player = 'red'
while True:
    # Get player input as two integers i and j separated by a space (e.g.: 3 1)
    i, j = tuple(map(int, input(f'{player} turn: ').split(' ')))
    game.play(i, j, player)
    player = 'red' if player == 'blue' else 'blue'