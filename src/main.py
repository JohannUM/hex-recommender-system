from game.hex import Hex

def main():
    h = Hex(5)
    board = h.get_board()
    # Just checking all methods working so far
    for y in board:
        for x in y:
            print(f"Tile at location: {x.get_location()}")
            print(f"State: {x.get_state()}")
            print(f"Edge_tile: {x.is_edge_tile()}")
            print(f"Neighbors: {[neighbor.get_location() for neighbor in x.get_neighbors()]}")
            print()
    

if __name__ == '__main__':
    main()