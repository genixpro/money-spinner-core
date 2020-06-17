from .tiletype import TileType
from .tile import Tile



class Map:
    def __init__(self):
        self.width = 50
        self.height = 50

        self.loadTileTypes()

        self.grid = [
            [Tile(self.tileTypes['grass'], x, y) for y in range(self.height)] for x in range(self.width)
        ]


    def loadTileTypes(self):
        self.tileTypes = {
            "grass": TileType("grass"),
            "water": TileType("water")
        }


