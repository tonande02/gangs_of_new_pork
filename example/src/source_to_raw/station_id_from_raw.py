### Getting a list of the weather station ids for using with
### weather data extraction script

import json

# stores the data from json file as python dict
def get_dict_from_file(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
        
        return data
    except FileNotFoundError:
        print("File not found - check your filename/path")

# returns station_ids as list of strings
def station_ids_from_data(data):
    stations = data["data"]
    station_ids = []

    for station in stations:
        id = station["id"]
        station_ids.append(id)

    return station_ids

# writes the data to filepath as a .txt-file
def write_data_to_file(data, filepath):
    with open(filepath, "w") as file:
        for line in data:
            file.write(line)
            file.write("\n")


# sets source and destination filepaths (edit as needed)
source_filepath = "data/raw/raw_weather_stations.json" # enter correct filepath here
destination_path = "data/raw/frost_station_ids.txt" # add correct path here

# get the data
data = get_dict_from_file(source_filepath)
station_ids = station_ids_from_data(data)

# # ---- run this to write the data to file ----
write_data_to_file(station_ids, destination_path)

# # ---- run this to view content in terminal --
# print(station_ids)
