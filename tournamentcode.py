''''''

# Introductory part, get name + check for actual name
print("Welcome to this tournament results processor!")
ask_name = True
while ask_name:
    is_spaces = True
    name = input("What is the name of your team? ")
    for i in range(len(name)):
        if name[i] != " ":
            is_spaces = False
    if is_spaces == True:
        print("Please choose a proper name.")
    else:
        ask_name = False


print("")

# Getting opposition names and waiting for 'done'
opponents = []
ask_opponents = True
print("You will now be entering the names of the opponents that you have played.")
print("Input 'done' to stop entering names ('done' will not be included in the names).")
while ask_opponents:
    opponent = input("Enter a name here: ")
    if opponent.lower() == "done":
        ask_opponents = False
    else:
        for i in range(len(opponent)):
            # Check for all spaces!
        opponents.append(opponent)

print("")

# Getting the scores of the matches and working out the results
print("Now, it is time to input results.")
print("Please input the number of points each team scored. (integer)")
points = 0
for i in range(len(opponents)):
    your_score = int(input(f"Please input {name}'s score here. "))
    op_score = int(input(f"Please input {opponents[i]}'s score here. "))
    if your_score > op_score:
        print("You won!")
        points += 3
    elif your_score == op_score:
        print("You drew.")
        points += 2
    else:
        print("You lost... ")
        points += 1

print("")

print("The competition is over!")
print(f"{name} finished the competition with {points} points!")
