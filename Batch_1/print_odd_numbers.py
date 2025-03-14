#initialize a variable for odd
odd_count = 0
#use for loop
for count in range(10):
#set input variable
    num = int(input(f"Enter number {count+1} : "))
#if statement with modulus
    if num % 2 != 0:
#add 1 value in odd variable
        odd_count += 1
#print result
print(f'the amount of odd numbers you entered is {odd_count}')