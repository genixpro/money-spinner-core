from .map import Map
from .person import Person
import heapq
import random
import json
from flask import Flask
from flask_cors import CORS
import threading
import datetime
from .mapgenerator.mapgenerator import MapGenerator

class Engine:
    def __init__(self):
        mapGenerator = MapGenerator()

        self.map = Map()

        mapGenerator.generateMap(self.map)

        self.heapQueue = []
        self.people = []

        for n in range(50):
            person = Person(self, random.randint(0, self.map.width - 1), random.randint(0, self.map.height - 1), n)
            heapq.heappush(self.heapQueue, person)
            self.people.append(person)

        self.app = Flask("moneyspinner")
        CORS(self.app)

        self.mainLoopRunning = False

        @self.app.route('/')
        def home():
            return self.homeEndpoint()

        @self.app.route('/grid')
        def grid():
            return self.gridEndpoint()

        @self.app.route('/people')
        def people():
            return self.peopleEndpoint()

        @self.app.route('/building_objects')
        def buildingObjects():
            return self.buildingObjectsEndpoint()

    def runMainLoop(self):
        if not self.mainLoopRunning:
            self.mainLoopRunning = True
            print("running main loop")
            start = datetime.datetime.now()
            count = 0
            while True:
                # Get the next person who has to decide upon an action
                person = heapq.heappop(self.heapQueue)
                action = person.decideNextAction()
                actionFinishTime = action.execute(person)
                person.nextActionTime = actionFinishTime
                heapq.heappush(self.heapQueue, person)
                count += 1
                seconds = (datetime.datetime.now() - start).total_seconds()
                if seconds > 10:
                    print(count / seconds)
                    start = datetime.datetime.now()
                    count = 0


    def runAPIServer(self):
        self.app.run(debug=True, port=42424, host='0.0.0.0')


    def homeEndpoint(self):
        return json.dumps({})


    def gridEndpoint(self):
        return json.dumps({"cells": [
            cell.json() for cellRow in self.map.grid for cell in cellRow
        ]})


    def peopleEndpoint(self):
        return json.dumps({"people": [person.json() for person in self.people]})


    def buildingObjectsEndpoint(self):
        return json.dumps({"buildingObjects": [object.json() for object in self.map.buildingObjects]})

