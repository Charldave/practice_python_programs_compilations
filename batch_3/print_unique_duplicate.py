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
        #if in list display duplicate
        #else display unique
        #list.append()
    #except valueerror
    except ValueError:
        print("invalid inputs please try again")
        break