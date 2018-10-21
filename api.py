import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from cache_handler import CacheHandler
from slugify import slugify
from db_controller import DbController

app = Flask(__name__)
db = CacheHandler()
app.config["DEBUG"] = True
CORS(app)


@app.route("/test")
def test():
    return "test"


@app.route("/search")
def get_data():
    keys = db.get_keys()
    source = slugify(request.args.get("source", ""), separator="-")
    destination = slugify(request.args.get("destination", ""), separator="-")
    price = int(request.args.get("price", "9999999999999"))

    if source:
        keys = filter(lambda key: key.find(source) == 9, keys)

    if destination:
        keys = filter(lambda key: key.find(destination) > 9, keys)

    journeys = [
        journey for journey in [db.get_journeys_by_key(key) for key in list(keys)]
    ][0]

    if price:
        journeys = filter(lambda journey: journey.get_price() <= price, journeys)

    return json.dumps([journey.beautify() for journey in list(journeys)])


@app.route("/search/db")
def search():
    controller = DbController()
    arguments = dict(request.args)
    arguments = dict([(key, arguments[key][0]) for key in arguments])
    querry_result = controller.get_journey(**arguments)
    return jsonify(querry_result)


if __name__ == "__main__":
    app.run(port=5001)
