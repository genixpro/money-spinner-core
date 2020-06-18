import random
from ..property import Property

class MapGenerator:
    def __init__(self):
        self.propertySize = 10

        self.propertySpacing = 3


    def generateMap(self, map):
        for n in range(5):
            self.addLake(map)

        map.recomputeObstacleDistanceGradient()

        self.divideIntoProperties(map)

    def addLake(self, map):
        expansionTiles = []

        lakeStart = map.grid[random.randint(0, map.width - 1)][random.randint(0, map.height - 1)]

        lakeStart.tileType = map.tileTypes['water']

        expansionTiles.append(lakeStart)

        lakeTiles = 50
        while lakeTiles > 0:
            tile = random.choice(expansionTiles)

            possibleExpansions = []

            for relX in [-1, 0, 1]:
                for relY in [-1, 0, 1]:
                    if relX == 0 and relY == 0:
                        continue

                    newX = tile.x + relX
                    newY = tile.y + relY

                    if newX >= 0 and newY >= 0 and newX < map.width and newY < map.height:
                        expandTile = map.grid[newX][newY]
                        if expandTile.tileType.name != 'water':
                            possibleExpansions.append(expandTile)

            if len(possibleExpansions) == 0:
                expansionTiles.remove(tile)
            else:
                chosen = random.choice(possibleExpansions)

                chosen.tileType = map.tileTypes['water']

                expansionTiles.append(chosen)

                lakeTiles -= 1

    def divideIntoProperties(self, map):
        propertyX = 0
        while propertyX < map.width:
            propertyY = 0
            while propertyY < map.height:
                left = propertyX
                right = propertyX + self.propertySize
                top = propertyY
                bottom = propertyY + self.propertySize

                if right < map.width and bottom < map.height:
                    closestObstacle = None
                    for x in range(left, right):
                        for y in range(top, bottom):
                            tileDist = map.tileAt(x, y).distanceFromObstacle
                            if closestObstacle is None or tileDist < closestObstacle:
                                closestObstacle = tileDist
                    if closestObstacle is not None and closestObstacle > 1:
                        property = Property(propertyX, propertyY, self.propertySize, self.propertySize, None)
                        map.addProperty(property)


                        for y in range(top - int(self.propertySpacing / 2) - 1, bottom + int(self.propertySpacing / 2) + 1):
                            if y >= 0 and y < map.height:
                                if (right + int(self.propertySpacing / 2)) < map.width:
                                    map.tileAt(right + int(self.propertySpacing / 2), y).tileType = map.tileTypes['dirt_road']
                                if left - int(self.propertySpacing / 2) - 1 >= 0:
                                    map.tileAt(left - int(self.propertySpacing / 2) - 1, y).tileType = map.tileTypes['dirt_road']

                        for x in range(left - int(self.propertySpacing / 2) - 1, right + int(self.propertySpacing / 2) + 1):
                            if x >= 0 and x < map.width:
                                if bottom + int(self.propertySpacing / 2) < map.height:
                                    map.tileAt(x, bottom + int(self.propertySpacing / 2)).tileType = map.tileTypes['dirt_road']
                                if top - int(self.propertySpacing / 2) - 1 >= 0:
                                    map.tileAt(x, top - int(self.propertySpacing / 2) - 1).tileType = map.tileTypes['dirt_road']


                propertyY += self.propertySize + self.propertySpacing
            propertyX += self.propertySize + self.propertySpacing


    def addBuilding(self, map):
        pass
