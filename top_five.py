'''Top Five JToH Towers List - user creation and editing.'''
towers = []
print("Welcome to the Top Five JToH Towers list!")
print("Please enter your top five JToH towers below.")
print("As a reminder, tower acronyms must start with 'To', 'Co', or 'So', with no numbers, special characters, or spaces.")

for i in range(5):
    keep_start_adding = True
    while keep_start_adding:
        in_towers = False
        start_tower = input(f"{i+1}. ")
        if start_tower.strip() == "":
            print("Please do not enter blanks/spaces.")
        elif start_tower.isalpha() == False:
            print("Please pick an acronym with no numbers, special characters, or spaces.")
        elif len(start_tower) > 6 or len(start_tower) < 3:
            print("The length of your tower is invalid, please re-enter your tower.")
        elif (start_tower[0] == "T" or start_tower[0] == "C" or start_tower[0] == "S") and start_tower[1] == "o":
            for j in range(len(towers)):
                if towers[j].lower() == start_tower.lower():
                    in_towers = True
            if in_towers == False:
                keep_start_adding = False
                towers.append(start_tower)
            else:
                print("That tower has already been entered, please pick another one.")
        else:
            print("Remember, tower acronyms must start with 'To', 'Co', or 'So'.")

def menu():
    print("Top 5 Towers Menu")
    print("="*17)
    print("1. See the top 5")
    print("2. Add a tower to the top 5")
    print("3. Quit program")

    keep_selectioning = True
    while keep_selectioning:
        try:
            selection = int(input("Selection: "))
            if selection < 4 and selection > 0:
                keep_selectioning = False
            else:
                print("Invalid selection. Please enter an integer from 1 to 3 (inclusive).")
        except ValueError:
            print("Invalid selection. Please enter an integer from 1 to 3 (inclusive).")

    if selection == 1:
        print("Top 5 Towers")
        print("="*12)
    elif selection == 2:
        print("Add a Tower")
        print("="*11)
    else:
        keep_quitsureing = True
        while keep_quitsureing:
            quitsure = input("Are you sure you want to quit the program? (y or n) ")
            if quitsure.lower() == "y":
                print("Quitting program...")
                keep_quitsureing = False
            elif quitsure.lower() == "n":
                print("Okay, sending you back to the menu...")
                keep_quitsureing = False
                menu()
            else:
                print("Please pick either y or n.")
menu()
