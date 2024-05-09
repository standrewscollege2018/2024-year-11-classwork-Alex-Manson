''' Cars database stuff'''

import sqlite3

DATABASE = "cars.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Run a query
cursor.execute("SELECT * FROM car")
# Get results
results = cursor.fetchall()

# Loop over results list and display each result one at a time
print(f"{'Number Plate':15} {'Name':25} {'Make':20} Model")
print("="*73)
for i in range(len(results)):
    print(f"{i+1}. {results[i][1]:12} {results[i][2]:25} {results[i][3]:20} {results[i][4]}")
