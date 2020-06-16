from .economic_object import EconomicObject
from .actions.enter_building import EnterBuilding
from .actions.exit_building import ExitBuilding


class Building(EconomicObject):
    def __init__(self, x, y, width, height, floors):
        super(EconomicObject, self).__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.floors = floors

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




