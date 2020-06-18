from .economic_object import EconomicObject
from .actions.enter_building import EnterBuilding
from .actions.exit_building import ExitBuilding
import random

class Building(EconomicObject):
    def __init__(self, x, y, width, height, floors):
        super(EconomicObject, self).__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.floors = floors

        self.property = None

        self.buildingObjects = []

        self.enterAction = EnterBuilding(self)
        self.exitAction = ExitBuilding(self)


    def getAvailableActions(self, person):
        if person.currentBuilding == self:
            return [
                self.exitAction
            ]
        elif person.currentBuilding is None:
            return [
                self.enterAction
            ]
        else:
            return []


    def addBuildingObject(self, buildingObject):
        possibleSpots = set()
        for x in range(self.x + 1, self.x + self.width - 2):
            possibleSpots.add((x, self.y + 1))
            possibleSpots.add((x, self.y + self.height - 1))

        for y in range(self.y, self.y + self.width - 2):
            possibleSpots.add((self.x + 1, y))
            possibleSpots.add((self.x + self.width - 1, y))

        for object in self.buildingObjects:
            if (object.x, object.y) in possibleSpots:
                possibleSpots.remove((object.x, object.y))

        chosenSpot = random.choice(list(possibleSpots))

        buildingObject.x = chosenSpot[0]
        buildingObject.y = chosenSpot[1]

        self.buildingObjects.append(buildingObject)

        return chosenSpot
