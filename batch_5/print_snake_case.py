name = input('Enter your full name in incorrect casing: ')
name = name.lower().replace(" ", "_")
print(name)