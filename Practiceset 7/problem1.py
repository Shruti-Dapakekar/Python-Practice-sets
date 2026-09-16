# Write a program to print multiplication table of a given number using for loop.
a = int(input("Enter a number: "))
for i in range(1,11):
    print(a, 'x', i ,'=', a*i)