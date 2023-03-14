import numpy as np

from game.board import Board

class Hex:
    def __init__(self, gridsize:int=11): # default size is 11
        self.gridsize = gridsize
        self.board = Board(self.gridsize)
        print('(When entering a location do so like this: row col e.g. 4 1 or 0 0, space between)')
        self.board.display_board()
    
    def game_loop(self):
        player = 1
        while True:
            row, col = tuple(map(int, input(f'\n{player} turn: ').split(' ')))

            if not self.board.contains_location((row, col)):
                print('Not a valid location on the board.')
                continue

            if not self.board.check_position_state((row, col)) == 0:
                print('This location is already occupied.')
                continue

            # Move
            self.board.update_position_state((row, col), player)
            self.board.display_board()

            winner = self.board.check_winner()
            if winner == 1:
                print('Player 1 has won!')
                break
            elif winner == 2:
                print('Player 2 has won!')
                break

            player = 3 - player
        
        print('Game Over')
