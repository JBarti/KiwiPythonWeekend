from currency_converter import CurrencyConverter


class WebsiteParser:
    def __init__(self, html):
        self.html = html
        self.currencyConverter = CurrencyConverter()

    def arival_departure_time(self):
        return map(lambda x: x.text, self.html.find(".vrijeme-top"))

    def departure_time(self):
        return list(
            map(lambda x: x.split("k")[2].split(" ")[0], self.arival_departure_time())
        )

    def arival_time(self):
        return list(
            map(lambda x: x.split("k")[2].split(" ")[0], self.arival_departure_time())
        )

    def prices(self):
        prices = map(lambda x: x.text.split(" ")[0], self.html.find(".cijena"))
        prices = filter(lambda x: (not not x), prices)
        prices = map(
            lambda x: str(
                int(self.currencyConverter.convert(int(x.split(",")[0]), "HRK", "EUR"))
            )
            + " EUR",
            prices,
        )
        return list(prices)

    def traveling_time(self):
        return list(
            map(lambda x: x.text.split(" ")[2], self.html.find(".vrijeme-bottom"))
        )

    def carriers(self):
        return list(map(lambda x: x.text, self.html.find(".prijevoznik")))
