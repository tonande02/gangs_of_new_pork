from io import BytesIO
from urllib.request import urlopen
import urllib.parse
from zipfile import ZipFile
import csv

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
    with open(f"data/raw/{file_name}","r") as file:
        csv_reader = csv.reader(file)

        with open("data/raw/citibike_data.json","w") as new_file:
            csv_writer = csv.writer(new_file)

            for line in csv_reader:
                csv_writer.writerow(line)

file_name = download_zip_file()

from_csv_to_json(file_name)