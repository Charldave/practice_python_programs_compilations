user_input = input("Enter a string: ")

upper_to_lower = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x','Y': 'y', 'Z': 'z'}
lower = ''

for letter in user_input:
    if letter in upper_to_lower:
        lower += upper_to_lower[letter]
    else:
        lower += letter

print(lower)