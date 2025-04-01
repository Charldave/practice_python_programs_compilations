user_input = input("Enter a string: ")
starts_with = input("Enter prefix to check: ")

length = len(starts_with)

print(user_input[:length] == starts_with)