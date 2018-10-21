from dataclasses import dataclass


@dataclass
class Journey:
    departure: str
    departure_date: str
    arival: str
    price: str
    traveling_time: str
    carrier: str
    departure_destination: str
    arival_destination: str

    def beautify(self):
        return {
            "departure": self.departure,
            "departure_date": self.departure_date,
            "arival": self.arival,
            "price": self.price,
            "traveling_time": self.traveling_time,
            "carrier": self.carrier,
            "departure_destination": self.departure_destination,
            "arival_destination": self.arival_destination,
        }

    def get_price(self):
        return int(self.price.split(" ")[0])
