from .availableaction import AvailableAction


class EconomicObject:
    def __init__(self, name):
        self.name = name





    def getAvailableActions(self, person):
        raise NotImplementedError()




    def json(self):
        return {
            "name": self.name
        }
