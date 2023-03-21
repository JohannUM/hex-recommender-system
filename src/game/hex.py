from game.board import Board

from game import minimax

class Hex:
    def __init__(self, gridsize:int=11): # default size is 11
        self.gridsize = gridsize
        self.board = Board(self.gridsize)
        print('(When entering a location do so like this: row col e.g. 4 1 or 0 0, space between)')
        self.board.display_board()


    def make_move(self, player, human=True):
        if human:
            print('\Human turn...')
            row, col = tuple(map(int, input(f'\n{player} turn: ').split(' ')))
            if not self.board.contains_location((row, col)):
                print('Not a valid location on the board.')

            if not self.board.check_position_state((row, col)) == 0:
                print('This location is already occupied.')
            print(f'Human moves: {row} {col}')
        else:
            print('\nComputer turn...')     
            best_move = minimax.get_move(board=self.board, player=player)
            row, col = best_move[0], best_move[1]
            print(f'Computer moves: {row} {col}')

        self.board.update_position_state((row, col), player)

    
    def game_loop(self):
        player = 1
        while True:

            self.make_move(player=player, human=False if player==1 else True)
            self.board.display_board()

            winner = self.board.check_winner()
            if winner == 1:
                print('Player 1 has won!')
                break
            elif winner == 2:
                print('Player 2 has won!')
                break
            
            # Switch turn
            player = 3 - player
        
        print('Game Over')