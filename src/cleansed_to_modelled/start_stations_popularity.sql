-- shows the 5 most and least popular start stations

select * from (
select count (cbd.start_station_id) as total_rides, cbd.start_station_id, cbs.station_name from cleansed.bike_data as cbd
join cleansed.bike_station as cbs on cbd.start_station_id = cbs.station_id
group by cbd.start_station_id, cbs.station_name
order by count (cbd.start_station_id) desc
limit 5) as most_popular
union
select * from (
select count (cbd.start_station_id), cbd.start_station_id, cbs.station_name from cleansed.bike_data as cbd
join cleansed.bike_station as cbs on cbd.start_station_id = cbs.station_id
group by cbd.start_station_id, cbs.station_name
order by count (cbd.start_station_id) asc
limit 5) as least_popular
order by total_rides desc;