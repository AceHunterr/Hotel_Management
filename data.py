import csv


with open('room_details.txt', 'r') as file:
    readCSV = csv.reader(file,delimiter=',')
    print(readCSV)
    
    rooms_data_list = [row for row in readCSV]
    print(rooms_data_list)