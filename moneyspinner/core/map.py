from .tiletype import TileType




class Map:
    def __init__(self):
        width = 100
        height = 100

        self.grid = [
            [self.tileTypes['grass'] for n in range(height)] for n in range(width)
        ]


    def loadTileTypes(self):
        self.tileTypes = {
            "grass": TileType("grass"),
            "water": TileType("water")
        }


