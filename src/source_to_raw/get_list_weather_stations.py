import json

FILE_PATH = "test.json"

def find_info(filepath):
    with open(filepath, "r") as opened_file:
        our_files = json.load(opened_file)
        return our_files

def make_list(our_files):
    stations = our_files["features"]
    our_dict = {}
    for station in stations:
        our_id = station['properties']['stationIdentifier']
        our_coord = station['geometry']['coordinates']
        our_dict[our_id] = our_coord
        #print(station['properties']['stationIdentifier'])
    return our_dict

def write_file(our_dict):
    with open('test2.json', "w") as opened_file:
        json.dump(our_dict, opened_file, indent=2)

if __name__ == "__main__":

    our_files = find_info(FILE_PATH)

    our_dict = make_list(our_files)

    write_file(our_dict)
    #print(len(our_dict))