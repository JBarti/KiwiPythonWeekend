create_table = """ 
    CREATE TABLE IF NOT EXISTS journeys_barti (
        id SERIAL PRIMARY KEY,
        departure TEXT,
        arival TEXT,
        departure_date TEXT,
        price INTEGER,
        traveling_time TEXT,
        carrier TEXT,
        departure_destination TEXT,
        arival_destination TEXT
    ) """

drop_table = """
    DROP TABLE journeys_barti
"""

add_journey = """
    INSERT INTO journeys_barti (departure, 
    arival,
    departure_date,
    price,
    traveling_time,
    carrier,
    departure_destination,
    arival_destination
    )
    VALUES(
        %(departure)s,
        %(arival)s,
        %(departure_date)s,
        %(price)s,
        %(traveling_time)s,
        %(carrier)s,
        %(departure_destination)s,
        %(arival_destination)s)
"""

get_journey = """SELECT * FROM journeys_barti"""

querries = {
    "departure_destination": """departure_destination = %(departure_destination)s""",
    "arival_destination": """arival_destination = %(arival_destination)s""",
    "price": """price <= %(price)s""",
    "carrier": """carrier = %(carrier)s""",
}
