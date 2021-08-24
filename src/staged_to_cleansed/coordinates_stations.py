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
TABLE_NAMES = ["weather_data", "weather_station", "bike_data", "bike_station"]

# gather the weather station id and coordinates from our tables
def get_weather_stations(schema_name, table_station, table_data):
    query = f"""
    SELECT station_id, latitude::float, longitude::float FROM {schema_name}.{table_station}
    WHERE station_id IN
    (SELECT station_id FROM {schema_name}.{table_data}
    WHERE date >= '01-06-2021');"""

    return query

# gather the bike station id and coordinates from our tables
def get_bike_stations(schema_name, table_station):
    query = f"""
    SELECT station_id, latitude::float, longitude::float FROM {schema_name}.{table_station};"""

    return query

# goes through the different bike stations, and finds the nearest weather station
def get_station_proximity(list_bike_stations, list_weather_stations):
    closest_stations = []

    for station in list_bike_stations:
        b_coords = (station[1], station[2])

        closest_distance = 500000
        closest_station = ""

        for w_station in list_weather_stations:
            w_coords = (w_station[1], w_station[2])
            distance = geopy.distance.distance(b_coords, w_coords).km
            if distance < closest_distance:
                closest_distance = distance
                closest_station = w_station[0]

        stations_list = [station[0], closest_station]
        stations_tuple = tuple(stations_list)
        closest_stations.append(stations_tuple)
    
    return closest_stations

# adds a query for creating a new columns with the nearest weather station
def add_column_query(schema_name, table_name, column_name):
    query = f"""ALTER TABLE {schema_name}.{table_name}
    ADD {column_name} TEXT;"""

    return query

# adds the nearest weather station to the new column in bike station
def populate_column_query(schema_name, table_name, stations_list):
    query = f"""
    UPDATE {schema_name}.{table_name} SET nearest_weather_station = '{stations_list[1]}' WHERE station_id = '{stations_list[0]}';"""
    return query

# adds a foreign key to the nearest weather station in bike station 
def foreign_key_set_up(schema_name, table_name_bike, table_name_weather, column_name_1, column_name_2):
    query = f"""
    ALTER TABLE {schema_name}.{table_name_bike} 
    ADD CONSTRAINT constraint_fk_station
    FOREIGN KEY({column_name_1})
    REFERENCES {schema_name}.{table_name_weather} ({column_name_2});"""
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
            query = get_weather_stations(DESTINATION_SCHEMA_NAME, TABLE_NAMES[1], TABLE_NAMES[0])
            cursor.execute(query)
            w_result = cursor.fetchall()
            
            query = get_bike_stations(DESTINATION_SCHEMA_NAME, TABLE_NAMES[3])
            cursor.execute(query)
            b_result = cursor.fetchall()

            closest_stations = get_station_proximity(b_result, w_result)
            new_column = "nearest_weather_station"
            query = add_column_query(DESTINATION_SCHEMA_NAME, TABLE_NAMES[3], new_column)
            cursor.execute(query)
            for station in closest_stations:
                query = populate_column_query(DESTINATION_SCHEMA_NAME, TABLE_NAMES[3], station)
                cursor.execute(query)
                
            query = foreign_key_set_up(DESTINATION_SCHEMA_NAME, TABLE_NAMES[3], TABLE_NAMES[1], new_column, 'station_id')
            cursor.execute(query)

        connection_destination_db.commit()