import csv

def LoadDetails(csv_file):
    with open(csv_file, 'r') as file:
        readCSV = csv.reader(file,delimiter=',')
        rooms_data_list = [row for row in readCSV]
        return rooms_data_list

def enhance_room_details(list):
    return [int(item) if list.index(item)!=0 else item for item in list]

def to_string_room_details(list):
    return [str(item) for item in list]