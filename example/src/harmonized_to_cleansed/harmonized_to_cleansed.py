import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json

# conn = psycopg2.connect(
#     host = "academy-de-course-2021-summer-prod-001.postgres.database.azure.com",
#     dbname = "postgres",
#     user = "consultant@academy-de-course-2021-summer-prod-001",
#     password = "3eBXkuVvaJ5ncNGP",
#     port = 5432
# )

# conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# with conn.cursor() as cur:
#     cur.execute("CREATE DATABASE bikes_weather_db;")

# conn.close()
#-----------------------------------------------------------------
def create_schema(name):
#    global cur
    cur.execute("CREATE SCHEMA IF NOT EXISTS " + name + ";")
#-----------------------------------------------------------------
def create_table(schema, name, column_list):
    create_str = "CREATE TABLE IF NOT EXISTS "
    create_str += schema + "." + name
    create_str += " (c_id SERIAL PRIMARY KEY"
    for column_name in column_list:
        create_str += ", " + column_name + " TEXT"
    create_str += ");"
    print(create_str)
    cur.execute(create_str)
#-----------------------------------------------------------------
def populate_db_from_list_of_dict(schema_name, table_name, list_of_dict_to_add):
    list_of_rows = []
    for dict in list_of_dict_to_add:
        list_of_rows.append(tuple(dict.values()))
        # print("type(dict.values()) = " + type(dict.values()))

    columns = dict.keys()
    columns_str = ", ".join(columns)  # The resulting string: 'product_line_id, product_line, manager, updated_at'
    list_w_percent_s = ["%s"] * len(list_of_dict_to_add)  # Resulting list: ['%s', '%s', '%s', '%s', '%s', '%s', '%s']
    records_list_template = ", ".join(list_w_percent_s)  # Resulting string: '%s, %s, %s, %s, %s, %s, %s'
    insert_query = f"INSERT INTO {schema_name}.{table_name} ({columns_str}) VALUES {records_list_template}"
    cur.execute(insert_query, list_of_rows)
    return cur.rowcount

#-----------------------------------------------------------------
def get_list_of_dict_from_json(file_path):
    with open(file_path, "r") as r_file:
        r_loaded = json.load(r_file)
    if type(r_loaded) == list:  # to get columns from: obs_station_infor.json og obs_20*.json
        return r_loaded
    else:   # to get columns from: Frost stasjoninfo
        return r_loaded["stations"]
#-----------------------------------------------------------------
def get_columns_frost_json(file_path):
    with open(file_path, "r") as r_file:
        loaded_json = json.load(r_file)

    columns = []
    list_of_measurements = loaded_json["data"]
    example = list_of_measurements[0]
    for key, value in example.items():
        if type(value) != list: # and type(value) != dict:
            columns.append(key)
        elif type(value) == list: # L17
            for item in value: # L19-34 -contains one dictionarys and 6..
                if type(item) == dict: # L18
                    for key2, value2 in item.items():
                        if type(value2) != dict:
                            columns.append(key + "_" + key2)
                        else:   # L22
                            for key3, value3 in value2.items():
                                columns.append(key + "_" + key2 + "_" + key3)
                if type(item) != dict:
                    columns.append(key)
    # print(columns)
    return columns

#-----------------------------------------------------------------    
def get_measurement_data_from_json(file_path):
    with open(file_path, "r") as r_file:
        loaded_json = json.load(r_file)

    all_data = []
    list_of_measurements = loaded_json["data"]
    for measurement in list_of_measurements:
        pre_data = []
        data = []

        for key, value in measurement.items():
            if type(value) != list: # and type(value) != dict:
                if value == None or value == "":
                    value = "NULL"
                pre_data.append(value)
            elif type(value) == list: # L17
                
                for item in value: # L19-34 -contains one dictionary and 6..
                    if type(item) == dict: # L18
                        for key2, value2 in item.items():
                            if type(value2) != dict:
                                if value == None or value == "":
                                    value = "NULL"
                                data.append(value2)
                            else:   # L22
                                for key3, value3 in value2.items():
                                    if value == None or value == "":
                                        value = "NULL"
                                    data.append(value3)
                    if type(item) != dict:
                        if value == None or value == "":
                            value = "NULL"
                        data.append(value)

                    ## after each list item
                    if len(pre_data) == 2 and len(data) > 8:
                        measurement_data = pre_data + data
                        all_data.append(tuple(measurement_data))
                    else:
                        print(f"FAULT: len(pre_data) == {len(pre_data)} and len(data) == {len(data)}")
                    data = []

        # if len(data) > 10:
        #     all_data.append(tuple(data))
    # print(all_data)
    return all_data

#-----------------------------------------------------------------    
def populate_db_from_list_of_tuples(schema_name, table_name, columns, list_of_tuples_to_add):
    list_of_rows = list_of_tuples_to_add

    columns_str = ", ".join(columns)  # The resulting string: 'product_line_id, product_line, manager, updated_at'
    list_w_percent_s = ["%s"] * len(list_of_tuples_to_add)  # Resulting list: ['%s', '%s', '%s', '%s', '%s', '%s', '%s']
    records_list_template = ", ".join(list_w_percent_s)  # Resulting string: '%s, %s, %s, %s, %s, %s, %s'

    insert_query = f"INSERT INTO {schema_name}.{table_name} ({columns_str}) VALUES {records_list_template}"
    # return insert_query, list_of_rows
    cur.execute(insert_query, list_of_rows)
    return cur.rowcount

#-----------------------------------------------------------------
def populate_hard():
    frost_temp_columns = get_columns_frost_json("data/raw/weather_data_temperature.json")
    frost_perc_columns = get_columns_frost_json("data/raw/weather_data_precipitation.json")

    frost_temp_data = get_measurement_data_from_json("data/raw/weather_data_temperature.json")
    frost_perc_data = get_measurement_data_from_json("data/raw/weather_data_precipitation.json")
    
    print(populate_db_from_list_of_tuples(schema, "temperature", frost_temp_columns, frost_temp_data))
    print(populate_db_from_list_of_tuples(schema, "rain", frost_perc_columns, frost_perc_data))

#-----------------------------------------------------------------    
def get_columns_from_frost_stations_json(file_path):
    with open(file_path, "r") as r_file:
        loaded_json = json.load(r_file)
    stations = loaded_json["stations"]
    dict_ex = stations[0]
    column_list = dict_ex.keys()
    print(column_list)
    return column_list
#-----------------------------------------------------------------
def get_columns_from_obs_json(file_path):
    with open(file_path, "r") as r_file:
        loaded_json = json.load(r_file)
    dict_ex = loaded_json[0]
    column_list = dict_ex.keys()
    print(column_list)
    return column_list
#-----------------------------------------------------------------
def create_schema_and_tables():
    create_schema(schema)

    frost_temp_columns = get_columns_frost_json("data/raw/weather_data_temperature.json")
    frost_perc_columns = get_columns_frost_json("data/raw/weather_data_precipitation.json")
    frost_weather_station_columns = get_columns_from_frost_stations_json("data/harmonized/harmonized_weather_stations.json")
    obs_bike_trip_columns = get_columns_from_obs_json("data/harmonized/obs_2021-06.json")
    obs_bike_station_columns = get_columns_from_obs_json("data/harmonized/obs_station_info.json")

    create_table(schema, "weather_station", frost_weather_station_columns)
    create_table(schema, "temperature", frost_temp_columns)
    create_table(schema, "rain", frost_perc_columns)
    create_table(schema, "bike_station", obs_bike_station_columns)
    create_table(schema, "bike_trip", obs_bike_trip_columns)

def populate_easy():
    frost_weather_station_data = get_list_of_dict_from_json("data/harmonized/harmonized_weather_stations.json")
    obs_bike_trip_data = get_list_of_dict_from_json("data/harmonized/obs_2021-06.json")
    obs_bike_station_data = get_list_of_dict_from_json("data/harmonized/obs_station_info.json")
    
    print(populate_db_from_list_of_dict(schema, "weather_station", frost_weather_station_data))
    print(populate_db_from_list_of_dict(schema, "bike_trip", obs_bike_trip_data))
    print(populate_db_from_list_of_dict(schema, "bike_station", obs_bike_station_data))

#################################################################
schema = "cleansed"
db_name = "biking_engineers"#"bikes_weather_db"#

conn = psycopg2.connect(
    host = "academy-de-course-2021-summer-prod-001.postgres.database.azure.com",
    dbname = db_name,
    user = "consultant@academy-de-course-2021-summer-prod-001",
    password = "3eBXkuVvaJ5ncNGP",
    port = 5432
)

cur = conn.cursor()

# create_schema_and_tables()
# populate_easy()
populate_hard()

conn.commit()
conn.close()





"""
        create_str = "INSERT INTO " + schema + "." + table_name + " (" + ", ".join(dict.keys()) + ") VALUES (" + value_str + ");" #"id, name, latitude, longditude"
        args_str = ','.join(cur.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s)", x) for x in tup)

mogr_str = []
tup = tuple(("a1","b2","c3","d4"))
print(tup)
for x in tup:
    moggy = cur.mogrify("(%s,%s,%s,%s)", x)
    print(moggy)
    mogr_str.append(moggy)
print(mogr_str)
args_str = ','.join(mogr_str)
print(args_str)
"""