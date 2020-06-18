


class Tile:
    def __init__(self, tileType, x, y):
        self.tileType = tileType
        self.x = x
        self.y = y

        self.building = None
        self.property = None

        self.distanceFromObstacle = None
        self.processed = False

    def json(self):
        return {
            "type": self.tileType.name,
            "x": self.x,
            "y": self.y
        }

    def isObstacle(self):
        if self.tileType.speed == 0:
            return True

        if self.building is not None:
            return True

        return False



