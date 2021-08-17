import json
from pathlib import Path
import requests
import csv
import io

STATION_IDS = ["USC00284339",
"USC00287545",
"US1NJBG0018",
"USC00305816",
"US1NYNY0078",
"USW00094728",
"US1NYNY0074",
"USC00305806",
"USC00305799",
"US1NYBX0025",
"USC00300961",
"USW00014732",
"USC00302868",
"US1NYQN0026",
"USC00305804",
"US1NYQN0002",
"USC00300958",
"US1NYKN0025"]

ENDPOINT = "https://www.ncei.noaa.gov/access/past-weather/ID/data.csv"


def get_data_from_station_endpoint(endpoint):
    response = requests.get(endpoint)
    r = response.text

    reader = csv.DictReader(io.StringIO(r))
    # print(reader)
    # print(len(reader))

    # json_data = []
    # for row in reader:
    #     json_data.append(row)
    json_data = json.dumps(list(reader))
    # print(json_data)
    
    with open("data/raw/w_station1.json","w",encoding="utf-8") as new_file:
            jsonString = json.dumps(json_data, indent=4)
            new_file.write(jsonString)


if __name__ == "__main__":
    get_data_from_station_endpoint("https://www.ncei.noaa.gov/access/past-weather/USC00284339/data.csv")