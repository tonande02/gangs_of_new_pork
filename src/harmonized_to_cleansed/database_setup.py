import json
from pathlib import Path
import psycopg2

############################################
# Connecting to the database   
DB_HOST = "gmpzlu2vtr1icu.cs0xobsxhp2r.eu-west-1.rds.amazonaws.com"
DB_USER = "GangsofNP"
PASSWORD = "Awesometeam2021"
PORT = 5432
DESTINATION_DB_NAME = "NYCbike"
############################################

DESTINATION_SCHEMA_NAME  = "staged"



def read_json_files(fpath):
    with open(fpath,"r") as file_json:
        lines = file_json.read()
        jsonf = json.loads(lines)

    return jsonf

def creating_query_table(schema_name, table_name, fp):
    columns_datatype = []
    for columns in fp:
        col = columns + " TEXT"
        columns_datatype.append(col)
    
    columns_string = ", ".join(columns_datatype)


    query = f'CREATE TABLE IF NOT EXISTS {schema_name}.{table_name}'
    query += f'(Id_column serial PRIMARY KEY,'
    query += columns_string
    query += ", audit_inserted_to_staged_at TIMESTAMP DEFAULT NOW() );"
    return query

























































if __name__ == "__main__":
    with psycopg2.connect(
        host = DB_HOST,
        dbname = DESTINATION_DB_NAME,
        user = DB_USER,
        password = PASSWORD,
        port = PORT,
   ) as connection_destination_db:

        with connection_destination_db.cursor() as cursor:
            jsonf = read_json_files("data/raw_to_harmonized/columns.json")
            fp =creating_query_table("BIKER","BIKER",jsonf)
            cursor.execute(fp)

        connection_destination_db.commit()

    #jsonf = read_json_files("data/raw_to_harmonized/columns.json")


    table_names = ["weather_data", "weather_station", "bike_data", "bike_station"]

    #fp =creating_query_table(DESTINATION_SCHEMA_NAME,"BIKER",jsonf)
    #fp = f"data/raw_to_harmonized/{​table_names[0]}​_columns.json"




