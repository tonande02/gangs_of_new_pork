-- shows the number of rides with/without rain from each station, and the difference in percentage

select dry.dry_id as station_id, dry.dry_rides, rainy.rainy_rides, sum(100 -( (rainy.rainy_rides::numeric / 100 ) / (dry.dry_rides::numeric / 100 ) * 100)) as percentage_less_rain_rides from 
(select bd.start_station_id as dry_id, count(bd.start_station_id) as dry_rides from cleansed.bike_data bd
join cleansed.bike_station bs on bd.start_station_id = bs.station_id 
where (bs.nearest_weather_station, date(bd.started_at)) in 
(select station_id, date(date) from cleansed.weather_data wd
where precipitation_centimeters = 0
and date(date) >= '2021-06-01'
group by station_id, date(date) )
group by dry_id 
order by dry_id) as dry
join (select bd.start_station_id as rainy_id, count(bd.start_station_id) as rainy_rides from cleansed.bike_data bd
join cleansed.bike_station bs on bd.start_station_id = bs.station_id 
where (bs.nearest_weather_station, date(bd.started_at)) in 
(select station_id, date(date) from cleansed.weather_data wd
where precipitation_centimeters > 0
and date(date) >= '2021-06-01'
group by station_id, date(date) )
group by rainy_id 
order by bd.start_station_id ) as rainy on rainy.rainy_id = dry.dry_id
group by station_id, dry.dry_rides, rainy.rainy_rides
order by dry.dry_rides desc, rainy.rainy_rides desc