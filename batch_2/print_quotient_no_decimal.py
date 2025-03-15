#set variable for inputs
num_1=float(input("Enter the first number: "))
num_2=float(input("Enter the second number: "))
#if statement
if num_2!=0:
    #set quotient operation
    quotient=num_1/num_2
    print((f"{int(num_1)} divided by {int(num_2)} is {int(quotient)}"))
#else statement
else:
    print("invalid")