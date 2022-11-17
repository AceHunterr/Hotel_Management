import math
from data import enhance_room_details,to_string_room_details        


def CheckAvailability(roomData,category,numberOfGuests):
    room_details = roomData[category]
    room_details = enhance_room_details(room_details)
    num_rooms = room_details[1]
    capacity = room_details[2]
    rooms_occupied = room_details[6]
    vacant_rooms = num_rooms-rooms_occupied
    vacant_capacity = vacant_rooms*capacity

    if vacant_capacity >=numberOfGuests:
        return True
    else:
        return False


def CalculatePrice(roomData,durationOfStay,roomIndex,numberOfGuests):
    room_details = roomData[roomIndex]
    room_details = enhance_room_details(room_details)
    capacity = room_details[2]
    per_night = room_details[3]
    per_week = room_details[4]
    per_month = room_details[5]

    int_rooms = int(numberOfGuests/capacity)
    rooms_needed = (math.floor(int_rooms)+1) if (numberOfGuests%capacity!=0) else int_rooms 


    months = math.floor(durationOfStay/30)
    days_left = durationOfStay%30
    weeks = math.floor(days_left/7)
    days = days_left%7
    total_cost = ((months*per_month) + (weeks*per_week) + (days*per_night)*rooms_needed)

    return total_cost


def UpdateData(room_details,numberOfGuests,category,roomData,id=1):
    capacity = room_details[2]
    int_rooms = int(numberOfGuests/capacity)
    rooms_needed = (math.floor(int_rooms)+1) if (numberOfGuests%capacity!=0) else int_rooms 
    
    if id ==1:
        room_details[6] += rooms_needed
    else:
        if rooms_needed>room_details[6]:
            print("You have entered WRONG CHECKOUT DATA!!! TRY AGAIN ")
        else: 
            room_details[6] -= rooms_needed

    room_details = to_string_room_details(room_details)
    roomData[category] = room_details

def CreateSummary(roomData):
    for row in roomData:
        if roomData.index(row)!=0:
            print(f"{row[0]} | {int(row[1]) - int(row[6])} rooms are occupied")
