import json

def read_json():
    with open("data/raw/citibike_data_full.json","r") as jsonfile:
        line = jsonfile.read()
        dictionary = json.loads(line)
        return dictionary

def get_sorted_keys_start(dictionary):
    list_of_keys=[]
    for i in dictionary:
        for keys in i.keys():
                list_of_keys.append(keys)
    sorted_list_of_keys = sorted(set(list_of_keys))
    
    sorted_list_of_keys_start = (sorted_list_of_keys[8],sorted_list_of_keys[9],sorted_list_of_keys[10],sorted_list_of_keys[11])
    return sorted_list_of_keys_start

def get_sorted_keys_end(dictionary):
    list_of_keys=[]
    for i in dictionary:
        for keys in i.keys():
                list_of_keys.append(keys)
    sorted_list_of_keys = sorted(set(list_of_keys))
    
    sorted_list_of_keys_end = (sorted_list_of_keys[0],sorted_list_of_keys[1],sorted_list_of_keys[2],sorted_list_of_keys[3])
    return sorted_list_of_keys_end

def get_list_of_rows_from_dict(dictionary, sorted_list_of_keys_start):
    list_of_rows = []
    values = []
    for i in dictionary:
        values = []
        for key in sorted_list_of_keys_start:
            values.append(i[key])

        if values in list_of_rows:
            pass
        else:
            list_of_rows.append(values)
    return list_of_rows

def adding_missing_stations(dictionary,list_of_rows,list_of_keys_end):
    values = []
    for i in dictionary:
        values = []
        for key in list_of_keys_end:
            values.append(i[key])
            
        for i in list_of_rows:
            if values not in list_of_rows:
                list_of_rows.append(values)
            else:
                pass

    return list_of_rows

def removing_missing_values(new_list_of_rows):
    lista = []
    for i in new_list_of_rows:
        if "" in i:
            pass
        else:
            lista.append(i)
    return lista

def removing_duplicates(list_of_rows):
    lists_of_ids = []
    new_list_of_rows = []
    for lists in list_of_rows:
        if lists[2] not in lists_of_ids:
            lists_of_ids.append(lists[2])
        else:
            pass
    
    lists_of_ids=set(lists_of_ids)

    for i in list_of_rows:
        if i[2] in lists_of_ids:
            new_list_of_rows.append(i)
            lists_of_ids.remove(i[2])
    
    return new_list_of_rows                      

def write_to_file(data, filepath):
    with open(filepath, "w") as open_file:
        json.dump(data, open_file, indent= 2)

dicto = read_json()
list_of_keys_start = get_sorted_keys_start(dicto)
list_of_keys_end = get_sorted_keys_end(dicto)
list_of_row = get_list_of_rows_from_dict(dicto,list_of_keys_start)
new_list_of_rows = adding_missing_stations(dicto,list_of_row,list_of_keys_end)
lastone = removing_missing_values(new_list_of_rows)
last2=removing_duplicates(lastone)

write_to_file(list_of_keys_start,"data/harmonized/bike_stations_columns.json")
write_to_file(last2,"data/harmonized/bike_stations_rows.json")

