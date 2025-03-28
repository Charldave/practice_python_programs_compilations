user_input = input("Enter a string: ")
length = int(input("Enter the total count: "))

if len(user_input) < length:
    user_input += ' ' * (length - len(user_input))

print(user_input)