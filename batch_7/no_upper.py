user_input = input("Enter a string: ")

lower_to_upper = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F','g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L','m': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R','s': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X','y': 'Y', 'z': 'Z'}

uppercase = ''

for letter in user_input:
    if letter in lower_to_upper:
        uppercase += lower_to_upper[letter]
    else:
        uppercase += letter

print(uppercase)