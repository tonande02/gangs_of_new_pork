ALTER TABLE cleansed.bike_data
ALTER COLUMN started_at TYPE timestamp without time zone USING started_at::timestamp without time zone;

ALTER TABLE cleansed.bike_data
ALTER COLUMN ended_at TYPE timestamp without time zone USING ended_at::timestamp without time zone;

ALTER TABLE cleansed.bike_stations
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






















