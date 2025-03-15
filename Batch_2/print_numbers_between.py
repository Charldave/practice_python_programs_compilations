#set variables for user input 1 and 2
first_num=int(input("Enter first number: "))
second_num=int(input('Enter second number: '))
#if 1>2
if first_num>second_num:
    #1, 2 = 2, 1
    first_num, second_num=second_num, first_num
#for loop in range(1, 2)
for count in range(first_num, second_num+1):
    #print result
    print(count)