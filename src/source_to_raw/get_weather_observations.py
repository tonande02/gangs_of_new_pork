# Test-script for getting weather observations from weather station IDs

import json
from pathlib import Path
import requests


# returns list with station IDs from json-file
def get_station_ids_from_file(file_path):
    with open(file_path, "r") as opened_file:
        file_dict = json.load(opened_file)
    
    station_list = []
    for key in file_dict.keys():
        station_list.append(key)

    return station_list


# returns endpoint-url for one station
# date format must be: yyyy-mm-dd
def get_base_url(station_id, start_time, end_time):
    endpoint = f"https://api.weather.gov/stations/{station_id}/observations"
    endpoint += f"?start={start_time}T00%3A00%3A00%2B00%3A00&end={end_time}T00%3A00%3A00%2B00%3A00"

    return endpoint


# returns json from one endpoint-url
def get_data_from_one_station(endpoint):
    response = requests.get(endpoint)

    if response.status_code == 200:
        response_json = response.json()

        return response_json        

    else:
        return None


# writes data to one json file
def get_data_from_all(list_of_stations, start_t, end_t):
    with open('data/raw/observations.json', "a") as open_file:
        for station in list_of_stations:
            url = get_base_url(station, start_t, end_t)
            data = get_data_from_one_station(url)
        
            json.dump(data, open_file, indent=2)




## Edit below with correct paths
LIST_FILE = "data/raw/get_list_weather_stations.json"
# LIST_OF_STATION_IDs = get_station_ids_from_file(LIST_FILE)


if __name__ == "__main__":
    stations = get_station_ids_from_file(LIST_FILE)
    get_data_from_all(stations, "2021-08-08", "2021-08-15")

    ## just for testing
    # station = stations[510]
    # endpoint = get_base_url(station, "2021-08-08", "2021-08-10")
    # print(endpoint)
    # print(station)
    