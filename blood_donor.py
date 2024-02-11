# This program will check if someone is eligible for blood donation (i.e. age 16+ and weight 50kg and over)
keep_asking = True
AGE_MIN = 16
WEIGHT_MIN = 50

def check(a, w):
    if a >= AGE_MIN and w >= WEIGHT_MIN:
        return ""
    else:
        return " not"

while keep_asking:
    try:
        print("Please enter the details below to proceed with the eligibility check for blood donation. ")
        age = int(input("Please enter your age in years as an integer. "))
        weight = int(input("Please enter your weight in kilograms (without the kg sign) as an integer. "))
        if age > 0 and weight > 0:
            keep_asking = False
        elif age < 1 and weight > 0:
            print("Age must be positive and non-zero. ")
        elif age > 0 and weight < 0:
            print("Weight must be positive and non-zero. ")
        else:
            print("Weight and age must be positive and non-zero. ")
    except ValueError:
        print("Next time, enter an integer, don't be irrational... ")

print(f"You are{check(age, weight)} eligible to donate blood. ")
