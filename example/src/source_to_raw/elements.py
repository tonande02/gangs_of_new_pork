import requests
import pprint
import json

client_id = "abd5c534-9699-4349-b4e0-5bb937752eaa"

endpoint = "https://frost.met.no/observations/v0.jsonld"

with open('data/raw/frost_station_ids.txt', 'r') as file:
    station = file.readlines()
    clean_station = []
    for element in station:
        clean_station.append(element.strip())
    # print(clean_station)

stations = ",".join(clean_station)

# elements - temperature: 'air_temperature'
# elements - precipitation: 'sum(precipitation_amount PT1H)'

parameters = {
    'sources': stations,
    'elements': 'sum(precipitation_amount PT1H)',
    'referencetime': '2021-06-01T00:00:00.000Z/2021-07-01T00:00:00.000Z',
}

r = requests.get(endpoint, parameters, auth=(client_id,''))

print(r.ok)
print(r.status_code)

weather_dict = r.json()

with open('data/raw/weather_data_precipitation.json', 'w') as file:
    json.dump(weather_dict, file, indent=2)
