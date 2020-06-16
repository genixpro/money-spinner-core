from ..availableaction import AvailableAction


class EnterBuilding(AvailableAction):
    def __init__(self, building):
        super().__init__("enter_building")

        self.building = building



