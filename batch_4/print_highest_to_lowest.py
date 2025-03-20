#basically the same as batch_3/print_lowest_to_highest.py with reverse sort
list = []
while True:
    try:
        num = float(input('Enter number: '))
        list.append(num)#append inputs
    except ValueError:
        print('Invalid input, proceeding to sort')
        break
#.sort()
list.sort(reverse=True)#add reverse=True to reverse the outputs
print(list)