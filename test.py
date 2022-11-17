import csv

roomData = [['category_name', 'num_rooms', 'capacity', 'pp_night', 'pp_week', 'pp_month', 'num_rooms_occupied'], ['Wonderful', '20', '2', '1200', '8000', '30000', '2'], ['Marvelous', '20', '2', '1500', '9000', '35000', '3'], ['Spectacular', '20', '3', '1600', '10000', '40000', '2'], ['Fantastic', '20', '4', '2000', '12000', '50000', '2'], ['Fabulous', '20', '5', '2200', '13000', '60000', '2'], ['Wow', '20', '5', '2500', '15000', '65000', '2']]

def UpdateTextFile(roomData):
    with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for row in roomData:
            writer.writerow(row)