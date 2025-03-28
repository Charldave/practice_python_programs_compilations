user_input = input("Enter a string: ")
swapped = ""

for case in user_input:
    if case.isupper():
        swapped += case.lower()
    elif case.islower():
        swapped += case.upper()
    else:
        swapped += case

print(swapped)