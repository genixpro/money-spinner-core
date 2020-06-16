


class Tile:
    def __init__(self, tileType, x, y):
        self.tileType = tileType
        self.x = x
        self.y = y


    def json(self):
        return {
            "type": self.tileType.name,
            "x": self.x,
            "y": self.y
        }





