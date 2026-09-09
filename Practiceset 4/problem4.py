#WAP to sum a list of 4 numbers

num=[]
for i in range(4):
    n=int(input("Enter a number {}:".format(i+1)))
    num.append(n)
print("The sum of all numbers: ",sum(num))