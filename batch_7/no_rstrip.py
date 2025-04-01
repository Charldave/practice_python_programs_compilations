user_input = input('Enter a characters: ')

trim_count = 0
for spaces in reversed(user_input):
    if spaces == ' ':
        trim_count += 1
    else:
        break

if trim_count > 0:
    print(user_input[:-trim_count])
else:
    print(user_input)