ALTER TABLE cleansed.bike_stations
ADD CONSTRAINT constraint_unique
UNIQUE (station_id);

ALTER TABLE cleansed.bike_data
ADD CONSTRAINT constraint_fk
FOREIGN KEY(start_station_id)
REFERENCES cleansed.bike_stations (station_id);

ALTER TABLE cleansed.bike_data
ADD CONSTRAINT constraint_fk_end
FOREIGN KEY(end_station_id)
REFERENCES cleansed.bike_stations (station_id);

ALTER TABLE cleansed.weather_station
ADD CONSTRAINT constraint_unique_weather
UNIQUE (station_id);

ALTER TABLE cleansed.weather_data
ADD CONSTRAINT constraint_fk_weather
FOREIGN KEY(station_id)
REFERENCES cleansed.weather_station (station_id);
