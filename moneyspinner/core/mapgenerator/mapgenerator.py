import random


class MapGenerator:
    def __init__(self):
        pass


    def generateMap(self, map):
        for n in range(5):
            self.addLake(map)

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
