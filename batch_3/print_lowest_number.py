#set list=None
lowest_number=None
#while True loop
while True:
    try:
        #ask user input
        num=int(input('Enter a number: '))
        if lowest_number is None or num<lowest_number:
            lowest_number=num#updates value
    except ValueError:
        print('invalid input.')
        break