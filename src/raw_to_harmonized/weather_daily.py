import json
import csv

def get_json_raw(filepath):

    with open(filepath, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    return data


def create_rows_for_harmonized(raw_weather_file):
    row_list = []

    for line in raw_weather_file:
        if len(line) == 2:
            station_data = line[1]
            station_data = station_data.partition('(')[2]
            station_data = station_data.partition(')')[0]
        elif line[0] == 'Date':
            pass
        else:
            row_data = line
            row_data.insert(0, station_data)

            row_data_filled = []
            for value in row_data:
                if value == "":
                    value = None
                row_data_filled.append(value)

            row_list.append(row_data_filled)
        
    return row_list


def create_columns_for_harmonized(raw_weather_file):
    column_data = raw_weather_file[1]
    columns_list = []
    for element in column_data:
        column = element[:4]
        columns_list.append(column)

    columns_list.insert(0, 'station_id')
    return columns_list


def write_rows_to_file(row_list):
    with open('data/harmonized/weather_data_rows.json', "w") as opened_file:
        json.dump(row_list, opened_file, indent=2)


def write_columns_to_file(columns_list):
    with open('data/harmonized/weather_data_columns.json', "w") as opened_file:
        json.dump(columns_list, opened_file, indent=2)

if __name__ == "__main__":

    filepath = "data/raw/weather_data_raw.csv"

    raw_weather_file = get_json_raw(filepath)

    row_list = create_rows_for_harmonized(raw_weather_file)

    columns_list = create_columns_for_harmonized(raw_weather_file)

    write_rows_to_file(row_list)

    write_columns_to_file(columns_list)

