user_input = input("Enter a string: ")

words = user_input.split()
capped_words = []

for word in words:
    capped_word = word[0].upper() + word[1:].lower() if word else ''
    capped_words.append(capped_word)

result = ' '.join(capped_words)
print(result)