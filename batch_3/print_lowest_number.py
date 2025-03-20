#set list=None
lowest_number = None
#while True loop
while True:
    try:
        #ask user input
        num = int(input('Enter a number: '))
        if lowest_number is None or num < lowest_number:
            lowest_number = num#updates value
    except ValueError:
        print('invalid input.')
        break
#determines the lowest or no lowest
if lowest_number is not None:
    print(f'{lowest_number} is the lowest')
else:
    print('no lowest number')