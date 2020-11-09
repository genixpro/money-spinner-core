from ..availableaction import AvailableAction
import random

class EnterBuilding(AvailableAction):
    def __init__(self, building):
        super().__init__("enter_building")

        self.building = building



    def execute(self, person):
        person.currentBuilding = self.building

        person.x = self.building.x + random.randint(1, self.building.width - 2)
        person.y = self.building.y + random.randint(1, self.building.height - 2)

        return 1
