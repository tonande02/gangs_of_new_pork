ALTER TABLE cleansed.weather_data
ADD COLUMN temperature_maximum_celsius INTEGER;

UPDATE cleansed.weather_data 
SET temperature_maximum_celsius = (temperature_maximum_fahrenheit - 32) * 5 / 9;

ALTER TABLE cleansed.weather_data
ADD COLUMN temperature_average_celsius INTEGER;

UPDATE cleansed.weather_data 
SET temperature_average_celsius = (temperature_average_fahrenheit - 32) * 5 / 9;

ALTER TABLE cleansed.weather_data
ADD COLUMN temperature_minimum_celsius INTEGER;

UPDATE cleansed.weather_data 
SET temperature_minimum_celsius = (temperature_minimum_fahrenheit - 32) * 5 / 9;

---------------------------------
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
