'''This program is a raffle program.
It takes the prize name and value, and then takes names for the raffle.
It will then choose a random person to win the raffle.'''

import random

names = []

# Get the name and value of the prize and ensure validity.
print("Welcome to my raffle program!")
prize_name = input("Please input the name of the prize here. ")

ask_value = True
while ask_value:
    try:
        prize_value = float(input("Please input the value of the prize here. $"))
        ask_value = False
    except ValueError:
        print("Please enter a number.")

# Get the names and check if they are valid...
print("Okay, now you will be entering names for the raffle.")
print("Type 'end' at any time to finish entering names!")
print("Note: only letters and spaces will be accepted.")

ask_names = True
while ask_names:
    name = input("Please enter a name here. ")
    if name.isalpha() == True:
        if name.lower() == "end":
            ask_names = False
        else:
            names.append(name)
    else:
        name_accept = True
        for i in range(len(name)):
            if name[i].isalpha() == False:
                if name[i] != " ":
                    name_accept = False
        if name_accept == True:
            names.append(name)

# Time for the winner to be announced!
print(f"The winner of the raffle is...  {names[random.randint(0, len(names) - 1)]}!")
print(f"Congratulations on your {prize_name} worth ${prize_value}!")
