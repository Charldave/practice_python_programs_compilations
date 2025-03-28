user_input = input("Enter a string: ")
ends_with = input("Enter ending to check: ")

length = len(ends_with)

print(user_input[-length:] == ends_with)