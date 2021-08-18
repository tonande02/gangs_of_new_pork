import json


def open_weather_stations(filepath):
    with open(filepath, "r") as opened_file:
        our_files = json.load(opened_file)
        return our_files


def make_list_stations(our_stations):
    stations = our_stations["features"]
    stations_dict = {}

    for station in stations:
        station_id = station['properties']['stationIdentifier']
        station_coordinates = station['geometry']['coordinates']
        stations_dict[station_id] = station_coordinates
    return stations_dict


def write_stations_dict(stations_dict, filepath):
    with open(filepath, "w") as opened_file:
        json.dump(stations_dict, opened_file, indent=2)


if __name__ == "__main__":
    file_path = "data/raw/get_weather_stations.json"
    our_files = open_weather_stations(file_path)
    
    stations_dict = make_list_stations(our_files)

    file_path = "data/raw/get_list_weather_stations.json"
    write_stations_dict(stations_dict, file_path)
