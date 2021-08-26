-- shows the 5 most popular end stations, and 50 non-station drop of points

SELECT * FROM (
select count (cbd.end_station_id) as total_rides, cbd.end_station_id, cbs.station_name from cleansed.bike_data as cbd
join cleansed.bike_station as cbs ON cbd.end_station_id = cbs.station_id
group by cbd.end_station_id, cbs.station_name
order by count (cbd.end_station_id) desc
limit 5) AS most_popular
UNION
SELECT * FROM (
select count (cbd.end_station_id), cbd.end_station_id, cbs.station_name from cleansed.bike_data as cbd
join cleansed.bike_station as cbs ON cbd.end_station_id = cbs.station_id
group by cbd.end_station_id, cbs.station_name
order by count (cbd.end_station_id) asc
limit 50) AS least_popular
ORDER BY total_rides DESC;