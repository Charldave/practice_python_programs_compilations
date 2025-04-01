user_input = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")

length = len(suffix)

if user_input[-length:] == suffix:
    user_input = user_input[:-length]

print(user_input)