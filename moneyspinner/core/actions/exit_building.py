from ..availableaction import AvailableAction


class ExitBuilding(AvailableAction):
    def __init__(self, building):
        super().__init__("exit_building")

        self.building = building


