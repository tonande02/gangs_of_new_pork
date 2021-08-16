# cleansing weather station data from json-file to create a json-file with only
# relevant data

import json
from json import encoder

# read and store json file as python dict
def read_json_to_dict(source_path):
    with open(source_path, "r") as j_file:
        data = json.load(j_file)
    
    assert type(data) == dict
    assert len(data) > 0

    return data

# returns a dictionary with the following information:
# total number of stations, station id, station name, coordinates 
def filter_relevant_data(data):
    relevant_data = dict()

    # adding total nr of stations to dict
    nr_of_stations = data["totalItemCount"]
    relevant_data["nr_of_stations"] = nr_of_stations

    # creating a list  to hold the separate station dicts
    list_of_station_dicts = []

    # for each station in the data, adds dict with relevant info to list
    for dictionary in data["data"]:
        station = dict()
        station["id"] = dictionary["id"]
        station["name"] = dictionary["name"]
        station["latitude"] = dictionary["geometry"]["coordinates"][1]
        station["longitude"] = dictionary["geometry"]["coordinates"][0]
        
        list_of_station_dicts.append(station)
    
    # adds list of station-dicts to main station-dict
    relevant_data["stations"] = list_of_station_dicts

    return relevant_data

# prints cleaned data on stations to terminal
def view_filtered_data(filtered_data):
    pretty_filtered = json.dumps(filtered_data, indent=2)
    print(pretty_filtered)

# writes cleaned dictionary to new json-file
def write_data_to_file(data, destination_filepath):
    with open(destination_filepath, "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False) # beholder æøå



# sets source and destination file paths (edit as needed)
source_path = "data/raw/raw_weather_stations.json"
destination_path = "data/harmonized/harmonized_weather_stations.json"

# # fetch and filter the data
data = read_json_to_dict(source_path)
filtered_data = filter_relevant_data(data)

# # ---- run this to write data to file ----
write_data_to_file(filtered_data, destination_path)

# # ---- run this to view cleaned data in terminal ----
# view_filtered_data(filtered_data)
