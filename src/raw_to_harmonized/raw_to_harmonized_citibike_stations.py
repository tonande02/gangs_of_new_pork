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
    sorted_list_of_keys = (sorted_list_of_keys[0],sorted_list_of_keys[1],sorted_list_of_keys[2],sorted_list_of_keys[3],
    sorted_list_of_keys[8],sorted_list_of_keys[9],sorted_list_of_keys[10],sorted_list_of_keys[11])
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
        json.dump(data, open_file)

dicto = read_json()
list_of_keys = get_sorted_keys(dicto)
list_of_row = get_list_of_rows_from_dict(dicto,list_of_keys)
write_to_file(list_of_keys,"data/raw_to_harmonized/columns.json")
write_to_file(list_of_row,"data/raw_to_harmonized/list_of_tuples.json")

