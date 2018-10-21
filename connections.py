from requests_html import HTMLSession
from journey import Journey
from cache_handler import CacheHandler
from website_parser import WebsiteParser
import fire

session = HTMLSession()

cache_handler = CacheHandler()


class Connections:

    session = HTMLSession()
    data = {
        "post-type": "shop",
        "currentstepnumber": "1",
        "search-from": "Split",
        "search-to": "Zagreb",
        "search-datetime": "21.10.2018.",
        "ticket-type": "oneway",
    }

    url = "https://www.arriva.com.hr/hr-hr/odabir-polaska"

    def cache(self, output):
        cache_handler.add_journeys(
            self.data["search-from"],
            self.data["search-to"],
            self.data["search-datetime"],
            output,
        )

    def check_cache(self):
        return cache_handler.get_journeys(
            self.data["search-from"],
            self.data["search-to"],
            self.data["search-datetime"],
        )

    def run_request(self):
        request = session.post(self.url, data=self.data)
        return request.html

    def parse_request(self):

        cached = self.check_cache()
        if cached:
            print("CHACHED")
            return cached

        html = self.run_request()
        data_parser = WebsiteParser(html)
        departure = data_parser.departure_time()
        arival = data_parser.arival_time()
        prices = data_parser.prices()
        traveling_time = data_parser.traveling_time()
        carrier = data_parser.carriers()

        output = [
            Journey(
                departure=departure[x],
                departure_date=self.data["search-datetime"],
                arival=arival[x],
                price=prices[x],
                traveling_time=traveling_time[x],
                carrier=carrier[x],
                departure_destination=self.data["search-from"],
                arival_destination=self.data["search-to"],
            )
            for x in range(len(departure))
        ]

        if output:
            self.cache(output)
        return [journey.beautify() for journey in output]

    def main(self, source, destination, departure_date):
        self.data["search-from"] = source
        self.data["search-to"] = destination
        self.data["search-datetime"] = departure_date
        return self.parse_request()


if __name__ == "__main__":
    fire.Fire(Connections)
