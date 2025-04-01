user_input = input("Enter a string: ")
width = int(input("Enter total width: "))

zeros = width - len(user_input)

if zeros > 0:
    print('0' * zeros + user_input)
else:
    print(user_input)