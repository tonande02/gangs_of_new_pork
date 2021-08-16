import json
from pathlib import Path
import requests

def get_data_from_frost_api(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        response_json = response.json()
        #list_of_stations = []
        #for station in response_json:
            #list_of_stations.append("stationIdentifier")
        #return list_of_stations

        return response_json
        
    else:
        return None


def write_file(list_of_stations):
    with open('test.json', "w") as opened_file:
        json.dump(list_of_stations, opened_file, indent=2)


if __name__ == "__main__":
    endpoint = "https://api.weather.gov/stations?state=NY"

    list_of_stations = get_data_from_frost_api(endpoint)

    write_file(list_of_stations)

    for i in list_of_stations:
        print(i)

