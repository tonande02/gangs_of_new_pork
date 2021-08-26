-- shows the 5 most and least popular start stations

SELECT * FROM (
select count (cbd.start_station_id) as total_rides, cbd.start_station_id, cbs.station_name from cleansed.bike_data as cbd
join cleansed.bike_station as cbs ON cbd.start_station_id = cbs.station_id
group by cbd.start_station_id, cbs.station_name
order by count (cbd.start_station_id) desc
limit 5) AS most_popular
UNION
SELECT * FROM (
select count (cbd.start_station_id), cbd.start_station_id, cbs.station_name from cleansed.bike_data as cbd
join cleansed.bike_station as cbs ON cbd.start_station_id = cbs.station_id
group by cbd.start_station_id, cbs.station_name
order by count (cbd.start_station_id) asc
limit 5) AS least_popular
ORDER BY total_rides DESC;