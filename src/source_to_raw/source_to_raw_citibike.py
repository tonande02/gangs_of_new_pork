from io import BytesIO
from urllib.request import urlopen
import urllib.parse
from zipfile import ZipFile
import csv
import json

def download_zip_file():
    zipurl = "https://s3.amazonaws.com/tripdata/JC-202106-citibike-tripdata.csv.zip"
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall('data/raw')
    
    zipc = urllib.parse.urlsplit(zipurl)
    zipc= zipc.path.split("/")[-1]
    zipc=(zipc[:-4])
    return(zipc)

def from_csv_to_json(file_name):
    jsonArray = []

    with open(f"data/raw/{file_name}",encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            jsonArray.append(row)

        with open("data/raw/citibike_data.json","w",encoding="utf-8") as new_file:
            jsonString = json.dumps(jsonArray, indent = 4)
            new_file.write(jsonString)

file_name = download_zip_file()

from_csv_to_json(file_name)

