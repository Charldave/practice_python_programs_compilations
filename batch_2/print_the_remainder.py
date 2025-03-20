#set variable inputs
num_1 = float(input(f"Enter 1st num: "))
num_2 = float(input(f"Enter 2nd num: "))

if num_2 == 0:
    print('invalid input, cannot be divided by zero')
else:
#check remainder using modulus %
    remainder = num_1%num_2
#if statements !=0, print remainder
    if remainder != 0:
        print(f"The remainder of {num_1} over {num_2} is {remainder}")
#elif print no remainder
    else:
        print("no remainder")