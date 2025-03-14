#set variable for inputs
num_1=float(input("Enter the first number: "))
num_2=float(input("Enter the second number: "))
#set quotient operation
quotient=num_1/num_2
#if statement
if quotient!=0:
    print((f"{num_1} divided by {num_2} is {int(quotient)}"))
#else statement
else:
    print("invalid")