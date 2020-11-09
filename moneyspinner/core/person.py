import functools
import random

@functools.total_ordering
class Person:

    def __init__(self, engine, x, y, id):
        self.engine = engine
        self.x = x
        self.y = y
        self.id = id
        self.currentBuilding = None

        self.nextActionTime = 0


    def getAvailableActions(self):
        actions = []
        if self.currentBuilding is not None:
            actions.extend(self.currentBuilding.getAvailableActions(self))
        else:
            for building in self.engine.map.buildings:
                actions.append(building.enterAction)

        return actions


    def decideNextAction(self):
        available = self.getAvailableActions()
        return random.choice(available)


    def __eq__(self, other):
        return self.nextActionTime == other.nextActionTime


    def __lt__(self, other):
        return self.nextActionTime < other.nextActionTime


    def json(self):
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "movements": [],
            "nextActions": []
        }
