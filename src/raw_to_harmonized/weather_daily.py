import json
import csv

def get_json_raw(filepath):

    with open(filepath, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    return data

def parse_file(file_dict):
    our_list = []

    for line in file_dict:
        if len(line) == 2:
            our_key = line[1]
            our_key = our_key.partition('(')[2]
            our_key = our_key.partition(')')[0]
        elif line[0] == 'Date':
            pass
        else:
            our_list2 = line
            our_list2.insert(0, our_key)
            our_list.append(our_list2)

    return our_list

def get_our_columns(file_dict):
    our_list = file_dict[1]
    our_list.insert(0, 'station_id')
    return our_list

def write_columns_to_file(columns_list):
    with open('data/harmonized/weather_columns.json', "w") as opened_file:
        json.dump(columns_list, opened_file, indent=2)

def write_rows_to_file(row_list):
    with open('data/harmonized/weather_row.json', "w") as opened_file:
        json.dump(row_list, opened_file, indent=2)

if __name__ == "__main__":

    filepath = "data/raw/weather_data_for_conversion.csv"

    file_dict = get_json_raw(filepath)

    row_list = parse_file(file_dict)

    columns_list = get_our_columns(file_dict)

    write_columns_to_file(columns_list)

    write_rows_to_file(row_list)