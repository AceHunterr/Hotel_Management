from data import LoadDetails,enhance_room_details
from manager import CheckAvailability,CalculatePrice,CreateSummary,UpdateData

roomData = LoadDetails('room_details.txt')
quit = False

# def CheckOut():
#     category = int(input("""
#         Enter 1 for Wonderful,
#         Enter 2 for Marvelous,
#         Enter 3 for Spectcular,
#         Enter 4 for Fantastic,
#         Enter 5 for Fabulous,
#         Enter 6 for Wow,

#         Your Choice> """))

#     numberOfGuests = int(input("""
#         How many guests present? > """))
    
#     room_details = roomData[category]
#     room_details = enhance_room_details(room_details)

#     print(roomData)
#     print(room_details)
#     UpdateData(room_details,numberOfGuests,category,roomData,id=2)
#     print(roomData)

# def MakeReservation():
#     category = int(input("""
#         Enter 1 for Wonderful,
#         Enter 2 for Marvelous,
#         Enter 3 for Spectcular,
#         Enter 4 for Fantastic,
#         Enter 5 for Fabulous,
#         Enter 6 for Wow,

#         Your Choice> """))

#     numberOfGuests = int(input("""
#         How many guests will stay in the room? > """))

#     durationOfStay = int(input("""
#         How many nights would you like to stay in for? > 
#     """))

#     is_available = CheckAvailability(roomData,category,numberOfGuests)
#     if is_available:
#         print(CalculatePrice(roomData,durationOfStay,category))

#     room_details = roomData[category]
#     room_details = enhance_room_details(room_details)

#     print(roomData)
#     UpdateData(room_details,numberOfGuests,category,roomData,id=1)
#     print(roomData)

def CheckService(id):

    category = int(input("""
    Enter 1 for Wonderful,
    Enter 2 for Marvelous,
    Enter 3 for Spectcular,
    Enter 4 for Fantastic,
    Enter 5 for Fabulous,
    Enter 6 for Wow,

    Your Choice> """))

    numberOfGuests = int(input("""
        How many guests present? > """))
    
    room_details = roomData[category]
    room_details = enhance_room_details(room_details)

    if id==1:

        is_available = CheckAvailability(roomData,category,numberOfGuests)
        if is_available:
            durationOfStay = int(input("""
    How many nights would you like to stay in for? > 
            """))
            print(CalculatePrice(roomData,durationOfStay,category,numberOfGuests))
        else:
            print("!!!Sorry , Currently we are out of vacancies for the entered room!!!")
    print(roomData)
    UpdateData(room_details,numberOfGuests,category,roomData,id=id)
    print(roomData)


# while not quit:

service = input("Enter 1 to make a new Reservation, 2 to Check out or 'q' to quit: ")

if service == "1":
    CheckService(id=1)
elif service == "2":
    CheckService(id=2)
elif service == 'q' or service == "quit":
    pass

CreateSummary(roomData)
# print(roomData)
# print(roomData)