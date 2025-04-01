user_input = input('Enter a characters: ')

trim_count = 0
for spaces in reversed(user_input):
    if spaces == ' ':
        trim_count += 1
    else:
        break

print(user_input[:-trim_count])