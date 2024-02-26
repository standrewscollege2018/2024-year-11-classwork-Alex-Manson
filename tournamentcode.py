'''This program takes a team name and opposition team names,
as well as the scores of their matches,
and outputs the total score the primary team got.'''

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
        space = True
        for i in range(len(opponent)):
            if opponent[i] != " ":
                space = False
        if space == True:
            print("Please choose a proper name.")
        else:
            opponents.append(opponent)

print("")

# Getting the scores of the matches and working out the results
print("Now, it is time to input results.")
print("Please input the number of points each team scored. (integer)")
points = 0
keep_scoring = True
while keep_scoring:
    try:
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
        keep_scoring = False
    except ValueError:
        print("Please input an integer as the score.")

print("")

print("The competition is over!")
print("You get 3 points for a win, 2 points for a draw, and 1 point for a loss.")
print(f"{name} finished the competition with {points} points!")
