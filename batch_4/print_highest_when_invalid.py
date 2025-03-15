#set variable to None
highest_num=None
#start while true loop
while True:
    try:
        num=float(input('Enter number: '))
    #set if is None or > condition
        if highest_num is None or num>highest_num:
            highest_num=num#update variable value
    except ValueError:
        print('invalid')
        break
#print result