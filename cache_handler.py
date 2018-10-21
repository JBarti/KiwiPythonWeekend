from redis import StrictRedis
from journey import Journey
from slugify import slugify
import json


class CacheHandler(StrictRedis):
    def __init__(self):
        super().__init__(host="localhost", port="6379")

    def generate_key(self, departure, arival, departure_time):
        departure = slugify(departure, separator="-")
        arival = slugify(arival, separator="-")
        departure_time = slugify(departure_time)

        key = f"journeys:{departure}_{arival}_{departure_time}:BartiJ"
        return f"{key}"

    def store_key(self, key):
        keys = self.get_keys()
        if keys:
            keys.append(key)
            self.set("keys:JBarti", json.dumps(keys))
        else:
            self.set("keys:JBarti", json.dumps([key]))
        print(f"{key} stored")

    def get_keys(self):
        keys = self.get("keys:JBarti")
        if keys:
            return json.loads(keys)

    def add_journeys(self, departure, arival, departure_time, journeys):
        if not journeys:
            print("\nNo Data for given input\n")
            return
        key = self.generate_key(departure, arival, departure_time)
        self.store_key(key)

        journeys = list(map(lambda x: x.beautify(), journeys))

        self.set(key, json.dumps(journeys))
        print(f"\n{key} STORED IN REDIS \n")

    def get_journeys(self, departure, arival, departure_time):
        key = self.generate_key(departure, arival, departure_time)
        output = self.get(key)
        if output:
            return json.loads(output)

    def get_journeys_by_key(self, key):
        return [Journey(**data) for data in json.loads(self.get(key))]
