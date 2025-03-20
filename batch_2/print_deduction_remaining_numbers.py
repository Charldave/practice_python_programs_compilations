#create empty list
list = []
#for loop range to 10
for count in range (0, 10):
    num = float(input(f'Enter number {count+1}: '))#input
#append input to list
    list.append(num)
#subtract input
first_num = list[0]
for num in list[1:]:
    first_num -= num
    print(f'{first_num}')#result