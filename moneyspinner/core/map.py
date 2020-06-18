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

        self.properties = []

    def allTiles(self):
        for row in self.grid:
            for tile in row:
                yield tile


    def tileAt(self, x, y):
        return self.grid[x][y]


    def neighborsOfTile(self, tile):
        neighbors = []
        for relX in [-1, 0, 1]:
            for relY in [-1, 0, 1]:
                if relX == 0 and relY == 0:
                    continue

                newTileX = tile.x + relX
                newTileY = tile.y + relY

                if newTileX >= 0 and newTileX < self.width:
                    if newTileY >= 0 and newTileY < self.height:
                        neighbors.append(self.tileAt(newTileX, newTileY))
        return neighbors



    def loadTileTypes(self):
        self.tileTypes = {
            "grass": TileType("grass"),
            "water": TileType("water"),
            "dirt_road": TileType("dirt_road"),
        }



    def recomputeObstacleDistanceGradient(self):
        tileQueue = []

        for tile in self.allTiles():
            if tile.isObstacle():
                tileQueue.append(tile)
                tile.distanceFromObstacle = 0
                tile.processed = True
            else:
                tile.processed = False

        while len(tileQueue) > 0:
            tile = tileQueue.pop(0)
            for neighborTile in self.neighborsOfTile(tile):
                if not neighborTile.processed:
                    neighborTile.distanceFromObstacle = tile.distanceFromObstacle + 1
                    neighborTile.processed = True
                    tileQueue.append(neighborTile)

    def addProperty(self, property):
        self.properties.append(property)

        for x in range(property.x, property.x + property.width):
            for y in range(property.y, property.y + property.height):
                self.tileAt(x, y).property = property
