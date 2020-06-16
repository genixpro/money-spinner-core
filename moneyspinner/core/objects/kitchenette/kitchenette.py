from moneyspinner.core.economic_object import EconomicObject
from .cook_meal import CookMeal
from .drink_water import DrinkWater

class Kitchenette(EconomicObject):
    def __init__(self, x, y):
        super(EconomicObject, self).__init__()

        self.x = x
        self.y = y

        self.cookMealAction = CookMeal(self)
        self.drinkWaterAction = DrinkWater(self)


    def getAvailableActions(self, person):
        return [
            self.cookMealAction,
            self.drinkWaterAction
        ]



