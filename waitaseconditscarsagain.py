''' Example of connecting to a database and running queries'''

# This is the setup stuff that will appear on every program

# Start by importing the sqlite3 library
import sqlite3

# Set the database that we will connect to
# This is uppercase as it is a constant (won't change during the program)
# Make sure this file is saved in the same folder as the database
DATABASE = "car.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Get plate from user and run search
plate = input("Enter a number plate: ")

# This search requires an exact match.
cursor.execute("SELECT * FROM car WHERE plate = ?", (plate,))
results = cursor.fetchall()

for carItem in results:
    print(f"{carItem[1]:10} {carItem[2]:10}")

# This is a fuzzy search, looks for plates that include the variable
# We need to pre-prepare the variable
like_plate = f"%{plate}%"
cursor.execute("SELECT plate, owner FROM car WHERE plate LIKE ?", (like_plate,))

results = cursor.fetchall()

for carItem in results:
    print(f"{carItem[0]:10} {carItem[1]:10}")

# This is how you run a dynamic query with two inputs
name = input("Name: ")
model = input("Model: ")
cursor.execute("SELECT plate, owner FROM car WHERE owner = ? and model=?", (name,model))
results = cursor.fetchall()

for carItem in results:
    print(f"{carItem[0]:10} {carItem[1]:10}")
