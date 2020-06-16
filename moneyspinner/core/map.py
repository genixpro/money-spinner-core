from .tiletype import TileType
from .tile import Tile



class Map:
    def __init__(self):
        width = 100
        height = 100

        self.loadTileTypes()

        self.grid = [
            [Tile(self.tileTypes['grass'], x, y) for y in range(height)] for x in range(width)
        ]


    def loadTileTypes(self):
        self.tileTypes = {
            "grass": TileType("grass"),
            "water": TileType("water")
        }


