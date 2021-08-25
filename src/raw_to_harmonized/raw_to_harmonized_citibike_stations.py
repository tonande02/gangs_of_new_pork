import json

def read_json():

    with open("data/raw/citibike_data_full.json","r") as jsonfile:

        line = jsonfile.read()
        list_of_dicts = json.loads(line)
        return list_of_dicts



def get_sorted_keys_start(list_of_dicts):

    list_of_keys_start=[]

    for dict in list_of_dicts: #Going through each dict within the list of dicts
        for keys in dict.keys(): 
                list_of_keys_start.append(keys) #Appending each key(START STATIONS) that exist in the dicts into a list
    sorted_list_of_keys = sorted(set(list_of_keys_start))
    #Picking out all the unqiue keys(set) and sorting(sorted) them since they allways comes in diffrent orders.

    sorted_list_of_keys_start = (sorted_list_of_keys[8],sorted_list_of_keys[9],sorted_list_of_keys[10],sorted_list_of_keys[11])
    return sorted_list_of_keys_start #returning desired keys in list



def get_sorted_keys_end(list_of_dicts):

    list_of_keys_end=[]

    for dict in list_of_dicts: #Going through each dict within the list of dicts
        for keys in dict.keys():
                list_of_keys_end.append(keys) #Appending each key(END STATIONS) that exist in the dicts into a list
    sorted_list_of_keys = sorted(set(list_of_keys_end))
     #Picking out all the unqiue keys(set) and sorting(sorted) them since they allways comes in diffrent orders.

    sorted_list_of_keys_end = (sorted_list_of_keys[0],sorted_list_of_keys[1],sorted_list_of_keys[2],sorted_list_of_keys[3])
    return sorted_list_of_keys_end #returning desired keys in list



def get_list_of_values_from_dict(list_of_dicts, sorted_list_of_keys_start):

    list_of_values = []
    values = []

    for dicts in list_of_dicts: # Going through each dict within the list of dicts
        values = []
        for key in sorted_list_of_keys_start: #Using desired keys to get the right values into a list. 
            values.append(dicts[key]) 

        if values in list_of_values: #Appending each list of values into a list
            pass
        else:
            list_of_values.append(values)
    return list_of_values



def adding_missing_stations(list_of_dicts,list_of_values,list_of_keys_end):

    

    # Going through the end station data to see if 
    # we missed any stations. If so, appending them
    # into the already created list_of_values.

    for dicts in list_of_dicts: 
        #values = []
        for key in list_of_keys_end: 
            values.append(dicts[key])
            
<<<<<<< HEAD
        for i in list_of_values:
            if values not in list_of_values:
                list_of_values.append(values)
=======
        for value in values:
            if value not in list_of_values:
                list_of_values.append(value)
>>>>>>> d7a8c9ce045e87c2415b6c32e504b0c2116650a1
            else:
                pass

    return list_of_values



def removing_missing_values(list_of_values_start_and_end):

    removed_values_list = []

    for i in list_of_values_start_and_end:
        if "" in i:
            pass
        else:
            removed_values_list.append(i)

    return removed_values_list


def removing_duplicates(list_of_values_start_and_end):

    #Removing dublicates of stations

    lists_of_ids = []
    final_list_of_values = []

    for lists in list_of_values_start_and_end:
        if lists[2] not in lists_of_ids:
            lists_of_ids.append(lists[2])
        else:
            pass
    
    lists_of_ids=set(lists_of_ids)

    for i in list_of_values_start_and_end:
        if i[2] in lists_of_ids:
            final_list_of_values.append(i)
            lists_of_ids.remove(i[2])
    
    return final_list_of_values                      



def write_to_file(data, filepath):

    with open(filepath, "w") as open_file:
        json.dump(data, open_file, indent= 2)


if __name__ == "__main__":
    dicto = read_json() #reading json_file

    list_of_keys_start = get_sorted_keys_start(dicto) #Getting start station keys

    list_of_keys_end = get_sorted_keys_end(dicto) #Getting end station keys

    list_of_values = get_list_of_values_from_dict(dicto,list_of_keys_start) #Adding values for desired keys

    list_of_values_start_and_end = adding_missing_stations(dicto,list_of_values,list_of_keys_end) #Adding missing stations
    print(list_of_values_start_and_end)

    #list_of_values_start_and_end = removing_missing_values(list_of_values_start_and_end) #Removing missing values (" ")

    #final_list_of_vlues=removing_duplicates(list_of_values_start_and_end) #Remvoing dublicates of stations

<<<<<<< HEAD
    #write_to_file(list_of_keys_start,"data/harmonized/bike_station_columns.json")
    #write_to_file(final_list_of_vlues,"data/harmonized/bike_station_rows.json")
=======
    write_to_file(list_of_keys_start,"data/harmonized/test_bike_station_columns.json")
    write_to_file(final_list_of_vlues,"data/harmonized/test_bike_station_rows.json")
>>>>>>> d7a8c9ce045e87c2415b6c32e504b0c2116650a1

