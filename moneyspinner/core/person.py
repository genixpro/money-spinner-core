import functools

@functools.total_ordering
class Person:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.nextActionTime = 0


    def decideNextAction(self):
        pass



    def __eq__(self, other):
        return self.nextActionTime == other.nextActionTime

    def __lt__(self, other):
        return self.nextActionTime < other.nextActionTime

