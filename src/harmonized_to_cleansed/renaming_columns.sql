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

AlTER TABLE cleansed.bike_stations
RENAME COLUMN start_lat TO latitude;

AlTER TABLE cleansed.bike_stations
RENAME COLUMN start_lng TO longitude;

AlTER TABLE cleansed.bike_stations
RENAME COLUMN start_station_id TO station_id;

AlTER TABLE cleansed.bike_stations
RENAME COLUMN start_station_name TO station_name;

AlTER TABLE cleansed.bike_data
RENAME COLUMN rideable_type TO bike_type;

AlTER TABLE cleansed.bike_data
RENAME COLUMN member_casual TO customer_category;



















