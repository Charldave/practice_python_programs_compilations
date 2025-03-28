user_input = input("Enter a string: ")

all_upper = True
for count in user_input:
    if 'a' <= count <= 'z':
        all_upper = False
        break

print(all_upper)