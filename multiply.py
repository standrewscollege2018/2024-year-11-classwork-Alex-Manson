'''This program takes two integers as inputs and returns the product of the two.'''
keep_asking = True
while keep_asking:
    print("This program takes two integers as inputs and returns the product of the two.")
    try:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        keep_asking = False
    except ValueError:
        print("Next time, enter an integer, don't be irrational... ")
product = num1*num2
print(f"The product of your two integers is {product}!")
