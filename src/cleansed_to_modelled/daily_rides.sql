-- shows amount of rain and total rides taken from each bike station for every day

select distinct bd.start_station_id, date(wd.date), wd.precipitation_centimeters, count(bd.start_station_id) as amount_of_rides from cleansed.weather_data wd 
join cleansed.weather_station ws on wd.station_id = ws.station_id 
join cleansed.bike_station bs on wd.station_id = bs.nearest_weather_station 
join cleansed.bike_data bd on bs.station_id  = bd.start_station_id 
where wd.date >= '2021-06-01'
and wd.date < '2021-08-01'
and wd.date = date(bd.started_at)
group by bd.start_station_id , wd.date, wd.precipitation_centimeters
order by bd.start_station_id asc, date desc;