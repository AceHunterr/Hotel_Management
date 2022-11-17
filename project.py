from data import LoadDetails
from manager import CheckAvailability,CalculatePrice,CreateSummary

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

durationOfStay = int(input("""
    How many nights would you like to stay in for? > 
"""))

is_available = CheckAvailability(roomData,category,numberOfGuests)
if is_available:
    print(CalculatePrice(roomData,durationOfStay,category,numberOfGuests))

print(CreateSummary(roomData))

# print(roomData)