user_input = input("Enter a string: ")
desired_width = int(input("Enter the total width: "))

spaces_to_add = desired_width - len(user_input)

if spaces_to_add > 0:
    print(' ' * spaces_to_add + user_input)
else:
    print(user_input)