from functools import reduce
# Write a program to find the maximum of the numbers in a list using the reduce function.
l =[10,20,55,32,55,88,99,69,96,56,45,12,23,32]
def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))