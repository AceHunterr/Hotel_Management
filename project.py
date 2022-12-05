import art
import csv

############### DATA HANDLING ######################### 

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



############### HOTEL MANAGER FUNCTIONALITY ######################### 

import math
from data import enhance_room_details,to_string_room_details        

dash =  "------------------------------------------------"
         
def CheckService(roomData,id):
    # """To Check whether the service is to make reservation or checkout"""


    # Entering Category
    cat_input = input(""" Select from the room's category
    Enter 1 for Wonderful,
    Enter 2 for Marvelous,
    Enter 3 for Spectcular,
    Enter 4 for Fantastic,
    Enter 5 for Fabulous,
    Enter 6 for Wow,

Your Choice> """)

    # Checking for Invalid Input Error using Try and Except
    try:
        category = int(cat_input)
        if not category in range(1,7):  
            print("\n!!!YOU ENTERED INVALID DATA!!!\n") 
            return None 
    except ValueError: 
        print("\n!!!YOU ENTERED INVALID DATA!!!\n") # None is returned in case user enters invalid input and raises a ValueError 
        return None

    # Entering the number of guests
    guest_input = input("""
How many guests present? > """)
    try:
        numberOfGuests = int(guest_input)
    except ValueError:
        print("\n!!!YOU ENTERED INVALID DATA!!!\n")
        return None
    
    room_details = roomData[category]
    room_details = enhance_room_details(room_details)

    if id==1:

        # Checking Availability
        is_available = CheckAvailability(roomData,category,numberOfGuests)
            

        if is_available:
            print("\nGreat. We have availability.")        
            # Entering the nights to stay 
            dur_input = input("""
How many nights would you like to stay in for? > """)
            try:
                durationOfStay = int(dur_input)
            except ValueError:
                print("\n!!!YOU ENTERED INVALID DATA!!!\n")
                return None
        
                
            # Calculating Price
            price = CalculatePrice(roomData,durationOfStay,category,numberOfGuests) 
            print(f"\n{dash}\nYour Total Price for the rooms would be: {price}\n{dash}\n")
            print("Thank You for your Patience. Your Reservation has been made\n")
            
            # Updating the data according to making reservation or checking out... id=1 : MakeReservation, id=2 :CheckOut 
            UpdateData(room_details,numberOfGuests,category,roomData,id=id)

        else:
            print("\n!!!Sorry , Currently we are out of vacancies for the entered room!!!\n")
    
    else:
        UpdateData(room_details,numberOfGuests,category,roomData,id=id)


def CheckAvailability(roomData,category,numberOfGuests):
    # """Checking the Availability depending by calculating the vacancies using occupied and unoccupied"""

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
    # """Calculate the total price according to the numbers of days(which include the different prices for days,weeks and months) and rooms booked"""

    room_details = roomData[roomIndex]
    room_details = enhance_room_details(room_details)
    capacity = room_details[2]
    per_night = room_details[3]
    per_week = room_details[4]
    per_month = room_details[5]

    # Calculating rooms needed by total guests
    int_rooms = int(numberOfGuests/capacity)
    rooms_needed = (math.floor(int_rooms)+1) if (numberOfGuests%capacity!=0) else int_rooms 

    # Calculating the price acc to price per month,week and day 
    months = math.floor(durationOfStay/30)
    days_left = durationOfStay%30
    weeks = math.floor(days_left/7)
    days = days_left%7
    total_cost = ((months*per_month) + (weeks*per_week) + (days*per_night)*rooms_needed)

    return total_cost


def UpdateData(room_details,numberOfGuests,category,roomData,id=1):
    # """Updating our roomData by changing the num_rooms_occupied field i.e. room_details[6] by adding (during reservation) or subtracting (during Checkout) the rooms in the field """
    
    capacity = room_details[2]
    int_rooms = int(numberOfGuests/capacity)
    rooms_needed = (math.floor(int_rooms)+1) if (numberOfGuests%capacity!=0) else int_rooms 

    if id ==1:
        # During Making Reservation
        room_details[6] += rooms_needed

    else:
        # During Checking Out
        if rooms_needed>room_details[6]:
            # If the Checking Out Overflows the total number of rooms present then it returns the error message
            print("\nYou have entered WRONG CHECKOUT DATA!!! TRY AGAIN\n")
        else: 
            room_details[6] -= rooms_needed
            print("\nThank You for staying at Fancy Hotel. Please Visit Again\n")
            

    room_details = to_string_room_details(room_details)
    roomData[category] = room_details

def CreateSummary(roomData):
    # """Prints the Room Category and the number of vacancies available in each room"""

    print("\n")
    for row in roomData:
        if roomData.index(row)!=0:
            print(f"{row[0]} | {int(row[1]) - int(row[6])} rooms are available")
    print("\n")


file = 'room_details.txt'
roomData = LoadDetails(file)
quit = False
stars = "***********************"
hash = "#######################"

art.tprint("FANCY   HOTEL")
print("\nWelcome to Fancy Hotel... Please select from the following services\n")

while not quit:
    # While user want to keeps entering data the process goes on

    service = input("\nEnter 1 to make a new Reservation, 2 to Check out or 'q' to quit , 's' to see rooms available : ").lower()
    
    if service == "1":
        # Creating NEW RESERVATION 

        print(f"\n{stars}\nLets Begin the Registration Process\n{stars}\n")
        CheckService(roomData,id=1)
        print(f"\n{stars}\n")

    elif service == "2":
        # CHECKING OUT the customer

        print(f"\n{stars}\nLets Begin the Checkout Process\n{stars}")
        CheckService(roomData,id=2)
        print(f"\n{stars}\n")

    elif service == 'q' or service == "quit":
        #Ending the process 

        quit = True

    elif service == 's':
        # Returning list of rooms available

        CreateSummary(roomData)

    else:
        print("\n!!! Invalid Input !!! Try Again !!!\n")

    if not quit:
        # If the user wants to continue with services can continue by typing 'y'
        if (input("Do you want to continue with our services? Enter 'y' to continue otherwise enter: ").lower()) != 'y':
            quit=True

UpdateTextFile(roomData,file)
CreateSummary(roomData)

print(f"{hash}\n !!GOODBYE!!\n{hash}")

