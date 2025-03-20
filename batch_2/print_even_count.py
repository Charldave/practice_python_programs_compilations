#set even count=0
even_count = 0
#for loop range 10
for count in range (0, 10):
    num=float(input(f'Enter number {count+1}: '))#ask inputs
#if %2==0
    if num%2 == 0:
#even count+=1
        even_count += 1
#print even count
print(f'Even count is {even_count}')