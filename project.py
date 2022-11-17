from data import LoadDetails,enhance_room_details

roomData = LoadDetails('room_details.txt')

category = int(input("""
    Enter 1 for Wonderful,
    Enter 2 for Marvelous,
    Enter 3 for Spectcular,
    Enter 4 for Fantastic,
    Enter 5 for Fabulous,
    Enter 6 for Wow,

    Your Choice> """))

numberOfGuests = int(input("""
    How many guests will stay in the room? > """))

def CheckAvailability(roomData,category,numberOfGuests):
    room_details = roomData[category]
    room_details = enhance_room_details(room_details)
    
    num_rooms = room_details[1]
    capacity = room_details[2]
    rooms_occupied = room_details[6]
    vacant_rooms = num_rooms-rooms_occupied
    vacant_capacity = vacant_rooms*capacity

    # print(room_details)
    # print(vacant_capacity)

    if vacant_capacity >=numberOfGuests:
        return True
    else:
        return False


# def CalculatePrice(roomData,durationOfStay,roomIndex):
#     room_details = roomData[roomIndex]
#     room_details = enhance_room_details(room_details)



is_available = CheckAvailability(roomData,category,numberOfGuests)
# if is_available:
#     CalculatePrice()


# print(CheckAvailability(roomData,category,numberOfGuests))

# print(type(choice))

