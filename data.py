import csv

def LoadDetails(csv_file):
    # """Reading data from the CSV File and then converting it into list of lists"""

    with open(csv_file, 'r') as file:
        readCSV = csv.reader(file,delimiter=',')
        
        # The first row i.e. index=0 in the list of lists would be the header row that contains the title fields... therefore our room categories should start from index 1 not 0
        rooms_data_list = [row for row in readCSV]
        return rooms_data_list

def enhance_room_details(list):
    # """For converting the numeric data which is in string format to integer format for calculations"""

    return [int(item) if list.index(item)!=0 else item for item in list]

def to_string_room_details(list):
    # """For converting all the data back to string format to write in the file"""

    return [str(item) for item in list]

def UpdateTextFile(roomData,file):
    # """Writing the updated data recieved back in to the file"""

    with open(file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for row in roomData:
            writer.writerow(row)
