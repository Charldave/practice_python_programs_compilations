#set total=0
total = 0
#use for loop in range 10
for count in range(0, 10):
    #set variable for inputs/ask user to input
    number = float(input(f'Enter number {count+1}: '))
    #add input to the total
    total += number
#print the total
print(f'the total of all numbers is {total}')