from pathlib import Path
import requests
import json
import csv

# downloads and combines datasets from each station into one csv-file
def download_csvs_from_endpoint(base_endpoint, list_of_station_ids):
    new_file = "data/raw/weather_data_raw.csv"

    for station in list_of_station_ids:
        endpoint = base_endpoint.replace("ID", station)
        response = requests.get(endpoint)
        
        with open(new_file, "a") as file:
            writer = csv.writer(file)
            for line in response.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))
    
    return new_file

if __name__ == "__main__":
    STATION_IDS = [
        "USC00284339",
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

    BASE_ENDPOINT = "https://www.ncei.noaa.gov/access/past-weather/ID/data.csv"
    
    # these two run the program and download the files
    file = download_csvs_from_endpoint(BASE_ENDPOINT, STATION_IDS)