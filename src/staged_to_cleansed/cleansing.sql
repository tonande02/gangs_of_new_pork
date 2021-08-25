--creates cleansed schema, copies each table from staged schema
CREATE SCHEMA IF NOT EXISTS cleansed;

CREATE TABLE cleansed.bike_data (LIKE staged.bike_data INCLUDING ALL);

INSERT INTO cleansed.bike_data SELECT * FROM staged.bike_data;

CREATE TABLE cleansed.bike_station (LIKE staged.bike_station INCLUDING ALL);

INSERT INTO cleansed.bike_station SELECT * FROM staged.bike_station;

CREATE TABLE cleansed.weather_data (LIKE staged.weather_data INCLUDING ALL);

INSERT INTO cleansed.weather_data SELECT * FROM staged.weather_data;

CREATE TABLE cleansed.weather_station (LIKE staged.weather_station INCLUDING ALL);

INSERT INTO cleansed.weather_station SELECT * FROM staged.weather_station;

--renaming columns

AlTER TABLE cleansed.weather_data
RENAME COLUMN tavg TO temperature_average_fahrenheit;

AlTER TABLE cleansed.weather_data
RENAME COLUMN tmax TO temperature_maximum_fahrenheit;

AlTER TABLE cleansed.weather_data
RENAME COLUMN tmin TO temperature_minimum_fahrenheit;

AlTER TABLE cleansed.weather_data
RENAME COLUMN prcp TO precipitation_inches;

AlTER TABLE cleansed.weather_data
RENAME COLUMN snow TO snow_fall_inches;

AlTER TABLE cleansed.weather_data
RENAME COLUMN snwd TO snow_depth_inches;

AlTER TABLE cleansed.bike_station
RENAME COLUMN start_lat TO latitude;

AlTER TABLE cleansed.bike_station
RENAME COLUMN start_lng TO longitude;

AlTER TABLE cleansed.bike_station
RENAME COLUMN start_station_id TO station_id;

AlTER TABLE cleansed.bike_station
RENAME COLUMN start_station_name TO station_name;

AlTER TABLE cleansed.bike_data
RENAME COLUMN rideable_type TO bike_type;

AlTER TABLE cleansed.bike_data
RENAME COLUMN member_casual TO customer_category;

AlTER TABLE cleansed.weather_station
RENAME COLUMN stations_id TO station_id;

ALTER TABLE cleansed.weather_station
RENAME COLUMN audit_inserted_to_staged_at TO audit_inserted_to_cleansed_at;

ALTER TABLE cleansed.weather_data
RENAME COLUMN audit_inserted_to_staged_at TO audit_inserted_to_cleansed_at;

ALTER TABLE cleansed.bike_station
RENAME COLUMN audit_inserted_to_staged_at TO audit_inserted_to_cleansed_at;

ALTER TABLE cleansed.bike_data
RENAME COLUMN audit_inserted_to_staged_at TO audit_inserted_to_cleansed_at;

-- changing data types

ALTER TABLE cleansed.bike_data
ALTER COLUMN started_at TYPE timestamp without time zone USING started_at::timestamp without time zone;

ALTER TABLE cleansed.bike_data
ALTER COLUMN ended_at TYPE timestamp without time zone USING ended_at::timestamp without time zone;

ALTER TABLE cleansed.bike_station
ALTER COLUMN latitude TYPE numeric USING latitude::numeric,
ALTER COLUMN longitude TYPE numeric USING longitude::numeric;

ALTER TABLE cleansed.weather_data
ALTER COLUMN date TYPE timestamp without time zone USING date::timestamp without time zone;

ALTER TABLE cleansed.weather_data
ALTER COLUMN temperature_average_fahrenheit TYPE int USING temperature_average_fahrenheit::int,
ALTER COLUMN temperature_maximum_fahrenheit TYPE int USING temperature_maximum_fahrenheit::int,
ALTER COLUMN temperature_minimum_fahrenheit TYPE int USING temperature_minimum_fahrenheit::int,
ALTER COLUMN precipitation_inches TYPE numeric USING precipitation_inches::numeric,
ALTER COLUMN snow_fall_inches TYPE numeric USING snow_fall_inches::numeric,
ALTER COLUMN snow_depth_inches TYPE numeric USING snow_depth_inches::numeric;

ALTER TABLE cleansed.weather_station
ALTER COLUMN latitude TYPE numeric USING latitude::numeric,
ALTER COLUMN longitude TYPE numeric USING longitude::numeric;

-- metric conversion

ALTER TABLE cleansed.weather_data
ADD COLUMN temperature_maximum_celsius NUMERIC;

UPDATE cleansed.weather_data 
SET temperature_maximum_celsius = (temperature_maximum_fahrenheit - 32) * 5 / 9;

ALTER TABLE cleansed.weather_data
ADD COLUMN temperature_average_celsius NUMERIC;

UPDATE cleansed.weather_data 
SET temperature_average_celsius = (temperature_average_fahrenheit - 32) * 5 / 9;

ALTER TABLE cleansed.weather_data
ADD COLUMN temperature_minimum_celsius NUMERIC;

UPDATE cleansed.weather_data 
SET temperature_minimum_celsius = (temperature_minimum_fahrenheit - 32) * 5 / 9;

ALTER TABLE cleansed.weather_data
ADD COLUMN snow_fall_centimeters NUMERIC;

UPDATE cleansed.weather_data 
SET snow_fall_centimeters = snow_fall_inches * 2.54;

ALTER TABLE cleansed.weather_data
ADD COLUMN snow_depth_centimeters NUMERIC;

UPDATE cleansed.weather_data 
SET snow_depth_centimeters = snow_depth_inches * 2.54;

ALTER TABLE cleansed.weather_data
ADD COLUMN precipitation_centimeters NUMERIC;

UPDATE cleansed.weather_data 
SET precipitation_centimeters = precipitation_inches * 2.54;

-- adding fk and unique constraints

ALTER TABLE cleansed.bike_station
ADD CONSTRAINT constraint_unique
UNIQUE (station_id);

ALTER TABLE cleansed.bike_data
ADD CONSTRAINT constraint_fk
FOREIGN KEY(start_station_id)
REFERENCES cleansed.bike_station (station_id);

ALTER TABLE cleansed.bike_data
ADD CONSTRAINT constraint_fk_end
FOREIGN KEY(end_station_id)
REFERENCES cleansed.bike_station (station_id);

ALTER TABLE cleansed.weather_station
ADD CONSTRAINT constraint_unique_weather
UNIQUE (station_id);

ALTER TABLE cleansed.weather_data
ADD CONSTRAINT constraint_fk_weather
FOREIGN KEY(station_id)
REFERENCES cleansed.weather_station (station_id);
