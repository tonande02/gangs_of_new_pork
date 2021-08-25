SELECT ride_id, COUNT(ride_id) FROM cleansed.bike_data GROUP BY ride_id ORDER BY count(ride_id) DESC;

SELECT station_id, COUNT(station_id) FROM cleansed.bike_station GROUP BY station_id ORDER BY count(station_id) DESC;

SELECT station_id, COUNT(station_id) FROM cleansed.weather_station GROUP BY station_id ORDER BY count(station_id) DESC;

SELECT station_id, date, COUNT(station_id), COUNT(date) FROM cleansed.weather_data 
GROUP BY station_id, date ORDER BY COUNT(station_id) DESC, COUNT(date) DESC;
