''' This program takes a number as input and doubles it. '''

# Takes number input as a float and then prints double the number.
def run():
    try:
        num = float(input("Please enter a number. This program will then double it. "))
        print(f"Your newly doubled number is {num*2}!")
    except ValueError:
        print("Next time, enter a whole number or decimal, don't be irrational... ")
        run()
run()
