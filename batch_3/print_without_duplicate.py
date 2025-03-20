#set empty list
list = []
#ask user for inputs, for loop range 10
for count in range(0, 10):
    num = float(input(f'Enter number {count+1}: '))
    #.append(inputs)
    list.append(num)
#no duplicates list
no_dupli = []
#for loop in list
for num in list:
    #.count(num) 
    if list.count(num) == 1:
        no_dupli.append(num)
#print result
print(f'Non-duplicated numbers are {no_dupli}.')