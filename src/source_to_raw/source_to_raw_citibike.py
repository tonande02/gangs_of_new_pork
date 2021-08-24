from io import BytesIO
from urllib.request import urlopen
import urllib.parse
from zipfile import ZipFile
import csv
import json

def download_zip_file(lista): #Downloads zipfile, extracts the csv and saves into data/raw folder.

    zipurl = lista
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall('data/raw')
    zipc = urllib.parse.urlsplit(zipurl) #Renames the csv-file
    zipc= zipc.path.split("/")[-1]
    zipc=(zipc[:-4])
    return(zipc)

def merging_all_csv_files(list_of_csv):
    new_file = "data/raw/citibike_data_full.csv"
    columns_inserted = False

    for i in list_of_csv:
        with open(f"data/raw/{i}","r") as csvf:
            file = csv.reader(csvf)
            with open(new_file,"a") as large_csv:
                writer = csv.writer(large_csv)
                for line in file:
                    if line[0] == "ride_id":
                        if columns_inserted == False:
                            writer.writerow(line)
                            columns_inserted = True
                        else:
                            pass
                    else:
                        writer.writerow(line)

def from_csv_to_json(csvf): #Converts csv into json format.
    jsonArray = []
    with open(f"{csvf}",encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            jsonArray.append(row)
        with open("data/raw/citibike_data_full.json","a",encoding="utf-8") as new_file:
            jsonString = json.dumps(jsonArray, indent = 4)
            new_file.write(jsonString)

if __name__ == "__main__":
    lista = ["https://s3.amazonaws.com/tripdata/JC-202106-citibike-tripdata.csv.zip","https://s3.amazonaws.com/tripdata/JC-202107-citibike-tripdata.csv.zip"]
    list_of_csv = []

    for i in lista:
        file_name = download_zip_file(i)
        list_of_csv.append(file_name)
        
    merging_all_csv_files(list_of_csv)
    from_csv_to_json("data/raw/citibike_data_full.csv")