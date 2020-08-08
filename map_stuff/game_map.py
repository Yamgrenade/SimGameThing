from map_stuff.tile import Tile


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        # Generate array of tiles, all are unblocked for now
        tiles = [[Tile(y == 0 or y == self.height - 1 or x == 0 or x == self.width - 1) for y in range(self.height)] for x in range(self.width)]

        # Make a wall so we don't fall out of range

        return tiles

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False
