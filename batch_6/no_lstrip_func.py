user_input = input('Enter characters or words: ')
spaces = 0

for count in user_input:
    if count != ' ':
        break
    spaces += 1

no_space = user_input[spaces:]

print(no_space)