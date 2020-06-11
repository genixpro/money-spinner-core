from .map import Map
from .person import Person
import heapq
import random


class Engine:
    def __init__(self):
        self.map = Map()
        self.heapQueue = []

        for n in range(100):
            person = Person(random.randint(0, 99), random.randint(0, 99))
            heapq.heappush(self.heapQueue, person)

    def runMainLoop(self):
        while True:
            # Get the next person who has to decide upon an action
            person = heapq.heappop(self.heapQueue)
            action = person.decideNextAction()
            actionFinishTime = action.execute()
            person.nextActionTime = actionFinishTime
            heapq.heappush(self.heapQueue, person)



