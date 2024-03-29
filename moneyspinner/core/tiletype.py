import json
import pkg_resources


class TileType:
    def __init__(self, name):
        configDataStream = pkg_resources.resource_stream("moneyspinner", f"tiles/{name}.json")
        data = json.load(configDataStream)

        self.name = data['name']
        self.speed = data['speed']



