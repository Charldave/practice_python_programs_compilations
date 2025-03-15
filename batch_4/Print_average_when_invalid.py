#same while loop as print_highest_to_lowest.py and batch_3/print_lowest_to_highest.py so i skipped pseudocode
list=[]
while True:
    try:
        num=float(input('Enter number: '))
        list.append(num)#append inputs
    except ValueError:
        print('Invalid input, calculating average.')
        break
#the lines i added to calculate the average
if list: #if statement to have two output
    average=sum(list)/len(list)#sum to get total and len to get divisor
    print(f'the average of all inputs are {average:.2f}')#:.2f for 2 decimal
else:
    print(f'invalid inputs')