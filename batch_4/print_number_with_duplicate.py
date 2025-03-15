#set list[]
list=[]
for count in range (0, 10):
    num=float(input(f'Enter number {count+1}: '))#input
    list.append(num)#append(input)
#duplicate list
duplicates=[]

for num in list:
    if list.count(num) > 1 and num not in duplicates:
         #duplicate.append
        duplicates.append(num)
print(duplicates)#output
