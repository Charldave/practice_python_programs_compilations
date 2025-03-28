user_input = input("Enter a string: ")

prefix = user_input[0]
index = 0

while index < len(user_input) and user_input[index] == prefix:
    index += 1

result = user_input[index:]

print(f"Result: {result}")