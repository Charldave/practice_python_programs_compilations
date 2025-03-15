#create list
list=[]
#while True loop
while True:
    try:
        user_num=input('Enter a number: ')#ask user input
        
        if user_num == "" or not user_num.isdigit():#if input not a number
            print('Please Enter a valid number')#display invalid
            break
        #convert to int
        number=int(user_num)
        #if in list display duplicate
        if number in list:
            print('Duplicate')
        #else display unique
        else:
            print('Unique')
        #list.append()
        list.append(number)
    #except valueerror
    except ValueError:
        print("invalid inputs please try again")
        break