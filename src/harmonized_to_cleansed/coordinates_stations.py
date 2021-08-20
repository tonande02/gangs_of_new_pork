import geopy.distance
import json
from os import times
from pathlib import Path
import psycopg2
import time


############################################
# Connecting to the database   
DB_HOST = "gmpzlu2vtr1icu.cs0xobsxhp2r.eu-west-1.rds.amazonaws.com"
DB_USER = "GangsofNP"
PASSWORD = "Awesometeam2021"
PORT = 5432
DESTINATION_DB_NAME = "NYCbike"
############################################

DESTINATION_SCHEMA_NAME  = "cleansed"
TABLE_NAMES = ["weather_data", "weather_station", "bike_data", "bike_stations"]


def get_weather_stations(schema_name, table_station, table_data):
    query = f"""
    SELECT station_id, latitude, longitude FROM {schema_name}.{table_station}
    WHERE station_id IN
    (SELECT station_id FROM {schema_name}.{table_data}
    WHERE date >= '01-01-2021');"""

    return query

def get_bike_stations(schema_name, table_station):
    query = f"""
    SELECT station_id, latitude, longitude FROM {schema_name}.{table_station};"""

    return query







if __name__ == "__main__":
    with psycopg2.connect(
        host = DB_HOST,
        dbname = DESTINATION_DB_NAME,
        user = DB_USER,
        password = PASSWORD,
        port = PORT,
    ) as connection_destination_db:

        with connection_destination_db.cursor() as cursor:
            # query = get_weather_stations(DESTINATION_SCHEMA_NAME, "weather_station", "weather_data")
            # cursor.execute(query)
            # result = cursor.fetchall()
            # for line in result:
            #     print(line)
            # print(type(result[0]))
            # print(len(result))

            query = get_bike_stations(DESTINATION_SCHEMA_NAME, "bike_stations")
            cursor.execute(query)
            result = cursor.fetchall()
            print(result[0])
            print(type(result[0]))
            print(len(result))


        

        connection_destination_db.commit()