def firstRecurring(given_string):
    counts = {}  # initialise a dictionary
    for char in given_string:
        if char in counts:
            print(char)
            return char
        else:
            counts[char] = 1
    return None


my_string = input("Enter your string:  ")
firstRecurring(my_string)

