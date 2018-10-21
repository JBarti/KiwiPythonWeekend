import psycopg2
from psycopg2.extras import RealDictCursor
from sql_querries import create_table, drop_table, add_journey, get_journey, querries
from journey import Journey


class DbController:
    def __init__(self):
        with self.connection() as con:
            with self.cursor(con) as cursor:
                cursor.execute(create_table)

    def connection(self):
        pg_config = {
            "host": "pythonweekend.cikhbyfn2gm8.eu-west-1.rds.amazonaws.com",
            "database": "pythonweekend",
            "user": "shareduser",
            "password": "NeverEverSharePasswordsInProductionEnvironement",
        }
        return psycopg2.connect(**pg_config)

    def cursor(self, connection):
        return connection.cursor(cursor_factory=RealDictCursor)

    def add_journey(self, journey):
        journey_data = journey.beautify()
        journey_data["price"] = int(journey_data["price"])
        with self.connection() as con:
            with self.cursor(con) as cursor:
                cursor.execute(add_journey, journey_data)

    def get_journey(self, **kwargs):
        with self.connection() as con:
            with self.cursor(con) as cursor:
                querry = get_journey
                if kwargs:
                    querry += " WHERE "
                for key in kwargs:
                    querry += querries[key]
                    querry += " AND "
                if kwargs:
                    cursor.execute(querry[0 : len(querry) - 5], kwargs)
                else:
                    cursor.execute(querry, kwargs)
                return cursor.fetchall()


if __name__ == "__main__":
    db_controller = DbController()

    journey = Journey(
        **{
            "departure": "8:00",
            "departure_date": "22-10-2018",
            "arival": "21:00",
            "price": "1090",
            "traveling_time": "07:10",
            "carrier": "kiwi",
            "departure_destination": "Split",
            "arival_destination": "Zagreb",
        }
    )
    print(journey.beautify())

    print(
        db_controller.get_journey(
            departure_destination="Split", arival_destination="Zagreb"
        )
    )
