from ...availableaction import AvailableAction


class DrinkWater(AvailableAction):
    def __init__(self, kitchenette):
        super().__init__("drink_water")

        self.kitchenette = kitchenette



