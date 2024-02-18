'''This program takes names from input until stop is inputted,
sorting the names alphabetically and printing them into a numbered list.'''
names = []
keep_asking = True
while keep_asking:
    try:
        name = input()
        int_name = int(name)
        print("Please pick a valid name.")
    except ValueError:
        if name.strip(" ") == "":
            print("Please pick a valid name.")
        elif name.lower() == "stop":
            names = sorted(names)
            for i in range(len(names)):
                print(f"{i+1}. {names[i]}")
            keep_asking = False
        else:
            new_name = ""
            add_name = True
            for letter in name:
                if letter.isalpha() == True or letter == " ":
                    new_name = new_name + letter
                else:
                    add_name = False
            if add_name:
                names.append(name)
            else:
                print("Please pick a valid name.")
