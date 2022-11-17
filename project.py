from data import LoadDetails,UpdateTextFile
from manager import CreateSummary,CheckService
import art

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
