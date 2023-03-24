from game.game import Game
from game.hex import Hex

if __name__ == '__main__':
    game = Game(board_size=5, agent_type='hybrid')
    game.playGame()
