from data import LoadDetails,enhance_room_details,UpdateTextFile
from manager import CheckAvailability,CalculatePrice,CreateSummary,UpdateData

file = 'room_details.txt'
roomData = LoadDetails(file)
quit = False

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
    How many nights would you like to stay in for? > """))
            price = CalculatePrice(roomData,durationOfStay,category,numberOfGuests) 
            print(f"\nYour Total Price for the rooms would be: {price}\n")
        else:
            print("\n!!!Sorry , Currently we are out of vacancies for the entered room!!!\n")
    
    UpdateData(room_details,numberOfGuests,category,roomData,id=id)
    CreateSummary(roomData)


# while not quit:

service = input("Enter 1 to make a new Reservation, 2 to Check out or 'q' to quit , 's' to see rooms available : ")

if service == "1":
    CheckService(id=1)
elif service == "2":
    CheckService(id=2)
elif service == 'q' or service == "quit":
    pass
elif service == 's':
    CreateSummary(roomData)
else:
    print("\n!!! Invalid Input !!! Try Again !!!\n")

UpdateTextFile(roomData,file)
