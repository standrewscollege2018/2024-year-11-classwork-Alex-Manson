'''This program has a list of vehicles that can be hired by the user if available.
When the user hires a vehicle (inputting their name), it is no longer available as a choice for others.
When all of the hiring is complete (when the user inputs "0"),
the program will print out the hired cars and the people who hired them.'''
# Get everything set up.
sleephalf = 0.5
sleep1 = 1
sleep2 = 2
sleep3 = 3
import time
cars = [["Suzuki Van", 2, True], ["Toyota Corolla", 4, True], ["Honda CRV", 4, True], \
["Suzuki Swift", 4, True], ["Mitsubishi Airtrek", 4, True], ["Nissan DC Ute", 4, True], \
["Toyota Previa", 7, True], ["Toyota Hi Ace", 12, True], ["Toyota Hi Ace", 12, True]]
cars_names = []
keep_running = True
# Keep asking for vehicle hires.
while keep_running:
    print("Welcome to the vehicle hiring system!")
    time.sleep(sleep1)
    print("Here is the list of vehicles for the day.")
    time.sleep(sleephalf)
    for i in range(len(cars)):
        # Transforming the True/False into a useable format.
        available = " not"
        if cars[i][2] == True:
            available = ""
        time.sleep(sleephalf)
        # Printing the cars, whether they are available, and how many people they seat.
        print(f"{i+1}. A {cars[i][0]} is{available} available to be rented. It seats {cars[i][1]}.")
    ask_car = True
    while ask_car:
        try:
            # Choosing the vehicle to book.
            time.sleep(sleep1)
            print("You will now be inputting the vehicle you will book. Input '0' to end the program.")
            time.sleep(sleep2)
            choice = int(input("Which vehicle would you like to book? (please pick a number from the list) "))
            # Checking validity of the choice.
            if choice > 0:
                if choice <= len(cars):
                    ask_car = False
                else:
                    print("Please pick a car from the list.")
            elif choice == 0:
                # Stop asking for vehicle hire.
                keep_running = False
                ask_car = False
            else:
                print("Please pick a car from the list.")
        except ValueError:
            # Not an integer.
            print("Please pick a car from the list.")
    # Check whether to go through the hiring process - did they input 0?
    if choice != 0:
        chose_none = False
        # Is the car available to hire?
        if cars[choice-1][2] == True:
            time.sleep(sleep1)
            print("Cool, that car is available to hire.")
            cars[choice-1][2] = False
            # Getting the name of the hirer.
            get_name = True
            while get_name:
                time.sleep(sleep1)
                name = input("What is your name? ")
                name_alpha = True
                is_spaces = True
                # Check the validity of the name (probably could be improved)
                if name.isalpha() == False:
                    for i in range(len(name)):
                        if name[i].isalpha() == False:
                            if name[i] != " ":
                                name_alpha = False
                for i in range(len(name)):
                    if name[i] != " ":
                        is_spaces = False
                if name_alpha == True:
                    if is_spaces == True:
                        time.sleep(sleep1)
                        print("Please pick a valid name.")
                    else:
                        get_name = False
                else:
                    time.sleep(sleep1)
                    print("Please pick a valid name.")
            # The name was a success.
            time.sleep(sleep1)
            print(f"Thanks, {name}.")
            for i in range(2):
                print("")
            time.sleep(sleep3)
            # Add the hire to the list of lists of vehicles and names.
            cars_names.append([cars[choice-1][0], name])
        else:
            # The user chose a car that had already been hired.
            time.sleep(sleep1)
            print("Sorry, that car is not available to hire.")
            time.sleep(sleep1)
        # This is a clever way to figure out if I have defined chose_none.
    else:
        try:
            if chose_none:
                print("This is a bug.")
        except:
            chose_none = True
# Summary of vehicle hires!
time.sleep(sleep2)
print("")
time.sleep(sleephalf)
print("")
time.sleep(sleep1)
print("It's time for the daily summary.")
time.sleep(sleep2)
if chose_none == False:
    print("These are the vehicles that have been booked, and the people who have booked them.")
    time.sleep(sleep2)
    for i in range(len(cars_names)):
        print(f"{cars_names[i][0]} - {cars_names[i][1]}")
        time.sleep(sleep1)
else:
    # No vehicles were booked.
    print("It seems that no vehicles have been booked today.")
    time.sleep(sleep1)
print("")
print("-end-")
