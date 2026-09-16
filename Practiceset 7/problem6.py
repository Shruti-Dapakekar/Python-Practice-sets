# Write a program to calculate the factorial of a given number using for loop.
a = int(input("Enter a number:"))
factorial = 1
for i in range(1,a+1):
    factorial = factorial * i
print(f"The factorial of {a} is  {factorial}")
