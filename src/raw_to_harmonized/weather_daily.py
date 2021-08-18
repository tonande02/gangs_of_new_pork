import json
import csv

def get_json_raw(filepath):
    #with open(filepath, "r") as opened_file:
        #file_dict = json.load(opened_file)
        #return file_dict
    #writer = csv.writer(opened_file)
    #for line in response.iter_lines():
        #writer.writerow(line.decode('utf-8').split(','))
    with open(filepath, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    return data

        #print(data[0])
        #print(data[1])
        #print(data[2])

def parse_file(file_dict):
    our_dict = {}

    for line in file_dict:
        if len(line) == 2:
            our_key = line[1]
            our_key = our_key.partition('(')[2]
            our_key = our_key.partition(')')[0]
            print(our_key)





if __name__ == "__main__":

    #filepath = "data/raw/weather_data_raw.json"
    filepath = "data/raw/weather_data_for_conversion.csv"

    file_dict = get_json_raw(filepath)

    parse_file(file_dict)