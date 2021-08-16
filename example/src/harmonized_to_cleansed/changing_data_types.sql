select * from cleansed.weather_station ws 

alter table cleansed.weather_station 
alter column latitude type numeric using latitude::numeric,
alter column longitude type numeric using longitude::numeric;

select * from cleansed.bike_trip bt 

alter table cleansed.bike_trip
alter column started_at type timestamp using started_at::timestamp,
alter column ended_at type timestamp using ended_at::timestamp,
alter column start_station_id type int using start_station_id::int,
alter column end_station_id type int using end_station_id::int;

select * from cleansed.bike_station bs 

alter table cleansed.bike_station
alter column station_id type int using station_id::int,
alter column lat type numeric using lat::numeric,
alter column lon type numeric using lon::numeric,
alter column capacity type int using capacity::int;

select * from cleansed.rain r 

alter table cleansed.rain 
alter column referencetime type timestamp using referencetime::timestamp,
alter column observations_value type float using observations_value::float,
alter column observations_timeseriesid type float using observations_timeseriesid::float,
alter column observations_exposurecategory type float using observations_exposurecategory::float,
alter column observations_qualitycode type float using observations_qualitycode::float;

select * from cleansed.temperature t 

alter table cleansed.temperature 
alter column referencetime type timestamp using referencetime::timestamp,
alter column observations_value type float using observations_value::float,
alter column observations_level_value type float using observations_level_value::float,
alter column observations_timeseriesid type float using observations_timeseriesid::float,
alter column observations_exposurecategory type float using observations_exposurecategory::float,
alter column observations_qualitycode type float using observations_qualitycode::float;








