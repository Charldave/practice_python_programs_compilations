user_input = input("Enter a string: ")

if user_input:
    capped = user_input[0].upper() + user_input[1:].lower()
    print(capped)
else:
    print("Empty input.")