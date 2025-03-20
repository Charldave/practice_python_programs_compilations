#create list
list = []
#while loop inputs
while True:
    try:
        num = float(input('Enter a number: '))
        list.append(num)
#no int input, display no valid number
    except ValueError:
        print('Inavlid number input ')
        break
count_dict = {}#used a empty dictionary instead 
for num in list:
    count_dict[num] = count_dict.get(num, 0) + 1
#finds the number with biggest count
most_dupli = None
max_count = 0
for num, count in count_dict.items():
    if count > max_count:
        max_count = count
        most_dupli = num
#display result
print(f"The number with the most duplicates is: {most_dupli}")