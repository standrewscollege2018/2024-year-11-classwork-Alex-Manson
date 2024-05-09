'''Titanic database searching!'''

# Importing the stuff thingies
import time
import sqlite3

# time.sleep() setting
timesleep = 0

# Welcome!
print("Hi there, and welcome to the Titanic database.")
print("="*46)
print(""*2)

# Run the main program.
def run():
    # Get class from user - ask until adequate response is received.
    keep_classing = True
    while keep_classing:
        try:
            tclass = int(input("What class do you want to search on? (integer from 1 to 3) "))
            if tclass < 4 and tclass > 0:
                keep_classing = False
            else:
                print("Please enter an integer between 1 and 3.")
        except ValueError:
            print("Please enter an integer between 1 and 3.")

    # Get survived/deceased input in similar manner.
    keep_surceasing = True
    while keep_surceasing:
        try:
            surceased = int(input("Please enter 1 for the the list of survivors or 0 for the deceased: "))
            if surceased == 0 or surceased == 1:
                keep_surceasing = False
            else:
                print("Please enter 1 for survivors or 0 for deceased.")
        except ValueError:
            print("Please enter 1 for survivors or 0 for deceased.")

    # Database stuff - getting results
    DATABASE = "titanic.db"
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM passenger WHERE survived={surceased} AND class={tclass}")
    results = cursor.fetchall()

    # How many results were found?
    print(f"There are {len(results)} results found.")

    # Print names.
    for i in range(len(results)):
        time.sleep(timesleep)
        print(f"{i+1}. {results[i][3]}")

    # Ask if the user wants to run another query and act upon the answer.
    keep_againing = True
    while keep_againing:
        again = input("Would you like to run another query? (y or n) ")
        if again == "y":
            print("Running again...")
            print(""*2)
            keep_againing = False
            run()
        elif again == "n":
            print("Okay, bye.")
            keep_againing = False
        else:
            print("Please pick y or n.")

# Run the main program!
print("Menu")
print("="*4)
print("Search by name")
print("Search by passenger class")
print("Quit program")
run()
