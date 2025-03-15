#set list[]
list=[]
#for loop range 10
for count in range (0, 10):
    #input variabes, ask user
    num=float(input(f'Enter number {count+1}: '))
    #append(input)
    list.append(num)
#remove dupli list
removed_dupli=[]

print("no duplicates: ")
for num in list:
    if num not in removed_dupli:
        print(num)
        removed_dupli.append(num)#to record duplicates