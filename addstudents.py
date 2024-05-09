''' This program enables users to add students to the database '''

####### This is the setup stuff that will appear on every program ############

# Start by importing the sqlite3 library
import sqlite3
import time
timesleep = 2

# Set the database that we will connect to
DATABASE = "students.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()


#### Menu system for the program #######
run_program = True
while run_program:
    print("Main Menu")
    print("=========")
    print("1. Add student")
    print("2. Search for student")
    print("3. See all students")
    print("4. Quit")

    # get menu selection
    get_selection = True
    while get_selection:
        try:
            selection = int(input("Enter selection: "))
            if selection <1 or selection > 4:
                print("You must enter a number from 1-4")
            else:
                get_selection = False
        except ValueError:
            print("Only numbers from 1-4 allowed")

    # Now that we have the selection, do what the user wants

    ### Add student ###
    if selection == 1:
        print("\nAdd new student")
        # Get info about student
        first_name = input("First name: ")
        last_name = input("Last name: ")
        tutor_group = input("Tutor group: ")
        city = input("City: ")
        year_group = int(input("Year group: "))
        cursor.execute("INSERT INTO student (firstName, lastName, tutorGroup, city, yearGroup) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, tutor_group, city, year_group))
        # You must add connection.commit() or else the changes will not be saved when you stop the program
        connection.commit()
        print(f"New entry added: {first_name} {last_name}")

    ### Search for a student ###
    elif selection == 2:
        print("\nSearch for a student")
        # Get info about student
        first_name = input("First name: ")
        cursor.execute(f"SELECT * FROM student WHERE firstName='{first_name}'")
        results = cursor.fetchall()
        if len(results) == 0:
            print("That student does not exist. Returning to main menu.")
        elif len(results) == 1:
            print(f"There is 1 student named {first_name}.")
            getid = True
            while getid:
                try:
                    studentid = int(input(f"To access the information on {first_name}, what is their student ID? "))
                    getid = False
                    if studentid == results[0][0]:
                        print("Granting access to information...")
                        print(f"Information about {first_name}: ")
                        print(f"{'Student ID':10} {'First Name':10} {'Last Name':10} {'Tutor Code':10} {'City':10} {'Year Group':10}")
                        print("="*80)
                        print(f"{results[0][0]:10} {results[0][1]:10} {results[0][2]:10} {results[0][3]:10} {results[0][4]:10} {results[0][5]:10}")
                        input("Press enter to return to the menu. ")
                    else:
                        print("That is incorrect, sending you back to the menu.")
                except ValueError:
                    print("Please input an integer.")
            print("")
        else:
            print(f"There are {len(results)} students named {first_name}.")
            getid = True
            while getid:
                try:
                    studentid = int(input(f"To access the information on one of the people named {first_name}, what is their student ID? "))
                    getid = False
                    idcorrect = False
                    for i in range(len(results)):
                        if studentid == results[i][0]:
                            idcorrect = True
                            print("Granting access to information...")
                            print(f"Information about {first_name}: ")
                            print(f"{'Student ID':10} {'First Name':10} {'Last Name':10} {'Tutor Code':10} {'City':10} {'Year Group':10}")
                            print("="*80)
                            print(f"{results[i][0]:10} {results[i][1]:10} {results[i][2]:10} {results[i][3]:10} {results[i][4]:10} {results[i][5]:10}")
                            input("Press enter to return to the menu. ")
                    if idcorrect == False:
                        print("That is incorrect, sending you back to the menu.")
                except ValueError:
                    print("Please input an integer.")

        print("")
        time.sleep(timesleep)

    ### Show all students ###
    elif selection == 3:
        print("\nAll students")
        cursor.execute(f"SELECT * FROM student")
        results = cursor.fetchall()
        print("To access this sensitive information, you must enter the correct password.")
        password = input("What is the password? ")
        if password == "password":
            print("Correct! Printing information...")
            time.sleep(timesleep)
            print(f"{'Student ID':10} {'First Name':10} {'Last Name':10} {'Tutor Code':10} {'City':10} {'Year Group':10}")
            print("="*80)
            for i in range(len(results)):
                print(f"{results[i][0]:10} {results[i][1]:10} {results[i][2]:10} {results[i][3]:10} {results[i][4]:10} {results[i][5]:10}")
        else:
            print("Incorrect. Redirecting to the main menu...")

    ### Quit program ###
    else:
        print("Shutting down...")
        time.sleep(timesleep)
        for i in range(10):
            print("")
        run_program = False
