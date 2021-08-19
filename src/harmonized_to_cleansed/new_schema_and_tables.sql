CREATE SCHEMA IF NOT EXISTS cleansed;

CREATE TABLE cleansed.bike_data (LIKE staged.bike_data INCLUDING ALL);

INSERT INTO cleansed.bike_data SELECT * FROM staged.bike_data;

CREATE TABLE cleansed.bike_stations (LIKE staged.bike_stations INCLUDING ALL);

INSERT INTO cleansed.bike_stations SELECT * FROM staged.bike_stations;

CREATE TABLE cleansed.weather_data (LIKE staged.weather_data INCLUDING ALL);

INSERT INTO cleansed.weather_data SELECT * FROM staged.weather_data;

CREATE TABLE cleansed.weather_station (LIKE staged.weather_station INCLUDING ALL);

INSERT INTO cleansed.weather_station SELECT * FROM staged.weather_station;