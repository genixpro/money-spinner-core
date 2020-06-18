from .availableaction import AvailableAction
from .economic_object import EconomicObject

class BuildingObject(EconomicObject):
    def __init__(self, name, building):
        super(BuildingObject, self).__init__(name)

        self.building = building

        (x, y) = building.addBuildingObject(self)

        self.x = x
        self.y = y

        self.id = None





    def getAvailableActions(self, person):
        raise NotImplementedError()



    def json(self):
        data = super().json()

        data['id'] = self.id
        data['x'] = self.x
        data['y'] = self.y

        return data