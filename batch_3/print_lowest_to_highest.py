#create a list
list=[]
while True:
    try:
        num=float(input('Enter number: '))
        list.append(num)#append inputs
    except ValueError:
        print('Invalid input, proceeding to sort')
        break
#.sort()
list.sort()
print(list)