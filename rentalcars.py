''''''
import time
cars = [["Suzuki Van", 2, True], ["Toyota Corolla", 4, True], ["Honda CRV", 4, True], \
["Suzuki Swift", 4, True], ["Mitsubishi Airtrek", 4, True], ["Nissan DC Ute", 4, True], \
["Toyota Previa", 7, True], ["Toyota Hi Ace", 12, True], ["Toyota Hi Ace", 12, True]]
keep_running = True
while keep_running:
    print("Here is the list of vehicles for the day.")
    for i in range(len(cars)):
        available = " not"
        if cars[i][2] == True:
            available = ""
        time.sleep(0.1)
        print(f"{i+1}. A {cars[i][0]} is{available} available to be rented. It seats {cars[i][1]}.")
    ask_car = True
    while ask_car:
        try:
            print("You will now be inputting the vehicle you will book. Input '0' to end the program.")
            choice = int(input("Which vehicle would you like to book? (please pick a number from the list) "))
            if choice > 0:
                if choice <= len(cars):
                    ask_car = False
                else:
                    print("Please pick a car from the list.")
            elif choice == 0:
                keep_running = False
            else:
                print("Please pick a car from the list.")
        except ValueError:
            print("Please pick a car from the list.")
    if cars[choice][2] == True:
        print("Cool, that car is available to hire.")
        get_name = True
        while get_name:
            name = input("What is your name? ")
            name_alpha = True
            if name.isalpha() == False:
                for i in range(len(name)):
                    if name[i].isalpha() == False:
                        if name[i] != " ":
                            name_alpha = False
            if name_alpha == True:
                get_name = False
            else:
                print("Please pick a valid name.")
        print(f"Thanks, {name}.")
    else:
        print("Sorry, that car is not available to hire.")
print("It's time for the daily summary.")
print("These are the vehicles that have been booked, and the people who have booked them.")
print("")
