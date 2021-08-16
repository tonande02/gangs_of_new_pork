import json
# Test-script for getting weather observations from weather station IDs

from pathlib import Path

# returns list with station IDs from json-file
def get_endpoints(file_path):
    with open(file_path, "r") as opened_file:
        file_dict = json.load(opened_file)
    
    station_list = []
    for key in file_dict.keys():
        station_list.append(key)

    return station_list
    


## Edit below with correct paths
LIST_FILE = "data/raw/get_list_weather_stations.json"
LIST_OF_ENDPOINTS = get_endpoints(LIST_FILE)


if __name__ == "__main__":
    stations = get_endpoints(LIST_FILE)
    #here