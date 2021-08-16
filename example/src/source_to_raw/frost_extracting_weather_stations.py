import json
import requests


# returns the full data as python dict
def fetch_data_from_frost(url, client_id):
    r = requests.get(endpoint, auth=(client_id,''))

    # checking that the request went ok
    assert r.ok
    assert r.status_code == 200

    data = r.json() # entire raw content
    return data

# returns just info on the stations in a dict
def filter_stations_from_data(data):
    stations = data["data"]

    return stations

# prints info on stations to terminal in a readable manner
def view_stations(data):
    station_nr = 1
    for station in data:
        print(f"Station nr: {station_nr}")
        print(station["name"])
        print(station["shortName"])
        print(station["id"])
        print(f"Coordinates: {station['geometry']['coordinates']}")
        station_nr += 1
        print()

# writes the data to filepath as a json-file
def write_data_to_file(data, destination_filepath):
    with open(destination_filepath, "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False) # beholder æøå



# sets url_endpoint, client_id and destination file paths (edit as needed)
destination_path = "data/raw/raw_weather_stations.json"
client_id = "6d199937-3f7a-48cb-9c12-384cecb6cb07" # Tonjes id
endpoint = "https://frost.met.no/sources/v0.jsonld?types=SensorSystem&county=Oslo*"

# fetch the data
data = fetch_data_from_frost(endpoint, client_id)

# # ---- run this to write the data to file ----
write_data_to_file(data, destination_path)

# # ---- run this to view content in terminal --
# stations = filter_stations_from_data(data)
# # view relevant info on each station
# view_stations(stations)
# # view whole data file in formatted json style
# pretty_data = json.dumps(data, indent=2)
# print(pretty_data)
