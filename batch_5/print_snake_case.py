name = input('Enter your full name in incorrect casing: ')
name = name.lower().lstrip().rstrip().replace(" ", "_")
print(name)