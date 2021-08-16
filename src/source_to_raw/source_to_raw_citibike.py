from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import requests
import json
import csv

def download_zip_file():
    zipurl = "https://s3.amazonaws.com/tripdata/JC-202106-citibike-tripdata.csv.zip"
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall('data/raw')



def from_csv_to_json():
    with open("data/raw/citibike_data.csv","r") as file:
        csv_reader = csv.reader(file)

        with open("data/raw/citibike_data.json","w") as new_file:
            csv_writer = csv.writer(new_file)

            for line in csv_reader:
                csv_writer.writerow(line)

download_zip_file()

from_csv_to_json()