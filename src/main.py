from game.hex import Hex    

if __name__ == '__main__':
    print('Play Hex!')
    while True:
        board_size = int(input('What size board? (n): '))
        if board_size < 3 or board_size > 25:
            game = Hex()
        else:
            game = Hex(board_size)
        game.game_loop()

        again = input('Play again? (y/n): ')
        if again == 'y':
            continue

        break