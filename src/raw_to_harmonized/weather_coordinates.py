import json

def open_weather_stations(filepath):
    with open(filepath, "r") as opened_file:
        station_data = json.load(opened_file)
        return station_data

def write_stations_rows(stations_dict, filepath):
    with open(filepath, "w") as opened_file:
        json.dump(stations_dict, opened_file, indent=2)

def write_stations_columns(columns_list, filepath):
    with open(filepath, "w") as opened_file:
        json.dump(columns_list, opened_file, indent=2)


if __name__ == "__main__":
    file_path = "data/raw/weather_coordinates.json"
    station_data = open_weather_stations(file_path)

    file_path = "data/harmonized/weather_coordinates_rows.json"
    write_stations_rows(station_data, file_path)

    columns_list = ["stations_id", "location", "latitude", "longitude"]

    file_path = "data/harmonized/weather_station.json"
    write_stations_columns(columns_list, file_path)