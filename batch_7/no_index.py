user_input = input("Enter a string: ")
string_find = input("Enter the character to find: ")

found_index = -1

for count in range(len(user_input)):
    if user_input[count] == string_find:
        found_index = count
        break

if found_index != -1:
    print(found_index)
else:
    print("not found")