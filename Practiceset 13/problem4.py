# Write a program to filter a list of numbers which are divisible by 5

l = [1,2,5,10,11,15,30,25,20]
def div(n):
    if n%5==0:
        return True
    return False
divfiveonly = list(filter (div,l))
print(divfiveonly)
