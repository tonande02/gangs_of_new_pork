import json

def open_weather_stations(filepath):
    with open(filepath, "r") as opened_file:
        our_files = json.load(opened_file)
        return our_files

def write_stations_rows(stations_dict, filepath):
    with open(filepath, "w") as opened_file:
        json.dump(stations_dict, opened_file, indent=2)

def write_stations_columns(columns_list, filepath):
    with open(filepath, "w") as opened_file:
        json.dump(columns_list, opened_file, indent=2)


if __name__ == "__main__":
    file_path = "data/raw/weather_coordinates.json"
    our_files = open_weather_stations(file_path)

    file_path = "data/harmonized/weather_coordinates_rows.json"
    write_stations_rows(our_files, file_path)

    columns_list = ["stations_id", "location", "latitude", "longitude"]

    file_path = "data/harmonized/weather_coordinates_columns.json"
    write_stations_columns(columns_list, file_path)