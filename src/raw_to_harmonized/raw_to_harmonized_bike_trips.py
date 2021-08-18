import json

def read_json():
    with open("data/raw/citibike_data_full.json","r") as jsonfile:
        line = jsonfile.read()
        dictionary = json.loads(line)
        return dictionary

def get_sorted_keys(dictionary):
    list_of_keys=[]
    for i in dictionary:
        for keys in i.keys():
                list_of_keys.append(keys)
    sorted_list_of_keys = sorted(set(list_of_keys))
    
    sorted_list_of_keys = (sorted_list_of_keys[6], sorted_list_of_keys[7], sorted_list_of_keys[12], sorted_list_of_keys[4], sorted_list_of_keys[5])
    return sorted_list_of_keys   

def get_list_of_rows_from_dict(dictionary, sorted_list_of_keys):
    list_of_rows = []
    values = []
    for i in dictionary:
        values = []
        for key in sorted_list_of_keys:
            values.append(i[key])

        if values in list_of_rows:
            pass
        else:
            list_of_rows.append(values)
    return list_of_rows

def write_to_file(data, filepath):
    with open(filepath, "w") as open_file:
        json.dump(data, open_file, indent= 2)

dicto = read_json()
list_of_keys = get_sorted_keys(dicto)
list_of_row = get_list_of_rows_from_dict(dicto,list_of_keys)

write_to_file(list_of_keys,"data/harmonized/bike_data_columns.json")
write_to_file(list_of_row,"data/harmonized/bike_data_rows.json")

