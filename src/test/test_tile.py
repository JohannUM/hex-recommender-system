from game.tile import Tile

def test_tile_top_left():
    tile = Tile((0,0), 5)
    assert tile.get_location() == (0,0)
    assert tile.get_state == 0
    assert tile.is_edge_tile
    assert tile.neighbors == [(1,0), (0,1)]