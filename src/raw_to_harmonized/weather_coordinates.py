import json

#opens the weather station file from raw folder
def open_weather_stations(filepath):
    with open(filepath, "r") as opened_file:
        station_data = json.load(opened_file)
        return station_data

#writes the station data to a json file for later insertion to our table
def write_stations_rows(stations_dict, filepath):
    with open(filepath, "w") as opened_file:
        json.dump(stations_dict, opened_file, indent=2)

#writes a json file with the columns we will use for our database
def write_stations_columns(columns_list, filepath):
    with open(filepath, "w") as opened_file:
        json.dump(columns_list, opened_file, indent=2)


if __name__ == "__main__":
    file_path = "data/raw/weather_coordinates.json"
    station_data = open_weather_stations(file_path)

    file_path = "data/harmonized/weather_station_rows.json"
    write_stations_rows(station_data, file_path)

    columns_list = ["stations_id", "location", "latitude", "longitude"]

    file_path = "data/harmonized/weather_station_columns.json"
    write_stations_columns(columns_list, file_path)