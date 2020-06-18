from moneyspinner.core.building_object import BuildingObject
from .cook_meal import CookMeal
from .drink_water import DrinkWater

class Kitchenette(BuildingObject):
    def __init__(self, building):
        super().__init__("kitchenette", building)

        self.cookMealAction = CookMeal(self)
        self.drinkWaterAction = DrinkWater(self)


    def getAvailableActions(self, person):
        return [
            self.cookMealAction,
            self.drinkWaterAction
        ]


    def json(self):
        data = super(Kitchenette, self).json()

        return data

