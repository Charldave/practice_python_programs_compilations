user_input = input("Enter a string: ")
string_find = input("Enter the character to count: ")

count = 0

for find in user_input:
    if find == string_find:
        count += 1

print(f"appeared {count} times.")