user_inputs = input("Enter strings: ") 

lowered = ''

for c in user_inputs:
    if 'A' <= c <= 'Z':
        lowered += chr(ord(c) + 32)
    else:
        lowered += c

print(lowered)