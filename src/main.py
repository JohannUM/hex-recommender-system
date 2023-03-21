from game.game import Game    

if __name__ == '__main__':
    print('Play Hex!')
    #while True:
    board_size = int(input('What size board? (n): '))
    if board_size < 3 or board_size > 17:
        game = Game()
    else:
        game = Game(board_size)
    game.playGame()

        # again = input('Play again? (y/n): ')
        # if again == 'y':
        #     continue

        # break