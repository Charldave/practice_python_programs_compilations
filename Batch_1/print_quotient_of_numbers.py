#set variables and inputs
num_1=float(input("Enter the first number: "))
num_2=float(input("Enter the second number: "))
#use if statements with "" operator to reject 0
if num_1==0 or num_2==0:
    print(' Inavlid input "0"')
else:
#divide the inputs using "/"
    quotient=num_1/num_2
#print result
    print (f"{num_1} divided by {num_2} is {quotient}")