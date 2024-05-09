''' Example of connecting to a database and running queries'''

####### This is the setup stuff that will appear on every program ############

# Start by importing the sqlite3 library
import sqlite3

# Set the database that we will connect to
# This is uppercase as it is a constant (won't change during the program)
# Make sure this file is saved in the same folder as the database
DATABASE = "students.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Run a query
cursor.execute("SELECT * FROM student")
# Get results
results = cursor.fetchall()

# Loop over results list and display each result one at a time
print("Here are the names: ")
for i in range(len(results)):
    print(f"{i+1}. {results[i][1]:10} {results[i][2]:15} {results[i][3]}")
# OR this way
for student in results:
    print(f"{student[1]:10} {student[2]:15} {student[3]}")
