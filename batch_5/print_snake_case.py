name = input('Enter your full name in incorrect casing: ')
name = name.lower().strip().replace(" ", "_")
print(name)