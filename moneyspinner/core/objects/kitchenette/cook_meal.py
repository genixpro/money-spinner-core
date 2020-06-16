from ...availableaction import AvailableAction


class CookMeal(AvailableAction):
    def __init__(self, kitchenette):
        super().__init__("cook_meal")

        self.kitchenette = kitchenette



