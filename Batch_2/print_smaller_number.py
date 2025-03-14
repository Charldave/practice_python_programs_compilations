#set variable for inputs
num_1=float(input("Enter the first number: "))
num_2=float(input("Enter the second number: "))
#if elif statement > and <, print result
if num_1>num_2:
    print(f'{num_2} is smaller')
elif num_1<num_2:
    print(f'{num_1} is smaller')
elif num_1==num_2:
    print("Both are equal")