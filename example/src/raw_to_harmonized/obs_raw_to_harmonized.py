import json
from os import listdir

def get_raw_filenames(file_folder = None):
    if file_folder == None:
        file_folder = "."
    files = []
    for filename in listdir(file_folder):
        fn = filename.split(".")
        if len(fn) == 2:
            if fn[0][0:6] == "obs_20" and fn[1] == "json":
                files.append(filename)
    return files

def get_json_from_file(file_path):
    with open(file_path, "r") as r_file:
        json_content = json.load(r_file)
    return json_content # returns a list of dictionarys

def save_harmonized(filename, harmonized_data):
    file_path = "data/harmonized/" + filename
    with open(file_path, "w") as r_file:
        json.dump(harmonized_data, r_file)

def remove_excess_parts(raw_list_of_dict):
    har_list_of_dict = []
    keys_to_include = ["started_at", "ended_at", "start_station_id", "end_station_id"]
    for dict in raw_list_of_dict:
        new_dict = {}
        for key in dict.keys():
            if key in keys_to_include:
                new_dict[key] = dict[key]
        har_list_of_dict.append(new_dict)
    return har_list_of_dict

def reduce_timestamps(list_of_dict):
    for dict in list_of_dict:
        dict["started_at"] = dict["started_at"].split(".")[0]
        dict["ended_at"] = dict["ended_at"].split(".")[0]
    return list_of_dict

def harmonize(file_path):
    raw_data = get_json_from_file(file_path)
    harmonized_data = reduce_timestamps(remove_excess_parts(raw_data))
    filename = file_path.split("/")[-1]
    save_harmonized(filename, harmonized_data)

def harmonize_all():
    file_folder = "data/raw/"
    filenames = get_raw_filenames(file_folder)
    for filename in filenames:
        harmonize(file_folder + filename)

harmonize_all()

def harmonize_station_info():
    file_path = "data/raw/obs_station_info.json"
    raw_data = get_json_from_file(file_path)
#    prind(json.dumps(raw_data, indent=2))
    harmonized_data = raw_data["data"]["stations"]
    filename = file_path.split("/")[-1]
    save_harmonized(filename, harmonized_data)

#harmonize_station_info()