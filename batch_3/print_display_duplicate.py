#set list[]
list=[]
#for loop range 10
for count in range (0, 10):
    #input variabes, ask user
    num=float(input(f'Enter number {count+1}:'))
    #append(input)
    list.append(num)
#duplicate list
duplicated=[]
#for num in list
for num in list:
    #if .count num>1
    if list.count(num)>1:
        duplicated.append(num)
#print result
print(f'duplicate numbers {duplicated}')